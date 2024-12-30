from functools import reduce
# Function:
#     Function syntax
#     Lambda syntax
#     Parameter types (named, positioned, args, kwargs, ...)
# Lambda functions use cases
# map, filter, zip, reduce functions
# Scopes:
#     Definition of scope
#     Local, nonlocal and global, enclosing scope

# Syntax for function
def some_function() -> None:
    pass

# Lambda function, returns sum of args
x = lambda a, b: a + b
print(x(1,2)) # = 3 

# Lambda functions are use as anonymus functions inside other functions
def triple(n):
    return lambda a,b: a*b*n

mytripler = triple(2)
print(mytripler(2,3)) # = 2 * 2 * 3

# We can use lambda functions with map, filter, zip, reduce functions.
# Map function, we use it to apply a given function to every element in a list. It returns an map object -> which is an iterator
s = [1, 2, 3]

def potential(x: int) -> int:
    return x * x
potential_s = map(potential, s)
print(list(potential_s))

# The same with lambda
res = list(map(lambda a: a * a, s))
print(res)

# Filter function, based on the condition a function returns, items are returned
def is_one(x: int) -> bool:
    if x == 1:
        return True
    return False

res = list(filter(is_one, s))
print(res)

lambda_res = list(filter(lambda x: True if x == 1 else False, s))
print(lambda_res)

# The zip functions takes iterables and aggregates them into a tuple
x = [ 1, 2 ,3]
x_s = [ "one", "two", "three"]
print(*zip(x, x_s))

# Reduce is used to apply a particular function on all elements
def addition(x: int, y: int) -> int:
    return x + y

res = reduce(addition, x)
print(res)

lambda_res = reduce(lambda x, y: x + y, x)
print(lambda_res)
