# Conversion of one datatype into another datatype

a = "5"
b = "10"
print(a+b)
print(int(a) + int(b))

# string to integer
string = "15"
number = 29
string_number = int(string)
print(number + string_number)

# integer to string
num = 15
word = "Apples"
print(str(num) + word)

# integer to boolean
x = 1
y = 0
print(bool(x), bool(y))

#list to tuple
list1 = [34, 19, 28, 57]
list1 = tuple(list1)
print(list1)

#tuple to list
colors = ("red", "green", "blue")
colors = list(colors)
print(colors)