'''
@property (Getter): A decorator that turns a method into a read-only attribute. It allows you to compute a value or retrieve a "backing field" without the caller needing to use parentheses ().
@<attribute>.setter: A decorator that defines the write logic for a property. This is where you enforce validation rules before updating the underlying data.
Backing Fields: Because a property method shares the name of the attribute, you must store the actual data in a "private" backing field (conventionally prefixed with an underscore, e.g., _value) to avoid infinite recursion.
Type Hinting: Using var: type and -> type to document expected data types. While Python doesn't enforce these at runtime, static analyzers (like mypy in PyCharm) use them to catch bugs before compilation.
'''

'''
class PowerSupply:
    """A power supply with strict voltage limits."""
    
    def __init__(self, name: str, max_voltage: float):
        self.name: str = name
        self.max_voltage: float = max_voltage
        # Backing field for the property
        self._voltage: float = 0.0 

    @property
    def voltage(self) -> float:
        """Getter: Returns the current voltage."""
        return self._voltage

    @voltage.setter
    def voltage(self, new_voltage: float) -> None:
        """Setter: Validates and sets the voltage."""
        if new_voltage > self.max_voltage:
            raise ValueError(f"Overvoltage! {new_voltage}V exceeds max {self.max_voltage}V.")
        if new_voltage < 0:
            raise ValueError("Voltage cannot be negative.")
        self._voltage = new_voltage

    def status(self) -> str:
        return f"[{self.name}] Output: {self.voltage}V / Max: {self.max_voltage}V"

class AdjustablePSU(PowerSupply):
    """Subclass that overrides the status method."""
    
    def __init__(self, name: str, max_voltage: float, efficiency: float):
        super().__init__(name, max_voltage)
        self.efficiency: float = efficiency

    # Overriding the parent method
    def status(self) -> str:
        base_status = super().status()
        return f"{base_status} | Efficiency: {self.efficiency * 100}%"

# Usage
psu = AdjustablePSU(name="Main Rail", max_voltage=12.0, efficiency=0.95)
psu.voltage = 5.0  # Uses the setter
print(psu.status)  # Wait, this is a property, but status() is a method!
print(psu.status()) # Correct!
'''

'''
Common Mistakes:

    - The Infinite Recursion Trap: Inside the @voltage.setter, writing self.voltage = new_voltage. Why it happens: This calls the setter again, creating an infinite loop that crashes the program. You must assign to the backing field: self._voltage = new_voltage.
    - Forgetting the Setter: Defining @property but forgetting @<attribute>.setter, then trying to assign a value to it later. Why it happens: A property without a setter is strictly read-only.
    - Mixing up Methods and Properties: Trying to call a property like a method (obj.voltage()) or accessing a method like a property (obj.status).

Challenge: We need to build a safe motor controller class.

Requirements:

    - Create a base class HardwarePeripheral.
    - __init__ takes name (str) and max_current_ma (int). Use type hints for all parameters and return types.
    - Create a @property for current_draw_ma (int). It should return the value of a backing attribute _current_draw_ma.
    - Create a @current_draw_ma.setter that checks if the new value exceeds max_current_ma. If it does, raise a ValueError("Overcurrent protection triggered!"). Otherwise, set the backing attribute.
    - Create a method status(self) -> str that returns a string: "Peripheral [name] drawing [current]mA".
    - Create a subclass Motor that inherits from HardwarePeripheral. Its __init__ takes name, max_current_ma, and rpm (int).
    - Override the status() method in Motor. It should call super().status() and append " | Spinning at [rpm] RPM" to the end.
    - Execution: Instantiate a Motor. Set its current to a safe value and print its status. Then, use a try...except block to attempt setting the current above the max limit, catching the ValueError and printing the error message.
'''

class HardwarePeripheral:
    def __init__(self, name: str, max_current_ma: int):
        self.name: str = name
        self.max_current_ma: int = max_current_ma

    @property
    def current_draw_ma(self) -> int:
        return self._current_draw_ma

    @current_draw_ma.setter
    def current_draw_ma(self, new_current_draw_ma:int) -> None:
        if new_current_draw_ma > self.max_current_ma:
            raise ValueError("Overcurrent protection triggered!")
        self._current_draw_ma = new_current_draw_ma

    def status(self) -> str:
        return f"Pheriperal [{self.name}] drawing [{self.current_draw_ma} mA]"

class Motor(HardwarePeripheral):
    def __init__(self, name: str, max_current_ma: int, rpm: int):
        super().__init__(name, max_current_ma)
        self.rpm: int = rpm

    def status(self) -> str:
        base = super().status()
        return f"{base} | Spinning at [{self.rpm}] RPM"

motor1 = Motor(name='Sanyo', max_current_ma=10, rpm=100)
try:
    motor1.current_draw_ma = 15
    print(motor1.status())
except ValueError as e:
    print(e)


