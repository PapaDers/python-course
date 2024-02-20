# while loops excute block of code as long as condition is true
value = 1

# while value <= 10:
#     print(value)
#     if value == 5:
#         break
#     value += 1

# while value <= 10:
#     value += 1
#     if value == 5:
#         print("We reached 5!")
#         continue
#     print(value)
# else:
#     print("Value is now equal to " + str(value))

names = ["Dave", "Sara", "John"]
# for name in names:
#     print(name)

# for x in "Mississippi":
#     print(x)

# for name in names:
#     if name == "Sara":
#         break
#     print(name)

# for name in names:
#     if name == "Sara":
#         continue
#     print(name)

# for x in range(2, 4):
#     print(x)

for x in range(0, 100, 4):
    print(x)
else:
    print("We are done!")

names = ["Dave", "Sara", "John"]
actions = ["codes", "eats", "sleeps"]

# for name in names:
#     for action in actions:
#         print(name + " " + action + ".")

for action in actions:
    for name in names:
        print(name + " " + action + ".")
