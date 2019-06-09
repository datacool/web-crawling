f = open("C:\Temp\sample_data.txt", 'w')
data = "easy_python_crawler\n" + "Hello World"
f.write(data)
f.close()


f = open("C:\Temp\sample_data.txt", "r")
f.read()
f.close()

f = open("C:\Temp\sample_data.txt", "r")
for str in f.readlines():
    print(str)
f.close()

f = open("C:\Temp\sample_data.txt", "r")
for str in f.readline():
    print(str)
f.close()