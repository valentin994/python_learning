# Lambda functions:
#   Python lambda functions implementation details
#   How to implement recursion with lambdas

# Factorial

x = lambda a: 1 if a == 1 else a * x(a-1) 
print(x(7))
