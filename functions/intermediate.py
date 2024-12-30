# Functions as a 1st class citizens (as variable, as params,  as return values).
# Higher order functions.
# Function meta information – docstring, type hints, etc.
# Recursion:
#   Definition of recursive function
#   Definition of terminate point (terminate case), recursive step
#   Recursive functions pros and cons
# Scopes:
#   LEGB rule
# -----------------------------------------------------------------------------------------------------------------

# First class objects in a language are handled uniformly throughout. 
#   They may be stored in data structures, passed as arguments, or used in control structures. 
#   A programming language is said to support first-class functions if it treats functions as first-class objects. 
#   Python supports the concept of First Class functions.

# Properties of first class functions:
#    A function is an instance of the Object type.
#    You can store the function in a variable.
#    You can pass the function as a parameter to another function.
#    You can return the function from a function.
#    You can store them in data structures such as hash tables, lists, …

# A function is a higher order function if it contains another function as a parameter or returns a function

# Python functions offer several types of metadata
# def my_function(x: int) -> int: -> type hints
#   """Return x + 2""" -> docstring
#   return x + 2 
# print(my_function.__name__) -> function name

# Recursion
#  Functions are recursive if in execution they call themselfes, they have a base case/termination case
#  which is a case to determine if we are going to call the recursive function
#  Pros: 
#   reduces redundancy
#   reduces time complexity of a program 
#  Cons:
#   hard to understand sometimes
#   for the most part slower

# LEGB Rule
# The LEGB rule is a kind of name lookup procedure, which determines the order in which 
#   Python looks up names. For example, if you reference a given name, then Python will
#   look that name up sequentially in the local, enclosing, global, and built-in scope.
#   If the name exists, then you’ll get the first occurrence of it. Otherwise, you’ll get an error.
# Python scopes:
# Local - inside a function, variable not accessable outside of the function
# Global - accessable from anywhere
# Nonlocal(enclosing) - is used when there is a nested function with a variable, 
#   if we specify nonlocal then that variable will be accessable to the outer function
# Built-in - special scope that's created or loaded whenever you run a script or interactive
#   session. This scope contains names such as keywords, functions, exceptions; names that are
#   built in python
