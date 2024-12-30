# Decorator definition.
# Decorator use cases.
# Simple decorator implementation
# Be able to write a simple function decorator (without parameters)
# Built-in decorators:
#   classmethod
#   staticmethod
#   property. getter, setter, deletter syntax
#--------------------------------------------------------------------

# Decorators allow us to wrap another function in order to extend the behaviour of the wrapped 
#   function, without permanently modifying it.

# Use cases: logging, timing, jit decorator

from collections.abc import Callable
import time

def simple_decorator(func: Callable) -> Callable:
    def inner(*args, **kwargs):
        print(f"I got invoked at {time.time()}, with args {args}, and kwargs {kwargs}")
        func(*args, **kwargs)
    return inner

@simple_decorator
def adder(x: int, y: int) -> int:
    return x + y 

adder(1, y=1)

# Classmethod 
# Used to define a method that is bound to the class and not the instance of the class.
#   This means that it can be called on the class itself rather than on instances of the class.
#   Class methods are useful when you need to work with the class itself rather than 
#   any particular instance of it.

# The Difference between Class Method and Static method is stated below. While a static method
#   requires no specific parameters, a class method takes cls as its first argument. 
#   While a static method cannot access or modify the class state, a class method can. Static methods are
#   typically unaware of the class state.

class A:
    x = 1

    def __init__(self, y) -> None:
        self.y = y 

    @classmethod
    def adder(cls) -> int:
        return cls.x+1

    @staticmethod
    def static_print():
        return "Hello world"
    

x = A(2)
print(x.adder())
print(A.static_print())
print(A.adder())


# Getter, Setter 
class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def get_x(self):
        return self._x

    def set_x(self, value):
        self._x = value

    def get_y(self):
        return self._y

    def set_y(self, value):
        self._y = value

# If we want to directly get/set methods without typing point.set_y = 2, we can use the property decorator
#   so instead of a dict lookup for the variable we will execute our getter/setter function

class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        self._x = 0


p = Point(1,2)
p.x = 3

# Main use as I see it is, when you want to run a function or some complex operations while setting an attribute


