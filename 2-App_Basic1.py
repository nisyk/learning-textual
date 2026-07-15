
'''
The App Class: The root node of the Textual Document Object Model (DOM). Every TUI you build will subclass textual.app.App.
run() Method: The method that starts the Textual event loop. It is a blocking call; the program will not exit this method until the app is closed.
on_mount() Lifecycle Hook: An asynchronous method that Textual calls exactly once when the App has been fully initialized, the terminal is ready, and the DOM is built. It is the equivalent of your embedded system's setup() or init() function.
__main__ Guard: The standard Python idiom if __name__ == "__main__": ensures your app only runs when the script is executed directly, not when imported as a module.
'''

'''
from textual.app import App

class BootSequence(App):
    """A minimal Textual application."""
    
    # Optional: Set the title of the terminal window
    TITLE = "System Boot"

    async def on_mount(self) -> None:
        """Called when the app is fully initialized and ready."""
        # In a real app, we would compose UI elements here.
        # For now, we just print to the console to prove it runs.
        print("Kernel initialized. Event loop started.")

if __name__ == "__main__":
    # Instantiate the app
    app = BootSequence()
    # Start the event loop (this blocks until the app exits)
    app.run()
'''

'''
Common Mistakes:
    - Forgetting to Instantiate: Calling BootSequence.run() directly on the class instead of creating an instance (app = BootSequence(); app.run()). Why it happens: Confusing class methods with instance methods. run() requires an instance to manage the specific DOM tree.
    - Blocking the Event Loop: Putting a time.sleep(5) or a heavy while loop inside on_mount(). Why it happens: Treating the UI thread like a standard C++ main() loop. Textual's event loop must remain free to process terminal inputs and redraw the screen. Blocking it will freeze the UI. (We will cover Async/Workers later to solve this!).
    - Not knowing how to exit: When you run a blank Textual app, it takes over the terminal. How to exit: Press Ctrl+Q in the terminal, or press q if you bind it later.
'''

'''
Requirements I:

    - Import App from textual.app.
    - Create a subclass called EmbeddedTerminal.
    - Set the TITLE class attribute to "Embedded OS v1.0".
    - Implement the on_mount() method. Inside it, use the self.notify() method (a built-in Textual method that shows a toast notification on the screen) to display the message: "System online.". (Note: self.notify is much better than print in Textual, as print can mess up the terminal rendering!)
    - Use the if __name__ == "__main__": guard to instantiate EmbeddedTerminal and call run().
    - Run the script. You should see a blank screen with a title bar at the top, and a toast notification pop up. Press Ctrl+C to exit the app.
'''

'''
Requirements II:

    - Import App and ComposeResult from textual.app.
    - Import Header, Footer, and Static from textual.widgets.
    - Create your EmbeddedTerminal class (keep the TITLE = "Embedded OS v1.0").
    - Implement the compose() method with the correct type hints.
    - yield a Header widget.
    - yield a Static widget containing the text: "Awaiting sensor data..."
    - yield a Footer widget.
    - Keep your on_mount() method from the previous quest to show your boot notifications!
    - Run the script. You should see a beautiful TUI with a top bar, a bottom bar, and your text in the middle, alongside your colored boot notifications!

'''

from textual.app import App, ComposeResult
from textual.widgets import Footer, Header, Static


class EmbeddedTerminal(App):
    TITLE = "Embedded OS v1.0"
    BINDINGS = [("q", "quit", "Exit Application")]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Static("Awaiting sensor data...")
        yield Footer()

    def on_mount(self) -> None:

        self.notify("System online.")
        self.action_notify(message="Embedded OS v1.0 by NISY.", severity="warning")

    def action_quit(self) -> None:
        self.app.exit()

if __name__ == "__main__":
    app = EmbeddedTerminal()
    app.run()