"""
Objective:
Master event bubbling to catch messages at the container or App level without targeting specific widget IDs, and learn how to halt event propagation.
"""

"""
- Message Bubbling: By default, when a widget generates an event, it passes it to its parent, then its grandparent, all the way up to the App. 
- Global @on Selectors: If you omit the CSS selector in the @on decorator (e.g., @on(Button.Pressed)), the method will catch that event for any widget of that type that bubbles up to it.
- event.button / event.control: When catching an event globally, you need to know which widget triggered it. For Button.Pressed, the event object has a .button attribute pointing to the source widget. For Input.Changed, it's .control.
- event.stop(): If you handle an event and want to prevent it from bubbling up any further (to stop parent containers or the App from seeing it), you call event.stop().
"""

'''
from textual.app import App, ComposeResult
from textual.containers import Horizontal
from textual.widgets import Button, Static
from textual import on

class CentralController(App):
    def compose(self) -> ComposeResult:
        with Horizontal():
            # No IDs needed for the global handler, but good practice anyway
            yield Button("Start", id="btn_start", variant="success")
            yield Button("Stop", id="btn_stop", variant="error")
        yield Static("Awaiting command...", id="log")

    # Catch ALL Button.Pressed events that bubble up to the App
    @on(Button.Pressed)
    def handle_any_button(self, event: Button.Pressed) -> None:
        # Identify which button was pressed using the event's source
        button_id = event.button.id
        log_widget = self.query_one("#log", Static)

        if button_id == "btn_start":
            log_widget.update("System Started.")
        elif button_id == "btn_stop":
            log_widget.update("System Halted.")

        # Stop the event from bubbling further (though it's at the App level,
        # so it has nowhere else to go, but it's good practice to show it)
        event.stop()

if __name__ == "__main__":
    app = CentralController()
    app.run()
'''

"""
Common Mistakes:

    - Forgetting event.button or event.control: Trying to use event.id directly on the event object. 
        Why it happens: Assuming the event object is the widget. Correction: The event is a message about the widget. You must access the source widget via event.button (for Buttons) or event.control (for Inputs/Switches).
    - Catching events too early: Putting a global @on(Button.Pressed) on a Container, but then wondering why the App isn't seeing it. 
        Why it happens: Forgetting that if a parent handles it and calls event.stop(), the bubble pops and the App never gets it.
    - Using event.widget: Trying to use event.widget. 
        Why it happens: Confusion with other GUI frameworks like Tkinter. Correction: Textual uses event.button, event.control, or event.switch depending on the specific message type.
"""

"""
Challenge: Let's build a centralized color mixer control panel.
Requirements:

    - Create an App subclass called BubbleTerminal.
    - In compose(), yield a Horizontal container.
    - Inside the container, yield three buttons: "RED" (id="btn_red"), "GREEN" (id="btn_green"), and "BLUE" (id="btn_blue").
    - Below the container, yield a Static widget with id="color_display" and initial text "Selected: NONE".
    - Write ONE App-level event handler using @on(Button.Pressed) (no ID selector).
    - Inside the handler, check event.button.id.
    - Update the Static widget's text to "Selected: RED", "Selected: GREEN", or "Selected: BLUE".
    - Bonus: Use self.notify() to show a toast notification. Use severity="error" for Red, severity="success" for Green, and severity="information" for Blue.
    - Run the script and click the buttons. Notice how a single function handles all three!
"""

from textual.app import App, ComposeResult
from textual.containers import Horizontal
from textual.widgets import Button, Static
from textual import on

class BubbleTerminal(App):
    CSS = '''
    #color_display {
        dock: bottom;
        height: 1;
    
    }
    '''
    def compose(self) -> ComposeResult:
        with Horizontal():
            yield Button("RED", id="btn_red", variant="error")
            yield Button("GREEN", id="btn_green", variant="success")
            yield Button("BLUE", id="btn_blue", variant="primary")

        yield Static("Selected: NONE", id="color_display")

    @on(Button.Pressed)
    def button_handler(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        state = self.query_one('#color_display', Static)

        if button_id == "btn_red":
            state.update(f"Selected: RED")
            self.notify(f"Selected: RED", severity='error')
        if button_id == "btn_green":
            state.update(f"Selected: GREEN")
            self.notify(f"Selected: GREEN", severity='warning')
        if button_id == "btn_blue":
            state.update(f"Selected: BLUE")
            self.notify(f"Selected: BLUE", severity='information')

if __name__ == "__main__":
    app = BubbleTerminal()
    app.run()