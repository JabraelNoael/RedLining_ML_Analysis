def p(self):
    print(self)
    return self

object.p = p  # add method to base object

# Example:
x = 42
x.p()   # prints 42

"hello".p()  # prints hello