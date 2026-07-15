'''
Class: A blueprint or template for creating objects. It defines a set of attributes (data) and methods (functions) that the created objects will have.
Object (Instance): A concrete entity created from a class blueprint. You can create multiple independent objects from a single class.
__init__ Method: The constructor. It is automatically called when a new object is instantiated. It initializes the object's attributes.
self: A reference to the current instance of the class. It must be the first parameter of any instance method (including __init__) to access and modify the object's specific attributes.

'''

class GPIOPin:

    def __init__(self, pin_number: int, mode: str):
        # 'self' menghubungkan variable ini ke object spesifik
        self.pin_number = pin_number
        self.mode = mode
        self.state = False

    def toggle(self):

        self.state = not self.state
        print(f"Pin {self.pin_number} toggled to {'HIGH' if self.state else 'LOW'}")

    # Instantiating objects
led_pin = GPIOPin(pin_number=13, mode='OUTPUT')
button_pin = GPIOPin(pin_number=22, mode='INPUT')

led_pin.toggle()
print(f"Button state: {button_pin.state}")


'''
Now let's create an instance of a class blueprint for EmbeddedSensor:
'''

class EmbeddedSensor:
    def __init__(self, sensor_id: str, i2c_address: int):
        self.sensor_id = sensor_id
        self.i2c_address = i2c_address
        self.is_calibrated = False

    def calibrate(self) -> str:
        self.is_calibrated = True
        if self.is_calibrated:
            return "The sensor is calibrated!"



    def read_temperature(self):
        if self.is_calibrated:
            return 22.5
        else:
            return "Error! The sensor is not calibrated!"

dht11 = EmbeddedSensor(sensor_id='DHT11', i2c_address=10)
dht22 = EmbeddedSensor(sensor_id='DHT22', i2c_address=13)

print("--------------------")
dht11.calibrate()
if dht11.is_calibrated and dht22.is_calibrated:
    print("These sensor is calibrated!")


print(f"Sensor ID: {dht11.sensor_id}, I2C address: {dht11.i2c_address}")
print(f"Temperature for {dht11.sensor_id}: {dht11.read_temperature()}")

print(f"Sensor ID: {dht22.sensor_id}, I2C address: {dht22.i2c_address}")
print(f"Temperature for {dht22.sensor_id}: {dht22.read_temperature()}")