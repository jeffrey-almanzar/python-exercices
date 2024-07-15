'''
Class properties in Python are special attributes defined within a class that are accessed like normal attributes but have methods (getter, setter, deleter) associated with them. They allow you to define custom behavior when getting, setting, or deleting an attribute.
'''

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    @property
    def diameter(self):
        return self.radius * 2
    
    @property
    def area(self):
        return 3.14 * self.radius ** 2
    
    @property
    def perimeter(self):
        return 2 * 3.14 * self.radius

# Usage
circle = Circle(5)
# @property: Decorates methods (diameter, area, perimeter) to make them properties.
print("Radius:", circle.radius)
print("Diameter:", circle.diameter)
print("Area:", circle.area)
print("Perimeter:", circle.perimeter)


'''
Descriptors are a more powerful way to define custom behavior for attributes. 
They allow you to define __get__, __set__, and __delete__ methods, which Python calls when accessing, assigning to, or deleting an attribute. 
Descriptors can be used to enforce constraints, validate data, or perform actions whenever an attribute is accessed.
'''

class Celsius:
    def __init__(self, temperature=0):
        self._temperature = temperature
    
    def to_fahrenheit(self):
        return (self.temperature * 9/5) + 32
    
    def get_temperature(self):
        print("Getting value...")
        return self._temperature
    
    def set_temperature(self, value):
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible")
        print("Setting value...")
        self._temperature = value
    
    temperature = property(get_temperature, set_temperature)

# Usage
c = Celsius()
c.temperature = 37
print("Celsius:", c.temperature)
print("Fahrenheit:", c.to_fahrenheit())
