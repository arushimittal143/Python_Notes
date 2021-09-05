file = open("demo.txt", "w")
file.write("This is first line")
file.close()

file = open("demo.txt", "r")
content=file.read()
print(content)
file.close()

file = open("demo.txt", "a")
file.write(" new content added")
file.close()
