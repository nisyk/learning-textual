'''
Inheritance: A mechanism where a new class (child/subclass) derives attributes and methods from an existing class (parent/base class).
super(): A built-in function that returns a temporary object of the superclass, allowing the child class to call methods from the parent. Most commonly used in __init__ to ensure the parent's initialization logic runs.
Method Overriding: When a child class defines a method with the exact same name as a method in the parent class. The child's version replaces (overrides) the parent's version for instances of the child class.
isinstance(): A built-in function to check if an object is an instance of a class or its subclasses.
'''

class HardwareModule:
    """Base class for all hardware modules."""

    def __init__(self, module_id: str, voltage: float):
        self.module_id = module_id
        self.voltage = voltage
        self.is_active = False

    def power_on(self):
        self.is_active = True
        print(f"[{self.module_id}] Powered on at {self.voltage}V.")

class DisplayModule(HardwareModule):
    """Subclass for display modules, inheriting from HardwareModule."""

    def __init__(self, module_id: str, voltage: float, resolution: str):
        # Call the parent's __init__ to set module_id and voltage
        super().__init__(module_id, voltage)
        # Initialize subclass-specific attributes
        self.resolution = resolution

    # Overriding the parent method
    def power_on(self):
        # Call the parent's power_on method first
        super().power_on()
        # Add subclass-specific behavior
        print(f"[{self.module_id}] Initializing display at {self.resolution} resolution.")

# Usage
lcd = DisplayModule(module_id="LCD-01", voltage=3.3, resolution="1920x1080")
lcd.power_on()
# Output:
# [LCD-01] Powered on at 3.3V.
# [LCD-01] Initializing display at 1920x1080 resolution.

# -------------------------------

'''
Requirements:

    - Create a base class NetworkNode with an __init__ that takes node_id (str) and mac_address (str). It should also initialize is_connected to False.
    - Add a method connect() to NetworkNode that sets is_connected to True and prints "[node_id] Connecting via wired link...".
    - Create a subclass WirelessNode that inherits from NetworkNode. Its __init__ should take node_id, mac_address, and a new attribute frequency_ghz (float).
    - Use super() in WirelessNode.__init__ to properly initialize the parent attributes.
    - Override the connect() method in WirelessNode. It should first call the parent's connect() method using super(), and then print "[node_id] Tuning antenna to [frequency_ghz] GHz.".
    - Instantiate one NetworkNode and one WirelessNode. Call connect() on both to demonstrate the overridden behavior and the use of super().
    
'''

class NetworkNode:
    def __init__(self, node_id: str, mac_address: str):
        self.node_id = node_id
        self.mac_address = mac_address
        self.is_connected = False

    def connect(self) -> None:
        self.is_connected = True
        print(f"{self.node_id} Connected via wired link...")

class WirelessNode(NetworkNode):
    def __init__(self, node_id: str, mac_address: str, frequency: float):
       super().__init__(node_id, mac_address)
       self.frequency_ghz = frequency

    def connect(self):
        super().connect()

        print(f"{self.node_id} ({self.mac_address}): Connecting via wireless link with frequency {self.frequency_ghz}.")

esp32_wired = NetworkNode(node_id='esp32', mac_address='00:11:22:33:44:55')
esp32_wired.connect()
esp32 = WirelessNode(node_id='esp32', mac_address='01:02:03:04:05:06', frequency=3.3)
esp8266 = WirelessNode(node_id='esp8266', mac_address='06:05:04:03:02:01', frequency=2.2)
esp32.connect()
esp8266.connect()