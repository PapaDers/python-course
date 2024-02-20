# users = ["Dave", "John", "Sara"]

# data = ["Jeff", "Jiff", "Jennifer"]

# emptylist = []

# # print("Dave" in data)

# # # print(users[1])
# # # print(users[2])
# # # print(data[-1])

# # print(users.index("Sara"))

# print(users[0:2])
# print(users[0:])
# print(users)
# print(len(data))


# users.append("Elsa")
# print(users)

# users += ["data"]
# print(users)

# users.extend(data)
# print(users)

# users.insert(0, "Bob")
# print(users)


# users[2:2] = ["Eddie", "Alex"]
# print(users)


# users[1:3] = ["Robert", "JPJ"]
# print(users)


# users.remove("Bob")
# print(users)


# print(users.pop())
# print(users)

# del users[0]
# print(users)

# # del data
# data.clear()
# print(data)


# users.sort()
# print(users)

# users.sort(key=str.lower)
# print(users)


# numbs = [4, 42, 78, 1, 5]
# print(numbs)
# numbs.reverse()
# print(numbs)


# # numbs.sort(reverse=True)
# # print(numbs)


# print(sorted(numbs, reverse=True))
# print(numbs)


# numbscopy = numbs.copy()
# print(numbscopy)


# mynumbs = list(numbs)

# mycopy = numbs[:]
# mycopy.sort()

# print(mycopy)
# print(numbscopy)
# print(mynumbs)
# print(numbs)


# print(type(numbs))

mylist = list([1, "Neil", True])
print(mylist)

mytuple = tuple(("Dave", 42, True))
anothertuple = (1, 2, 5, 6, 2, 12, 5, 6, 5)


print(mytuple)
print(type(mytuple))
print(type(anothertuple))


newlist = list(mytuple)
newlist.append("Neil")
newtuple = tuple(newlist)
print(newtuple)
print(mytuple)


(one, *two, hey) = anothertuple
print(one)
print(two)
print(hey)

print(anothertuple.count(5))
