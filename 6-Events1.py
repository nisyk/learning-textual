"""
Objective:
Master the @on decorator to catch and handle widget events (like Button.Pressed or Switch.Changed), bridging the gap between UI interaction and backend logic.
"""

"""
- Messages (Events): Textual widgets emit messages when things happen (e.g., Button.Pressed, Input.Changed, Switch.Changed).
- The @on Decorator: The modern, clean way to bind an event to a method. Syntax: @on(EventType, "#widget_id").
- Event Handlers: The decorated method receives the event object as an argument (e.g., def on_switch_changed(self, event: Switch.Changed):).
- Importing on: You must explicitly import it: from textual import on.
"""

'''
from textual.app import App, ComposeResult
from textual.widgets import Button, Static
from textual import on

class EventDemo(App):
    # Use an instance variable to track state
    click_count: int = 0

    def compose(self) -> ComposeResult:
        yield Button("Click Me", id="btn1")
        yield Static("Clicks: 0", id="counter")

    @on(Button.Pressed, "#btn1")
    def increment_counter(self, event: Button.Pressed) -> None:
        self.click_count += 1
        counter = self.query_one("#counter", Static)
        counter.update(f"Clicks: {self.click_count}")

if __name__ == "__main__":
    app = EventDemo()
    app.run()
'''

"""
Common Mistakes:

    - Forgetting the # in the @on selector: Writing @on(Button.Pressed, "btn1"). 
        Why it happens: Forgetting CSS selector syntax. Correction: It must be "#btn1" to target the ID.
    - Forgetting to import on: Trying to use @on without from textual import on. 
        Why it happens: Assuming it's a built-in Python keyword.
    - Using the old naming convention: Writing def on_button_pressed(self, event): without the decorator. 
        Why it happens: Looking at older Textual tutorials. Correction: While still supported for backwards compatibility, @on is the modern standard and is much more explicit.
"""

"""
Challenge:
Let's build a power state toggle for our embedded system.
Requirements:

    - Create an App subclass called EventTerminal.
    - In compose(), yield a Switch with id="sw_power".
    - Below it, yield a Static widget with id="status" and initial text "Power: OFF".
    - Import on from textual.
    - Create a method decorated with @on(Switch.Changed, "#sw_power").
    - Inside the method, check the event.value attribute (which is True or False).
    - Use self.query_one("#status", Static) to get the label.
    - Use .update() to change the text to "Power: ON [OK]" if event.value is True, or "Power: OFF [CRITICAL]" if False.
    - Run the script and click the switch to see the state change in real-time!
"""

from textual.app import App, ComposeResult
from textual.widgets import Switch, Static
from textual import on

class EventTerminal(App):
    TITLE = "Login Terminal"

    def compose(self) -> ComposeResult:
        yield Switch(id='sw_power')
        yield Static("Power: OFF", id='status')

    @on(Switch.Changed, "#sw_power")
    def check_status(self, event: Switch.Changed) -> None:
        state = self.query_one("#status", Static)
        if event.value:
            state.update(f"Power: ON [OK]")
            self.notify(f"Power: ON [OK]", severity='information')
        else:
            state.update(f"Power: OFF [CRITICAL]")
            self.notify("Power: OFF", severity='error')

if __name__ == "__main__":
    app = EventTerminal()
    app.run()