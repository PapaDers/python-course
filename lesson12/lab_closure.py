# Closure is a function having access to the scope of its parent function after the parent function has returned.


def parent_function(person, coins=3):
    # coins = 3

    def play_game():
        nonlocal coins
        coins -= 1

        if coins > 1:
            print("\n" + person + " has " + str(coins) + " coins left.")
        elif coins == 1:
            print("\n" + person + " only has " + str(coins) + " coin left.")
        else:
            print("\n" + person + " is out of coins.")

    # return the function 'play_game()' to the variable 'tommy' and 'jenny'
    # this is called a closure because the function 'play_game()' has access to the scope of its parent function 'parent_function()' and the variables inside it like 'coins'.
    # this allows the tracking of values only needed by the function 'play_game()' limited to the scope of 'parent_function()' rather than cluttering the global scope.
    return play_game


# "tommy" and "jenny" are variables that are assigned the return of function 'parent_function()'
# The return of 'parent_function()' is the function 'play_game()'
# this allows us to call 'tommy()' and 'jenny()' as functions since they are assigned the return of 'parent_function()' which is 'play_game()'
tommy = parent_function("Tommy", 14)
jenny = parent_function("Jenny", 6)

tommy()
tommy()

jenny()

tommy()
