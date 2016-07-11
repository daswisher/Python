file = open("test.txt", "r+")

content = file.read()
print file.tell()
file.seek(0)
print file.tell()
file.truncate()
file.write(content + "world!")

file.close()
