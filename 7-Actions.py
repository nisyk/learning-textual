"""
Objective:
Master the BINDINGS class attribute and the action_* method naming convention to trigger backend logic via keyboard shortcuts.

"""
"""
- BINDINGS Class Attribute: A list of tuples defining your keyboard shortcuts. Format: [(key, action_name, description), ...].
    Example: BINDINGS = [("q", "quit", "Quit App"), ("t", "toggle", "Toggle State")]
- action_* Methods: Textual's action system uses reflection to find methods. If your binding says "toggle", Textual will look for a method named action_toggle(self).
- The Footer Widget: If you yield Footer() in your compose() method, it will automatically read the BINDINGS list and display the keys and descriptions at the bottom of the screen.
- Built-in Actions: Textual has some built-in actions, like quit (which exits the app) and focus_next / focus_previous (which tabs through widgets).

"""

"""
from textual.app import App, ComposeResult
from textual.widgets import Footer, Static


class ActionDemo(App):
    # Define the keyboard bindings
    BINDINGS = [
        ("t", "toggle_light", "Toggle Light"),
        ("q", "quit", "Quit"), # Built-in action to exit
    ]

    is_light_on: bool = False

    def compose(self) -> ComposeResult:
        yield Static("Light is OFF", id="light_status")
        yield Footer() # Automatically displays the BINDINGS!

    # The action system automatically routes the 't' key to this method
    def action_toggle_light(self) -> None:
        self.is_light_on = not self.is_light_on
        status_widget = self.query_one("#light_status", Static)

        if self.is_light_on:
            status_widget.update("Light is ON 💡")
        else:
            status_widget.update("Light is OFF")

if __name__ == "__main__":
    app = ActionDemo()
    app.run()

"""

"""
Common Mistakes:

    - Mismatching the Action Name: Defining ("t", "toggle_light", "...") in BINDINGS but naming the method def toggle_light(self):. 
        Why it happens: Forgetting the action_ prefix. Correction: The method must be named action_toggle_light.
    - Forgetting to Yield Footer(): Defining bindings but not seeing them on the screen. 
        Why it happens: Forgetting that Footer is just a standard widget that needs to be yielded in compose() to display the key hints.
    - Using complex logic inside the action: Putting 50 lines of blocking code inside action_toggle_light. 
        Why it happens: Treating it like a standard function. Correction: Actions should be quick state toggles or trigger background workers (which we will cover in Level 11).
"""

"""
Challenge: Let's build a keyboard-controlled motor relay.
Requirements:

    - Create an App subclass called RelayTerminal.
    - In compose(), yield a Static widget with id="relay_status", initial text "Relay: OPEN [SAFE]", and center its content.
    - Yield a Footer widget so the operator can see the key hints.
    - Define a BINDINGS class attribute with a single tuple: ("m", "toggle_motor", "Toggle Motor").
    - Create an instance variable self.motor_running = False in the class (or __init__).
    - Implement the action_toggle_motor(self) method.
    - Inside the method, flip the self.motor_running boolean.
    - Query the #relay_status widget and .update() its text to "Relay: CLOSED [DANGER]" if True, or "Relay: OPEN [SAFE]" if False.
    - Bonus: Use self.notify() to alert the operator of the state change (use "error" severity for CLOSED/DANGER, and "information" for OPEN/SAFE).
    - Run the script. Press the m key on your keyboard to toggle the relay without using the mouse!

"""

from textual.app import App, ComposeResult
from textual.widgets import Static, Footer

class RelayTerminal(App):
    BINDINGS = [
        ("m", "toggle_motor", "Toggle Motor"),
    ]
    # for set it to middle, ik it would override other component, but this is the easiest method for me
    CSS = """
    #relay_status {
    width: 100%;
    height: 100%;
    content-align: center middle;
    }
    """


    motor_running: bool = False

    def compose(self) -> ComposeResult:
        yield Static("Relay: OPEN [SAFE]", id="relay_status")
        yield Footer()




    def action_toggle_motor(self) -> None:
        self.motor_running = not self.motor_running
        relay_state = self.query_one("#relay_status", Static)

        if self.motor_running:
            relay_state.update("Relay: CLOSED [DANGER]")
            self.notify("Relay: CLOSED [DANGER]", severity="error")
        else:
            relay_state.update("Relay: OPEN [SAFE]")
            self.notify("Relay: OPEN [SAFE]", severity="information")

if __name__ == "__main__":
    app = RelayTerminal()
    app.run()