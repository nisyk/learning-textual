"""
Objective:
Master Textual's native CSS (TCSS) selectors to target widgets by their Type, Class, and ID, and understand how specificity dictates which styles are applied.
"""

'''
- Type Selectors: Target all widgets of a specific class. Syntax: Button { ... }. (Lowest specificity).
- Class Selectors: Target widgets that have a specific class assigned via the classes argument in Python. Syntax: .my-class { ... }. (Medium specificity).
- ID Selectors: Target one specific widget using its unique id. Syntax: #my-id { ... }. (Highest specificity).
- Descendant Selectors: Target widgets nested inside other containers. Syntax: Vertical Button { ... } (Targets any Button inside a Vertical) or Vertical > Button { ... } (Targets only direct child Buttons).
- Specificity Rule: If a widget matches multiple selectors, the most specific one wins. ID > Class > Type.
'''
'''

from textual.app import App, ComposeResult
from textual.containers import Vertical
from textual.widgets import Button, Static

class SelectorDemo(App):
    CSS = """
    /* Type Selector: Applies to ALL buttons */
    Button {
        width: 20;
        height: 3;
        margin: 1;
    }
    
    /* Class Selector: Applies to widgets with classes="danger" */
    .danger {
        background: $error;
        color: $text;
    }
    
    /* ID Selector: Applies ONLY to the widget with id="special-btn" */
    #special-btn {
        background: $success;
        color: $text;
        border: tall $warning;
    }
    
    /* Descendant Selector: Applies to Static widgets inside a Vertical */
    Vertical Static {
        text-style: italic;
        color: $text-muted;
    }
    """
    

    def compose(self) -> ComposeResult:
        with Vertical():
            yield Static("System Controls:")
            # This button gets Type + Class styles
            yield Button("Abort", classes="danger")
            # This button gets Type + ID styles (ID overrides Class if it had one)
            yield Button("Launch", id="special-btn")
            # This button gets only Type styles
            yield Button("Standby")

if __name__ == "__main__":
    app = SelectorDemo()
    app.run()
'''

"""
Common Mistakes:

    Forgetting the . or #: Writing my-class { ... } instead of .my-class { ... }. 
    Why it happens: Forgetting CSS syntax. Without the dot, Textual thinks you are targeting a widget type named my-class, which doesn't exist.
    Using Web CSS Properties: Trying to use color: red; or background-color: blue;. 
    Why it happens: Web CSS habits. Correction: Textual uses color for text, but background (not background-color) for the background. And it prefers hex codes (#ff0000) or theme variables ($error) over named colors like red.
    Confusing classes with class: In Python, passing class="my-class" to a widget. Why it happens: Python keyword collision. 
    Correction: Textual uses the plural classes="my-class1 my-class2" to allow multiple classes on a single widget.
"""

"""
Challenge: Let's build a styled control panel using strict selector rules.
Requirements:

    - Create an App subclass called StyledPanel.
    - In compose(), yield a Vertical container with id="control_box".
    - Inside the container, yield three Button widgets:
        - First button: label "Start", id "btn_start".
        - Second button: label "Pause", classes "action-btn".
        - Third button: label "Stop", classes "action-btn".
    - Below the buttons, yield a Static widget with text "Status: Idle", id "status_text".
    - Write the CSS block with the following rules:
        - Type Selector: Make all Button widgets have width: 16 and height: 3.
        - Class Selector: Make all .action-btn widgets have background: $warning and color: $text.
        - ID Selector: Make #btn_start have background: $success and color: $text.
        - Descendant Selector: Target the Static widget inside #control_box and give it text-style: bold and margin-top: 2.
    - Run the script. You should see the Start button green, the Pause/Stop buttons yellow, and the status text bolded and spaced out!

"""

from textual.app import App, ComposeResult
from textual.widgets import Button, Static
from textual.containers import Vertical

class StyledPanel(App):
    TITLE = "StyledPanel"
    CSS = '''
    Button {
    width: 16;
    height: 3;
    }
    .action-btn {
    background: $warning;
    color: $text;
    }
    #btn_start {
    background: $success;
    color: $text;
    }
    
    #control_box Static {
    text-style: bold;
    margin-top: 2;
    }
    
    '''
    def compose(self) -> ComposeResult:
        with Vertical(id="control_box"):
            yield Button(label='start', id='btn_start')
            yield Button(label='pause', classes='action-btn')
            yield Button(label='stop', classes='action-btn')
            yield Static("Status: Idle", id='status_text')

if __name__ == "__main__":
    app = StyledPanel()
    app.run()
