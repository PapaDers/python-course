# Dictionaries
band = {
    "vocals": "Plant",
    "guitar": "Page",
}

band2 = dict(vocals="Plant", guitar="Page")

print(band)
print(band2)
print(type(band))
print(len(band))

# Access items
print(band["vocals"])
print(band.get("guitar"))

# list all keys
print(band.keys())

# list all values
print(band.values())

# list of key/value pairs as tuples
print(band.items())

# verify a key exists
print("guitar" in band)
print("triangle" in band)
print("Plant" in band)

# change dictionary values
band["vocals"] = "Coverdale"
print(band["vocals"])
band["cowbell"] = "Anders"
print(band)

band.update({"bass": "JPJ"})

print(band)

# remove items from dictionary
print(band.pop("bass"))
print(band)

band["drums"] = "Bonham"
print(band)


print(band.popitem())
print(band)

# delete and clear
band["drums"] = "Bonham"
print(band)
del band["drums"]
print(band)

band2.clear()
print(band2)

del band2

# band2 = band  # create a reference. Both refere to the same dictionary in memory. Changes to one, changes the other.
# print("Bad copy!")
# print(band2)
# print(band)

# band2["drums"] = "Dave"
# print(band)

band2 = band.copy()
band2["drums"] = "Dave"
print("Good copy!")
print(band)
print(band2)

# or use the dict() constructor function
band3 = dict(band)
print("Good copy!")
print(band3)
band["Tiangle"] = "Sara"
print(band)
print(band3)


# nested dictionaries
member1 = {"name": "Plant", "instrument": "vocals"}
member2 = {"name": "Page", "instrument": "guitar"}
band4 = {"member1": member1, "member2": member2}

print(band4)
print(band4["member1"]["name"])


# Sets

nums = {1, 2, 3, 4}

nums2 = set((1, 2, 3, 4))

print(nums)
print(nums2)
print(type(nums))
print(len(nums))


# no duplicates allowed in sets. They are also sorted.
nums = {1, 2, 2, 3, 4}
print(nums)

# true is a dupe of 1, false is a dupe of zero
nums = {5, True, 1, 2, False, 3, 4, 0}
print(nums)

# check if a value is in a set
print(False in nums)

# but you can't access a set by index or key

# add items to a set
nums.add(10)
print(nums)
nums.add(10)
print(nums)


# add elements from one set to another
morenums = {5, 6, 7}
nums.update(morenums)
print(nums)

# you can use update with lists, tuples, and dictionaries, too.
nums.update(band4)
print(nums)

# merge two sets to create a new set
one = {1, 2, 3}
two = {5, 6, 7}
mynewset = one.union(two)
print(mynewset)


# keep only the duplicates from both sets
one = {1, 2, 3}
two = {5, 6, 2, 3}

one.intersection_update(two)
print(one)


# keep everything except the duplicates from both sets
one = {1, 2, 3}
two = {5, 6, 2, 3}

one.symmetric_difference_update(two)
print(one)
