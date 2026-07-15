"""
Objective:
Master the Grid container and its associated TCSS (Textual CSS) properties to create complex, multi-column and multi-row 2D layouts.
"""

"""
- The Grid Container: A specialized container from textual.containers that lays out its children in a 2D grid.
- TCSS (Textual CSS): Textual uses its own CSS-like language for styling and layout. It is not web CSS. It is parsed natively by Textual.
- grid-size Property: The most important TCSS property for grids. It takes two integers: grid-size: <columns> <rows>;. (e.g., grid-size: 2 2; creates a 2x2 matrix).
- grid-gutter Property: Adds spacing (gutter) between grid cells so your widgets don't touch each other.
- Applying CSS in Python: You can pass a CSS string directly to the App using the CSS class attribute, or load it from an external .tcss file. For now, we will use the inline CSS string for simplicity.
"""

'''
from textual.app import App, ComposeResult
from textual.containers import Grid
from textual.widgets import Static



class GridDashboard(App):
    TITLE = "2D Matrix Dashboard"

    # Inline TCSS (Textual CSS)
    CSS = """
    #my_grid {
        grid-size: 2 2; /* 2 columns, 2 rows */
        grid-gutter: 1; /* 1 cell of space between items */
        height: 100%;   /* Make the grid fill the screen vertically */
    }
    
    .grid-item {
        background: $surface;
        border: tall $primary;
        content-align: center middle; /* Center text inside the widget */
    }
    """

    def compose(self) -> ComposeResult:
        # Yield the Grid container with an ID so our CSS can target it
        with Grid(id="my_grid"):
            yield Static("Temp: 22°C", classes="grid-item")
            yield Static("Hum: 45%", classes="grid-item")
            yield Static("Pres: 1013hPa", classes="grid-item")
            yield Static("Volt: 3.3V", classes="grid-item")

if __name__ == "__main__":
    app = GridDashboard()
    app.run()

'''

"""
Common Mistakes:

    - Using Grid without TCSS: Yielding a Grid but forgetting to define grid-size in CSS. Why it happens: Assuming Grid automatically figures out the layout. Correction: Without grid-size, Textual defaults to a single column, and it will just look like a Vertical container!
    - Confusing TCSS with Web CSS: Trying to use display: grid; or grid-template-columns: 1fr 1fr;. Why it happens: Muscle memory from web development. Correction: Textual's TCSS uses grid-size: 2 2; and grid-columns: 1fr 1fr;. Stick strictly to the Textual documentation for CSS rules!
    - Forgetting height: 100%: The grid might collapse to the height of its contents. Why it happens: Containers shrink to fit their children by default in Textual. You must explicitly tell the grid to expand to fill the screen.
"""

"""
Challenge: Let's build a 2D telemetry matrix for our embedded system.
Requirements:

    - Create an App subclass called TelemetryMatrix.
    - Define a CSS class attribute. Inside it, create an ID selector for #sensor_grid.
    - Set the CSS for #sensor_grid to have grid-size: 2 2; and grid-gutter: 1;. Also set height: 100%;.
    - In compose(), yield a Grid with id="sensor_grid".
    - Inside the Grid, yield four Static widgets representing: "Core Temp: 45°C", "Memory: 64% Used", "Network: 100Mbps", and "Uptime: 14h". Give them all a class of "cell" (and add a simple .cell CSS rule to give them a border).
    - Run the script. You should see a beautiful, perfectly spaced 2x2 grid of sensor readouts!

"""

from textual.app import App
from textual.widgets import Static
from textual.containers import Grid


class TelemetryMatrix(App):
    TITLE = "Telemetry Matrix"
    CSS = '''
    #sensor_grid {
    
    grid-size: 2 2;
    grid-gutter: 1;
    height: 100%;
    }
    
    .grid-item {
    background: #3c3836;
    border: solid #fe8819;
    content-align: center middle;
    height: 100%;
    }
    
    '''



    def  compose(self):
        with Grid(id="sensor_grid"):
            yield Static("Core Temp: 45°C", classes="grid-item", id="sensor_core")
            yield Static("Memory: 64% Used", classes="grid-item", id="sensor_memory")
            yield Static("Network: 100Mbps", classes="grid-item", id="sensor_network")
            yield Static("Uptime: 14h", classes="grid-item", id="sensor_uptime")

if __name__ == "__main__":
    app = TelemetryMatrix()
    app.run()