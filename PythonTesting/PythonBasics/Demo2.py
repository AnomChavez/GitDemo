
values = [1, 2, "rahul", 4, 5]

print(values[0]) #1

print(values[3]) #4


print(values[-1]) #5

print(values[1:3]) #2 rahul 4
values.insert(3, "shetty")

print(values) #[1, 2, 'rahul', 'shetty', 4, 5]

values.append("End") #[1, 2, 'rahul', 'shetty', 4, 5, 'End']

print(values)

values[2] = "Rahul" #Updating

del values[0] #delete

print(values)

# Dictionary

dic = {"a":2 , 4:"bcd", "c":"Hello world"}


print(dic[4])
print(dic["a"])

#
dict = {}

dict["firstname"] = "Rahul"

dict["lastname"] = "shetty"

dict["gender"] = "Male"


print(dict)
print(dict["lastname"])