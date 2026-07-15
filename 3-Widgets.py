'''

Master the Static widget, learn how to target specific widgets using IDs, and update their content dynamically at runtime.
'''

'''
- The Static Widget: The workhorse of Textual. Despite the name, it doesn't just hold static text. It can render plain text, rich text, and even Markdown. 
- Widget IDs: Just like HTML or CSS, you can assign an id to a widget (e.g., Static("Hello", id="my_label")). This allows you to target it later.
- query_one(): A DOM traversal method. self.query_one("#my_label", Static) searches the UI tree for the widget with the ID my_label and ensures it is of type Static.
- update(): The correct method to change the content of a Static widget. Never try to assign directly to a .text or .value attribute on a Static widget; it won't trigger a redraw. You must use widget.update("new content").
'''
'''

from textual.app import App, ComposeResult
from textual.widgets import Static
import asyncio

class TelemetryScreen(App):
    async def compose(self) -> ComposeResult:
        # Yield a Static widget with a unique ID
        yield Static("Initializing sensors...", id="sensor_display")

    async def on_mount(self) -> None:
        # Simulate a 1-second hardware boot delay
        await asyncio.sleep(1)
        
        # Target the widget by its ID and update its content
        display = self.query_one("#sensor_display", Static)
        display.update("Sensor online: 22.5°C")

if __name__ == "__main__":
    app = TelemetryScreen()
    app.run()

'''
'''
Common Mistakes:

    - Using widget.text = "...": Why it happens: Confusing Textual widgets with standard Python objects or Tkinter/PyQt widgets. Textual relies on reactive state. Using .update() ensures the Textual engine knows the DOM has changed and schedules a screen redraw.
    - Forgetting the # in query_one: Writing self.query_one("sensor_display"). Why it happens: Forgetting CSS selector syntax. In Textual (and CSS), an ID selector requires the hash/pound symbol (#). A class selector would use a dot (.).
    - Blocking on_mount with time.sleep(): Using the synchronous time.sleep() instead of await asyncio.sleep(). Why it happens: C++/standard Python habits. time.sleep() blocks the entire Textual event loop, freezing the UI. asyncio.sleep() yields control back to the event loop, keeping the UI responsive.
'''

'''
Requirements:

    - Create an App subclass called SensorDashboard.
    - In compose(), yield a Static widget with the initial text "Awaiting data..." and give it the id="temp_readout".
    - In on_mount(), use await asyncio.sleep(2) to simulate a 2-second sensor polling delay.
    - After the sleep, use self.query_one() to find the "#temp_readout" widget.
    - Use the .update() method to change the text to "Core Temp: 45.2°C [NORMAL]".
    - Wait another 2 seconds (await asyncio.sleep(2)).
    - Query the widget again and .update() it to "Core Temp: 89.9°C [CRITICAL]".
    - Run the script and watch the text change dynamically on the screen!

'''

from textual.app import App, ComposeResult
from textual.widgets import Static
from textual import work

import asyncio


class SensorDashboard(App):
    TITLE = "SensorDashboard"

    def compose(self) -> ComposeResult:
        yield Static("Awaiting data...", id="temp_readout")

    @work
    async def on_mount(self) -> None:
        temp_reading = self.query_one("#temp_readout", Static)
        await asyncio.sleep(2)

        temp_reading.update("Core Temp: 45.2°C [NORMAL]")

        await asyncio.sleep(2)
        temp_reading.update("Core Temp: 89.9°C [CRITICAL]")

if __name__ == '__main__':
    app = SensorDashboard()
    app.run()
