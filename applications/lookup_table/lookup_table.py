# Your code here

import random


def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v


expo = {}
fact = {}


def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    # calculate x^y
    # calculate factorial of x^y
    # have multiple objects to hold previously used values
    # check if full factorial is in fact object yet
    # if not then loop through but check each factorial on the way
    fact = 1
    v = x ** y
    if f"{v}" in expo:
        fact = expo[f"{v}"]
    else:
        for i in range(1, v + 1):
            key = str((i))
            fact = fact * i
            # print(fact)
            if key not in expo:
                expo[key] = fact
            # print(key, expo[key])


# Do not modify below this line!
for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')

# slowfun(2, 5)
