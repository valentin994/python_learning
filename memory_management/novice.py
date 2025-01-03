# Refcount

from sys import getrefcount
from ctypes import c_long
a = 20
b = a

# Python is using references, so when creating b from a we are not copying the value but the address
#   which means that the id, or the address of both variables it the same

# Python keeps track of memory references, when that count gets to 0, the object gets destroyed and the
#   memory reclaimed


print(f"Refcount for a: {getrefcount(a)}")
print(f"Refcount with clong for a: {c_long.from_address(id(a)).value}")

print(f"id of a: {id(a)} & id of b: {id(b)}")
a = a + 2

# If we change the value of a, we get a different adress
print(f"id of a: {id(a)} & id of b: {id(b)}")

print(f"Refcount for a: {getrefcount(a)}")


