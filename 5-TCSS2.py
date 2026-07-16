"""
Objective:
Master the TCSS Box Model (margin, padding, and border) to control the spatial relationships, clearance, and physical boundaries of your widgets.
"""

"""
- margin: The transparent space outside the widget's border. It pushes other widgets away. 
    Syntax: margin: 1; (all sides) or margin: 1 2 3 4; (Top, Right, Bottom, Left).

- padding: The space inside the widget's border, surrounding the content. It pushes the text/content away from the edge.
    Syntax: padding: 1; or padding: 1 2; (Top/Bottom, Left/Right).

- border: The visible edge of the widget. 
    - Syntax: border: <style> <color>; (e.g., border: solid $primary;).
    - Styles: solid, dashed, dotted, heavy, tall, thick, double.

- CRITICAL TEXTUAL DIFFERENCE: In Web CSS, borders and padding often add to the total width/height of an element. 
    In Textual, they do not. If you set width: 20;, the total width is 20. The border and padding will shrink the internal content area to fit inside that 20-character boundary.

"""

'''
from textual.app import App, ComposeResult
from textual.widgets import Static

class BoxModelDemo(App):
    CSS = """
    #microchip {
        /* Total width is 30, total height is 7 */
        width: 30;
        height: 7;
        
        /* The visible edge */
        border: heavy $warning;
        
        /* Space inside the border, pushing text away from the edge */
        padding: 1; 
        
        /* Space outside the border, pushing away from screen edges */
        margin: 2; 
        
        background: $primary;
        content-align: center middle;
    }
    """

    def compose(self) -> ComposeResult:
        yield Static("SILICON DIE", id="microchip")

if __name__ == "__main__":
    app = BoxModelDemo()
    app.run()
    
'''

'''
Common Mistakes:

    - Using Web CSS Border Syntax: Writing border: 1px solid red;. 
        Why it happens: Web CSS habits. Correction: Terminals don't have pixels. Textual uses border: solid red; (no width measurement). To make a border thicker, you change the style (e.g., border: heavy red; or border: thick red;).
    - Confusing align and content-align: Using align: center middle; to center text.
        Why it happens: Confusing widget alignment with text alignment. Correction: align positions the widget itself inside its parent container. content-align positions the text/content inside the widget.
    - Forgetting the Color in Border: Writing border: solid;. 
        Why it happens: Forgetting the second argument. Correction: Textual requires both style and color: border: solid $text;.
'''

'''
Challenge: Let's design a physical component socket to test the Box Model.
Requirements:

    - Create an App subclass called SocketLayout.
    - In compose(), yield a Static widget with the text "CORE", and give it id="core".
    - Below it, yield a second Static widget with the text "SHELL", and give it id="shell".
    - Write the CSS block with the following rules:
        For #core: 
            width: 20; height: 5;
            background: $primary;
            border: heavy $warning;
            padding: 1;
            margin: 2;
            content-align: center middle;
        For #shell:
            width: 30; height: 3;
            border: dashed $success;
            margin: 1 4; (1 cell top/bottom, 4 cells left/right).
            content-align: center middle;
    - Run the script. You should see two distinct boxes with clear spacing (margins) around them, thick/dashed borders, and internal padding pushing the text away from the borders.

'''

from textual.app import App, ComposeResult
from textual.widgets import Static

class SocketLayout(App):
    TITLE = "SocketLayout"
    CSS = """
    
    #core {
        width: 20;
        height: 5;
        border: thick $warning;
        background: $primary;
        padding: 1;
        margin: 2;
        content-align: center middle;
    }
    
    #shell {
        width: 30;
        height: 3;
        margin: 1 4;
        content-align: center middle;
        border: dashed $success;
    }
    """

    def compose(self) -> ComposeResult:
        yield Static("CORE", id="core")
        yield Static("SHELL", id="shell")

if __name__ == '__main__':
    app = SocketLayout()
    app.run()