def function1():
   print("hii")
   print("how are you")
   print("fine")

function1()
o/p-
hii
how are you
fine


**Passing arguments to functions
def add(a,b):
   sum=a+b;
   print(sum)

add(10,20)
add(30,40)


**Return some value in Function
def add(a,b):
   c=a*b;
   return c;

print(add(10,20))

**Passing functions as argument
def add(a,b):
   return a+b

def square(c):
   return c*c

result=square(add(2,3))
print(result)
