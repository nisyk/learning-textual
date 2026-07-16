"""
Objective:
Master Textual's pseudo-classes (:hover, :focus, :active) to dynamically alter widget styles based on user interaction (mouse and keyboard).
"""

"""
- :hover: Applied when the user's mouse cursor is resting over the widget. (Great for visual feedback before a click).
- :focus: Applied when the widget has keyboard focus (selected via Tab key or mouse click). Only works on widgets that are focusable (like Button, Input, Switch).
- Combining Selectors: You can chain pseudo-classes to standard selectors. Example: Button:hover { background: $warning; }.
- Transitions (Bonus): While not strictly a pseudo-class, adding transition: background 200ms; to a widget makes the color change smoothly animate when the pseudo-class triggers, giving a premium 
"""

'''
from textual.app import App, ComposeResult
from textual.widgets import Button, Input

class InteractiveDemo(App):
    CSS = """
    Button {
        width: 20;
        margin: 1;
        /* Smoothly animate background changes */
        transition: background 200ms; 
    }
    
    /* Mouse is hovering over the button */
    Button:hover {
        background: $warning;
        color: $text;
    }
    
    /* Button has keyboard/mouse focus */
    Button:focus {
        /* Add a thick border to show it's selected */
        border: tall $success;
        /* Remove default padding so border doesn't shift text */
        padding: 0 1; 
    }
    
    /* Button is actively being clicked */
    Button:active {
        background: $error;
        color: $text;
    }
    
    Input {
        width: 30;
        margin: 1;
    }
    
    /* Change input border when focused */
    Input:focus {
        border: heavy $primary;
    }
    """

    def compose(self) -> ComposeResult:
        yield Button("Hover or Click Me!", id="btn1")
        yield Input(placeholder="Type here and press Tab...")

if __name__ == "__main__":
    app = InteractiveDemo()
    app.run()
'''

"""
Common Mistakes:

    - Forgetting the Colon: Writing Button:hover instead of Button:hover. 
        Why it happens: Typo. Correction: Pseudo-classes always require a single colon :. (Double colons :: are for pseudo-elements in web CSS, which Textual doesn't use).
    - Applying :focus to non-focusable widgets: Trying to style Static:focus. 
        Why it happens: Assuming all widgets can receive focus. Correction: By default, only interactive widgets (Button, Input, Switch, etc.) can receive focus. If you want a Static widget to receive focus, you must explicitly set can-focus: true; in its CSS.
    - Layout Shift on Focus: Adding a border on :focus without adjusting padding, causing the text inside the button to jump 1 character to the right when focused. 
        Why it happens: Forgetting the Box Model. Correction: If you add a border on focus, reduce the horizontal padding by the same amount to keep the text perfectly still.
"""

"""
Challenge: Let's build an interactive login terminal for our embedded OS.
Requirements:

    - Create an App subclass called LoginTerminal.
    - In compose(), yield an Input widget with placeholder="Enter Username", id="input_user".
    - Below it, yield a Button with label "AUTHENTICATE", id="btn_auth", and variant="primary".
    - Write the CSS block with the following rules:
        For #input_user: Give it width: 40; margin: 2;. When it is :focus, change its border to heavy $success;.
        For #btn_auth: Give it width: 20; margin: 2;. Add a transition: background 200ms;.
        For #btn_auth:hover: Change the background to $warning.
        For #btn_auth:focus: Add a tall $primary; border. (Remember to adjust padding so the text doesn't shift!).
        For #btn_auth:active: Change the background to $error.
    - Run the script. Hover over the button, click it, and use the Tab key to move focus between the Input and the Button to see the dynamic styles trigger!
"""

from textual.app import App, ComposeResult
from textual.widgets import Input, Button
from textual.containers import Vertical

class LoginTerminal(App):
    TITLE = "Login Terminal"
    CSS = '''
    
    #input_user {
        width: 40;
        margin: 2;    
    }
    #input_user:focus {
        border: heavy $success;
    }
    
    #btn_auth {
        width: 20;
        margin: 2;
        transition: background 200ms;
        box-sizing: content-box;

    }
    
    #btn_auth:hover {
        background: $warning;
    }
    
    #btn_auth:focus {
        outline: tall $primary;
        padding-left: 1;
        padding-right: 1;
        margin-left: 1;
    }
    


    '''

    def compose(self) -> ComposeResult:
        with Vertical():
            yield Input(placeholder="Enter Username", id="input_user")
            yield Button("AUTHENTICATE", id="btn_auth", variant="primary")

if __name__ == "__main__":
    app = LoginTerminal()
    app.run()
