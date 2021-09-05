#Write a function which would divide two numbers, design the function in a manner that it handles the divide by zero exception.


def divide(a, b):
    try:
        return (a // b)
    except ZeroDivisionError:
         print("This is division by zero error")
         return 0;

a=int(input("First number"))
b=int(input("Second number"))

result=divide(a, b)
print(result)
