name = "Dave"
count = 1

print("count variable from global scope before calling another(): " + str(count))


def another():
    color = "pink"
    global count
    count += 1
    print("count variable from inside another() after being incremented: " + str(count))
    print("Color from inside another(): " + color)

    def greeting(name):
        nonlocal color
        color = "gold"
        print("Color from inside greeting(): " + color)
        print(name)

    greeting("Sara")
    print("Color from inside another() after calling greeting(): " + color)


another()
print("count variable from global scope after calling another(): " + str(count))
