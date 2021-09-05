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


#Writing and reading file
file = open("demo.txt", "w")
file.write("this is the text written into the file")
file.close()

file = open("demo.txt", "r")
content=file.read();
print(content)
#O/p-(console)this is the text written into the file

#Demo.txt
#this is the text written into the file

#Writing and reading and then writing-->In this the content written in first write gets deleted
file = open("demo.txt", "w")
file.write("this is the text written into the file")
file.close()

file = open("demo.txt", "r")
content=file.read();
print(content)

file = open("demo.txt", "w")
file.write("this is the new text")
file.close()

#O/p-(console)this is the text written into the file
#Demo.txt
#this is the new text

#Appending the content in the file
file = open("demo.txt", "w")
file.write("this is the text written into the file")
file.close()

file = open("demo.txt", "r")
content=file.read();
print(content)

file = open("demo.txt", "a")
file.write("this is the new text")
file.close()
#O/p-(console)this is the text written into the file
#Demo.txt
#this is the text written into the filethis is the new text


