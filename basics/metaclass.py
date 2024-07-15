# In Python, a metaclass is a class of a class that defines how a class behaves. 
# A class is an instance of a metaclass. 
# Metaclasses are powerful tools for metaprogramming, allowing you to control the creation, modification, and behavior of classes at a higher level than class decorators.

class MyMeta(type):
    # this method is called before the class is created. It receives the class itself, the name of the class, the base classes, and the dictionary of attributes and methods. It should return the newly created class
    def __new__(cls, name, bases, dct):
        print(f"Creating class {name}")
        return super().__new__(cls, name, bases, dct)
    # This method is called after the class is created. It can be used to modify the class after it has been created
    def __init__(cls, name, bases, dct):
        print(f"Initializing class {name}")
        super().__init__(name, bases, dct)
    # This method is called when an instance of the class is created. It can be used to control instance creation
    def __call__(cls, *args, **kwargs):
        print(f"Instantiating {cls.__name__}")
        return super().__call__(*args, **kwargs)

# Using the metaclass
class MyClass(metaclass=MyMeta):
    def __init__(self, value):
        self.value = value

# Creating an instance
instance = MyClass(10)



class MyMeta2(type):
    def __new__(cls, name, bases, attrs):
        attrs['x'] = 10
        return super().__new__(cls, name, bases, attrs)

class MiClass2(metaclass=MyMeta2):
    pass

object2 = MiClass2()
print(object2.x)


class TrackInstances(type):
    instances = []
        
    def __call__(cls, *args, **kwargs):
        TrackInstances.instances.append(cls)
        for instance in TrackInstances.instances:
            print(f"Instantiated {instance.__name__}")


class MyClass3(metaclass=TrackInstances):
    pass

class MyClass4(metaclass=TrackInstances):
    pass

class3 = MyClass3()
class4 = MyClass4()
