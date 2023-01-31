x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

print(x)
print(y)
print(z)

#and cannot:
    #2myvar = "John"
    #my-var = "John"
    #my var = "John"


fruits = ["apple", "banana", "cherry"]
q, b, a = fruits
print(q)
print(b)
print(a)

#Global Variables

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)