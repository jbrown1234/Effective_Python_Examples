fresh_fruit = {
    'apple': 10,
    'banana': 8,
    'lemon': 5,
}


def make_lemonade(count):
    print("squeeze, squeeze")
    print("add water")
    print("add sugar")
    return


def out_of_stock():
    print("Out of stock")
    return


count = fresh_fruit.get('lemon')  # note that the book is showing the syntax for the getter function as
                                  # ...get('lemon', 0), yet this form yields the same outcome, omitting
                                  # the default 0 value
if count:
    make_lemonade(count)
else:
    out_of_stock()

# Introduction of the walrus operator!!!
if count := fresh_fruit.get('lemon'): # offers variable assignment and
    make_lemonade(count)
else:
    out_of_stock()

def make_cider(count):
    print("grind, grind, grind")
    print("pressssssssss")

count = fresh_fruit.get('apples', 0)
if count >=4:
    make_cider()
else:
    out_of_stock()

if (count := fresh_fruit.get('apple', 0)) >= 4:
    make_cider(count)
else:
    out_of_stock()

import random


def slice_bananas():
    print("slice a bunch")
    # return a random number between 1 & 20
    return random.randrange(1, 21)


class OutOfBananas(Exception):
    pass


def make_smoothies(count):
    print("make the smoothie")
    # each smoothie requires 10 slices to make
    return

pieces = 0
count = fresh_fruit.get('banana', 0)
if count >= 2:
    pieces = slice_bananas()

try:
    smoothies = make_smoothies(pieces)
except OutOfBananas:
    out_of_stock()

# alternative to this
pieces = 0
if (count := fresh_fruit.get('banana', 0)) >= 2:
    pieces = slice_bananas()

try:
    smoothies = make_smoothies(pieces)
except OutOfBananas:
    out_of_stock()

# another alternative to this
if (count := fresh_fruit.get('banana', 0)) >= 2:
    pieces = slice_bananas()
else:
    pieces = 0

try:
    smoothies = make_smoothies(pieces)
except OutOfBananas:
    out_of_stock()


# old-school workaround to a switch/case statement
count = fresh_fruit.get('banana', 0)
if count >= 2:
    pieces = slice_bananas()
    to_enjoy = make_smoothies(pieces)
else:
    count = fresh_fruit.get('apple', 0)
    if count >= 4:
        to_enjoy = make_cider()
    else:
        count = fresh_fruit.get('lemon', 0)
        if count:
            to_enjoy = make_lemonade(count)
        else:
            to_enjoy = 'Nothing'

# reenvision this as.....
if (count := fresh_fruit.get('banana,', 0)) >= 2:
    pieces = slice_bananas()
    to_enjoy = make_smoothies(pieces)
elif (count := fresh_fruit.get('apple', 0)) >= 4:
    to_enjoy = make_cider()
elif (count := fresh_fruit.get('lemon', 0)) >= 0:
    to_enjoy = make_lemonade(count)
else:
    to_enjoy = 'Nothing'

# old-school workaround to getting a do/while
def pick_fruit():
    print("picking fruit")
    return

def make_juice(fruit, count):
    print("make some juice")
    return

bottles = []
fresh_fruit = pick_fruit()
while fresh_fruit:
    for fruit, count in fresh_fruit.items():
        batch = make_juice(fruit, count)
        bottles.extend(batch)
    fresh_fruit = pick_fruit()

# let's reenvision the loop....
bottles = []
while True:
    fresh_fruit = pick_fruit()
    if not fresh_fruit:
        break
    for fruit, count in fresh_fruit.items():
        batch = make_juice(fruit, count)
        bottles.extend(batch)

# simplify with the walrus
bottles = []
while fresh_fruit := pick_fruit()
    for fruit, count in fresh_fruit.items():
        batch = make_juice(fruit, count)
        bottles.extend(batch)