# Standard library decorators:
#   total_ordering
#   single_dispatch

# Given a class defining one or more rich comparison ordering methods, this class decorator supplies the rest.
#   This simplifies the effort involved in specifying all of the possible rich comparison operations: 
#   The class must define one of __lt__(), __le__(), __gt__(), or __ge__(). In addition, the class should supply
#   an __eq__() method.

# It is slower than supplying all comparison methods

from functools import total_ordering, singledispatch

@total_ordering
class Example:
    def __init__(self, x) -> None:
        self.x = x

    def __eq__(self, value: object ) -> bool:
        if value == self.x:
            return True
        return False

    def __gt__(self, value):
        if self.x > value:
            return True
        return False

x = Example(2)
print(x>1)
print(x==2)
print(x<9)

# Single dispatch is used for dynamically overloading functions. We can use it to exted a functions functionality
# We can define which function is to be called by defining the type of the input variables

@singledispatch
def simple_function(arg, verbose=False):
    if verbose:
        print("Let me just say", end=" ")
    print(arg)

@simple_function.register(int)
def _(arg, verbose=False):
    if verbose:
        print("I am very verbose now ")
    print(f"Called the registered int variation of simple function with {arg}")

simple_function(1)
simple_function("hell yeah")
