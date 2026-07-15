"""
Objective:
Master Textual's layout containers (Vertical and Horizontal) to organize widgets into structured rows and columns, replacing the default "stacked" layout.
"""

"""
- The Default Layout: By default, the App itself is a Vertical container. Every widget you yield directly into compose() is stacked top-to-bottom.
- Vertical Container: Groups widgets in a top-to-bottom column. (Useful when you need a specific section of the screen to be a column, nested inside a larger horizontal layout).
- Horizontal Container: Groups widgets in a left-to-right row. 
- Nesting / Yielding into Containers: To put widgets inside a container, you yield the container, and then yield the child widgets. Textual's compose() handles this nesting automatically based on indentation and sequential yields, or you can pass them as arguments.
- Center and Middle Containers: (Bonus) Center aligns children horizontally in the middle, Middle aligns them vertically in the middle.
"""

"""
from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Button, Static, Header, Footer


class DashboardLayout(App):
    TITLE = "Structured Dashboard"

    def compose(self) -> ComposeResult:
        yield Header()
        
        # A Horizontal row containing three buttons
        with Horizontal():
            yield Button("Start", id="btn_start", variant="success")
            yield Button("Pause", id="btn_pause", variant="warning")
            yield Button("Stop", id="btn_stop", variant="error")
            
        # A Vertical column containing static text
        with Vertical():
            yield Static("System Log:")
            yield Static("12:00 - Booted")
            yield Static("12:01 - Sensors Online")
            
        yield Footer()

if __name__ == "__main__":
    app = DashboardLayout()
    app.run()

"""

"""
Common Mistakes:

    - Forgetting to Import Containers: Trying to use Horizontal() without from textual.containers import Horizontal. Why it happens: Containers are in textual.containers, not textual.widgets.
    - Nesting too deeply without CSS: Creating 5 layers of Vertical and Horizontal containers. Why it happens: Trying to do CSS layout purely in Python. While containers work, Textual's CSS (TCSS) is actually much better at complex layouts. We will use containers for logical grouping, and TCSS for precise positioning later.
    - Using yield instead of with: Writing yield Horizontal(Button("A"), Button("B")). While this works, the with Horizontal(): yield Button("A") context manager syntax is heavily preferred in the Textual community for readability.
"""
"""
Challenge:
Let's restructure your OperatorPanel from the previous quest into a proper, organized HMI.
Requirements:

    - Import Horizontal and Vertical from textual.containers.
    - In compose(), yield a Header and a Footer.
    - Create a Horizontal container. Inside it, yield your "Deploy Payload" Button and your "Safety" Switch side-by-side.
    - Below that, create a Vertical container. Inside it, yield your Input (for altitude) and your Static status label, stacked on top of each other.
    - Run the script. You should see a top bar, a bottom bar, a row containing the button and switch, and a column below them containing the input and status text.
"""


from textual.app import App, ComposeResult
from textual.widgets import Input, Static, Button, Switch, Header, Footer
from textual.containers import Horizontal, Vertical

class HMI(App):

    TITLE = "HMIApp"
    def compose(self) -> ComposeResult:
        yield Header()
        with Horizontal():
            yield Button(label="Deploy Payload", id="btn_deploy", variant="warning")
            yield Switch(value=False, id="sw_safety")
        with Vertical():
            yield Input(id="input_altitude", placeholder="Altitude")
            yield Static("Status: [SAFE]", id="status")


        yield Footer()


if __name__ == "__main__":
    app = HMI()
    app.run()




