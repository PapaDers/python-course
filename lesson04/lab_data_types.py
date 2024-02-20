# String data type

# literal assignment
first = "Anders"
last = "Tonnesen"

# print(type(first))
# print(type(first) == int)
# print(isinstance(first, str))


# # Int data type
# number = 42
# print(type(number))


# # constructor function
# pizza = str("Pepperoni")
# print(type(pizza))
# print(type(pizza) == int)
# print(isinstance(pizza, str)) # Is pizza an instance of str (class?)?

# Concatenation
fullname = first + " " + last
# print(fullname)

# fullname += " is the best!"
# print(fullname)


# Casting a number to a string
decade = str(1980)
# print(type(decade))
# print(decade)

statement = "I like all sorts of music from the " + decade + "s."
# print(statement)


# Multiple lines
multiline = """
Hey, how are you?

I was just checking in.

This is Python and I am learning


....All good?                           oorrr not?

"""
# print(multiline)


# Escaping special characters
sentence = "I'm back at work!\tHey!\n\nWhere's this at\\located? "
# print(sentence)


# String Methods (methods are functions that belong to an object/class?)
# print(first)
# print(first.lower())
# print(first.upper())
# print(first)
# print(multiline)
# print(multiline.title())
# print(multiline.replace("Python", "Anders"))


# print(len(multiline))
# multiline += "                                      "
# multiline = "                  " + multiline
# print(len(multiline))
# print(len(multiline.strip()))
# print(len(multiline.lstrip()))
# print(len(multiline.rstrip()))


# Build a menu
# title = "menu".upper()
# print(title.center(20, "#"))
# print("Coffee".ljust(16, ".") + "$1".rjust(4))
# print("Muffin".ljust(16, ".") + "$2".rjust(4))
# print("Cheesecake".ljust(16, ".") + "$4".rjust(4))

# print("")

# # string index values
# print(first[1])
# print(first[-1])
# print(first[1:-1])
# print(first[0:])
# print(first[-1:])


# Some methods return boolean data
# print(first.startswith("A"))
# print(first.startswith("Z"))

myvalue = True
x = bool(False)
print(type(x))


# Numeric data types

# integer type
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))

# float type

gpa = 3.28
y = float(1.14)
# print(type(gpa))
# print(type(y))


# # complex type
# comp_value = 5 + 3j
# print(type(comp_value))
# print(comp_value.real)
# print(comp_value.imag)


# print(abs(gpa))
# print(round(gpa))

# print(round(gpa, 1))
# print(round(gpa, 2))


string = "tes t"
import math

# print(math.pi)
# print(math.sqrt(64))
# print(math.ceil(gpa))
# print(math.floor(gpa))


# Casting a string to a number
zipcode = "10001"
zip_value = int(zipcode)
print(type(zip_value))
