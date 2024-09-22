# Write a function my Reverse() which receives a string as an input and returns the reverse of the string

def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str

s = "Roshon"

print("The original string is : ", end="")
print(s)

print("The reversed string(using loops) is : ", end="")
print(reverse(s))
