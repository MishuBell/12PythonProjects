
adj = input("Enter an adj: ")

def print_madlibs():
    user_input = input("Enter a name: ")
    print("subscribe to " + user_input)
    print("Subscribe to {}".format(user_input))
    print(f"subscribe to {user_input}")


def print_madlibs_2():
    madlib = f"Computer programming so so {adj}"
    print(madlib)


print_madlibs()
print_madlibs_2()