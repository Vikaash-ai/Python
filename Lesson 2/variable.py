Vikaash = "Vikaash"

name = input("Write your name: ")

age = input("Write your age: ")

formating = format(name, age)

print("Hello ", name , "Welcome for joining Codingal you are ",age, "years old")

# New way 1
print("Hello {1} Welcome to Codingal where we code you are {0} years old!" .format(age, name))

# New way 1 Doubt
print(f"Hello {format} Welcome to Codingal where we code you are {formating} years old!")