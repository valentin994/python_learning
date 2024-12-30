# Scopes:
#     gloal and nonlocal keywords
#     global and nonlocal usecases in real world
#     Scopes in nested functions, closures
#     globals() and locals() functions: meaning, can we mutate them?
# Recursion:
#     Use cases
# Scopes:
#     Exception variables scope: referencing exception variable after try-except block
# -------------------------------------------------------------------------------------
from pprint import pprint as print
# Global variables can be accessed in functions but not modified if we do not use the keyword global
x = 1

def print_x() -> None:
    print(x) # -> This will work
    # x+=1 -> UnboundLocalError 

def add_global_x() -> None:
    global x
    x += 1

print_x()
add_global_x()
print(x)

# Nonlocal variables are all variables defined in a nested function
# The nonlocal keyword is used to work with variables inside nested functions, 
#   where the variable should not belong to the inner function.

def my_func() -> str:
    x = "Valentin"
    def my_func2() -> None:
        nonlocal x # Without the nonlocal the changed x would not be present in the return x
        x = "Hello"
        return 
    my_func2()
    return x

print(my_func())

# Closures
# In Python, a closure is a powerful concept that allows a function to remember and access variables from 
#   its lexical scope, even when the function is executed outside that scope. Closures are closely related 
#   to nested functions and are commonly used in functional programming, event handling and callbacks.

# A closure is created when a function (the inner function) is defined within another function (the outer function)
#   and the inner function references variables from the outer function. Closures are useful when you need
#   a function to retain state across multiple calls, without using global variables.

def fun(a):
    # Outer function that remembers the value of 'a'
    def adder(b):
        # Inner function that adds 'b' to 'a'
        return a + b
    return adder  # Returns the closure

# Create a closure that adds 10 to any number
val = fun(10)

# Use the closure
print(val(5))  
print(val(20))

# globals() & locals() return symbol tables

# The globals() method returns a dictionary with all the global variables and symbols for the current program. 
#  globals() can be used to modify global variables
print(globals())

# The locals() method returns a dictionary with all the local variables and symbols for the current program. 
# we can't mutate the locals
print(locals())

# Define a function named list_sum that takes a list of numbers as input
def list_sum(num_list):
    # Check if the length of the input list is 1
    if len(num_list) == 1:
        # If the list has only one element, return that element
        return num_list[0]
    else:
        # If the list has more than one element, return the sum of the first element
        # and the result of recursively calling the list_sum function on the rest of the list
        return num_list[0] + list_sum(num_list[1:])

# Print the result of calling the list_sum function with the input [2, 4, 5, 6, 7]
print(list_sum([2, 4, 5, 6, 7]))

# Try except does not introduce a new scope. We can define variables in the block but they might be unbound.
try:
    ks = "yes"
    raise NameError
except NameError:
    foo = "no"

print(foo)
