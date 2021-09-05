#Reading data from the file
#demo.txt
this is the first line
this is the second line

#Demo.py with read parameters
file = open("demo.txt", "r")
# w-write r-read
# do something with the file
content = file.read(20)
#20-no.of bytes parameter
print(content)
file.close()
O/p-this is the first li

#Demo.py to read only first Line
file = open("demo.txt", "r")
content = file.readline()
print(content)
file.close()
O/p-this is the first line


