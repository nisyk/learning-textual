"""
Objective:
Master the dock TCSS property to pin widgets to the absolute edges of the screen, removing them from the normal document flow.
"""

"""
- The dock Property: A TCSS property that pins a widget to an edge. Values: top, bottom, left, right.
- Removed from Flow: When a widget is docked, it no longer takes up space in the normal vertical/horizontal layout. It acts like an overlay.
- Order Matters: If you dock multiple widgets to the same edge (e.g., two widgets to the top), the first one yielded in compose() gets the absolute edge, and the second one docks just below it.
- Explicit Dimensions: Docked widgets need an explicit dimension in the direction they are docked. If you dock: top;, you must give it a height: X;. If you dock: left;, you must give it a width: X;. Otherwise, it will collapse to 0!
"""

'''
from textual.app import App, ComposeResult
from textual.widgets import Static

class ChassisLayout(App):
    TITLE = "Physical Enclosure"
    
    CSS = """
    #top-bezel {
        dock: top;
        height: 3;
        background: $primary;
        content-align: center middle;
    }
    
    #bottom-bezel {
        dock: bottom;
        height: 1;
        background: $surface;
    }
    
    #left-panel {
        dock: left;
        width: 20;
        background: $panel;
    }
    
    #main-display {
        /* No dock needed! It will automatically fill the remaining space */
        background: $background;
        content-align: center middle;
    }
    """

    def compose(self) -> ComposeResult:
        yield Static("SYSTEM TITLE", id="top-bezel")
        yield Static("STATUS: OK", id="bottom-bezel")
        yield Static("MENU\n-\n-\n-", id="left-panel")
        yield Static("MAIN DISPLAY AREA", id="main-display")

if __name__ == "__main__":
    app = ChassisLayout()
    app.run()
'''

"""
Common Mistakes:

    - Forgetting Explicit Dimensions: Writing dock: top; but forgetting height: 3;. 
        Why it happens: Assuming the dock will auto-size. Correction: Docked widgets shrink to their content size (which is often 0 or 1 line) unless you explicitly define their cross-axis dimension.
    - Overlapping Docked Widgets: Docking two things to left without giving them different widths or offsets, causing them to draw on top of each other. 
        Why it happens: Forgetting that docked widgets are essentially Z-axis overlays.
    - Trying to dock the last widget: Trying to dock the main central content area. 
        Why it happens: Not understanding that the undocked widgets automatically expand to fill the space left behind by the docked widgets.
"""

"""
Challenge: Let's build the physical chassis for our embedded HMI.
Requirements:

    - Create an App subclass called EmbeddedChassis.
    - Define a CSS block.
    - Create a Static widget with id="title_bar". Dock it to the top, give it a height: 3, and text "=== EMBEDDED OS ===".
    - Create a Static widget with id="status_bar". Dock it to the bottom, give it a height: 1, and text "STATUS: NOMINAL | MEM: 64%".
    - Create a Static widget with id="sidebar". Dock it to the left, give it a width: 15, and text "Logs:\n-\n-\n-".
    - Create a final Static widget with id="main_screen". Do not dock it. Give it the text "Awaiting Telemetry..." and center its content. It should automatically fill the remaining space in the middle!
    - Run the script. You should see a perfect window-like layout with a top bar, bottom bar, left sidebar, and a main central area.
"""

from textual.app import App, ComposeResult
from textual.widgets import Static

class EmbeddedChassis(App):
    TITLE = "Embedded Chassis"
    CSS = '''
    #title_bar {
        dock: top;
        height: 3;
        content-align: center middle;
        background: $success;
        color: black;
        border: solid $background;
    }
    
    #status_bar {
        dock: bottom;
        height: 1;
    }
    
    #sidebar {
        dock: left;
        width: 15;
        margin-top: 3;
        margin-bottom: 1;
        height: 100%;
        background: $background;
        border: solid $primary;
    }
    
    #main_screen {
        background: $background;
        content-align: center middle;
        height: 100%
    }
    '''

    def compose(self) -> ComposeResult:
        yield Static("=== EMBEDDED OS ===", id="title_bar")
        yield Static("STATUS: NORMAL | MEM 64%", id="status_bar")
        yield Static("Log \n-\n-\n-", id="sidebar")
        yield Static("Awaiting Telemetry...", id="main_screen")

if __name__ == "__main__":
    app = EmbeddedChassis()
    app.run()