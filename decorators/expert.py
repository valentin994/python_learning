# Closures internals (co_freevars, cell_contents)

# Cell objects are used to implement variables used by multiple scopes
# co_freevars are variables from the outer scope of a nested function

def foo():
    x = 1
    y = 2
    def bar():
        print(x,y)
    return bar

a = foo()

print(a.__closure__[0].cell_contents)
print(a.__closure__[1].cell_contents)
print(a.__code__.co_freevars)
