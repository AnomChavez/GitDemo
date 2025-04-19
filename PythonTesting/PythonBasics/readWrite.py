file = open('test.txt', 'r')
#Read all the contents of file
#read n number of characters by passing parameter
#print(file.read(5))
#read one single line at a time using readline()
#print(file.readline())
#print(file.readline())



#Print line by line using readLine method
# line = file.readline()
# while line != "":
#     print(line)
#     line = file.readline()

#values = [abc, b, "rahul", 4, 5] when in  a list it is easy to iterate, extract, evaluate
for line in file.readlines():
    print(line)





file.close()