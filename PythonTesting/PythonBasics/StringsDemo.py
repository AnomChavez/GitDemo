str = "RahulShettyAcademy.com"
str1 = "Consulting firm"
str3 = "RahulShetty"



print(str[1])  #a

print(str[0:5]) # if you want substring in python, like in loop syntax 0 - n-1

print(str+str1)  # concatenation


print(str3 in str) # substring check


var = str.split(".")
print(var)
print(var[0])

str4 = " great "

print(str4.strip())

print(str4.lstrip())

print(str4.rstrip())