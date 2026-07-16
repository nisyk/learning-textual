""""
Objective:
Master Textual's reactive descriptor to automatically synchronize Python variables with UI widgets, eliminating the need for manual query_one().update() calls.
"""

"""
 - reactive(): A special descriptor imported from textual.reactive. It turns a standard class attribute into a reactive state variable.
 - Declaration: my_counter: int = reactive(0). The type hint is mandatory for reactive variables to work correctly.
 - Automatic UI Binding: If you yield a widget that supports reactive binding (like Static using the renderable argument, or Input using value), Textual automatically links the widget to the reactive variable. When the variable changes, the widget updates itself.
 - The Paradigm Shift: You stop thinking "How do I update the UI?" and start thinking "How do I update my state?" The UI takes care of itself.
"""

'''
from textual.app import App, ComposeResult
from textual.widgets import Static, Button
from textual.reactive import reactive
from textual import on

class ReactiveRelay(App):
    # 1. Declare the reactive state variable
    is_energized: bool = reactive(False)

    def compose(self) -> ComposeResult:
        # Yield an empty Static widget. We will update it via the watcher.
        yield Static("RELAY: OPEN [SAFE]", id="relay_screen")
        yield Button("TOGGLE RELAY", id="btn_toggle")

    # 2. The Watcher: Automatically called when 'is_energized' changes!
    def watch_is_energized(self, new_value: bool) -> None:
        screen = self.query_one("#relay_screen", Static)
        if new_value:
            screen.update("RELAY: CLOSED [HIGH VOLTAGE]")
        else:
            screen.update("RELAY: OPEN [SAFE]")

    @on(Button.Pressed, "#btn_toggle")
    def toggle_relay(self) -> None:
        # 3. Just flip the variable! The watcher handles the UI.
        self.is_energized = not self.is_energized

if __name__ == "__main__":
    app = ReactiveRelay()
    app.run()


'''

"""
Common Mistakes:

    - Forgetting the watch_ prefix: Naming the method on_is_energized_changed. Why it happens: Confusing it with event handlers. Correction: Textual strictly looks for watch_ followed by the exact variable name.
    - Not updating the widget inside the watcher: Just printing to the console inside the watcher. Why it happens: Forgetting that the watcher's job is to bridge the state to the UI.
    - Initial State: The watcher is not called when the app first starts (unless you pass init=True to the reactive descriptor). You must set the initial text in compose() or on_mount().
"""

"""
Challenge:
Let's build a properly functioning Reactive Motor Controller.
Requirements:

    - Create an App subclass called ReactiveMotor.
    - Import reactive from textual.reactive.
    - Declare a reactive variable: motor_speed: int = reactive(0).
    - In compose(), yield a Static widget with id="speed_display" and initial text "Speed: 0%".
    - Yield three Buttons: "+" (id="btn_up"), "-" (id="btn_down"), and "STOP" (id="btn_stop").
    - Implement the watcher: watch_motor_speed(self, new_speed: int) -> None.
        Inside the watcher, query #speed_display and .update() it to show the new speed (e.g., "Speed: 50%").
        Bonus: If new_speed is > 80, change the Static widget's color to red (using self.query_one("#speed_display").styles.color = "red"). Otherwise, set it to default.
    - Implement @on(Button.Pressed, "#btn_up") to increase self.motor_speed by 10 (cap it at 100).
    - Implement @on(Button.Pressed, "#btn_down") to decrease self.motor_speed by 10 (cap it at 0).
    - Implement @on(Button.Pressed, "#btn_stop") to set self.motor_speed = 0.
    - Run the script. Click the buttons. Watch the UI update automatically via the watcher, without you ever calling .update() inside the button handlers!

"""

from textual.app import App, ComposeResult
from textual.widgets import Static, Button
from textual.reactive import reactive
from textual.containers import Horizontal
from textual import on

class ReactiveMotor(App):

    motor_speed: int = reactive(0)

    def compose(self) -> ComposeResult:
        yield Static("Speed 0%", id="speed_display")
        with Horizontal():
            yield Button("+", id="btn_up", variant="success")
            yield Button("-", id="btn_down", variant="warning")
            yield Button("STOP", id="btn_stop")

    def watch_motor_speed(self, new_speed: int) -> None:
        screen = self.query_one("#speed_display", Static)
        screen.update(f"Speed: {new_speed}")

        if self.motor_speed > 80:
            screen.styles.color = "red"
        else:
            screen.styles.color = "white"

        if self.motor_speed < 0:
            self.motor_speed = max(0, self.motor_speed)

    @on(Button.Pressed)
    def btn_pressed(self, event: Button.Pressed) -> None:
        btn_id = event.button.id

        if btn_id == "btn_up":
            self.motor_speed += 10
        if btn_id == "btn_down":
            self.motor_speed -= 10
        if btn_id == "btn_stop":
            self.motor_speed = 0

if __name__ == "__main__":
    app = ReactiveMotor()
    app.run()
