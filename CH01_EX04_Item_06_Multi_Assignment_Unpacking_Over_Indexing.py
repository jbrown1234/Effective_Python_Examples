def print_blank_lines(count):
    for j in range(0, count):
        print("")
        #print(f"{j}")

snack_calories = {
    'chips': 149,
    'popcorn': 80,
    'nuts': 190,
}

items = tuple(snack_calories.items())
print(items)
print_blank_lines(1)

# Simple version of unpacking....
item = ('Peanut butter', 'jelly')
first, second = item    # unpack
print(f"{first} and {second}")
print_blank_lines(1)

# Book example of a very verbose manner of doing things
favorite_snacks = {
    'salty': ('pretzels', 100),
    'sweet': ('cookies', 180),
    'veggie': ('carrots', 70),
}
((type1, (name1, cals1)),
 (type2, (name2, cals2)),
 (type3, (name3, cals3))) = favorite_snacks.items() # unpack
print(f"Favorite {type1} is {name1} with {cals1} calories.")
print(f"Favorite {type2} is {name2} with {cals2} calories.")
print(f"Favorite {type3} is {name3} with {cals3} calories.")
print_blank_lines(1)

# Classic bubble sort example
# Old school...
def bubble_sort(a):
    for _ in range(len(a)):
        for i in range(1, len(a)):
            if a[i] < a[i-1]:
                temp = a[i]
                a[i] = a[i-1]
                a[i-1] = temp
names = ['prezels', 'carrots', 'arugula', 'bacon']
bubble_sort(names)
print(names)
print_blank_lines(1)
# Using unpacking...
names = ['prezels', 'carrots', 'arugula', 'bacon']
def bubble_sort_alt(a):
    for _ in range(len(a)):
        for i in range(1, len(a)):
            if a[i] < a[i - 1]:
                a[i-1], a[i] = a[i], a[i-1]   # swap
bubble_sort_alt(names)
print(names)
print_blank_lines(1)

# the author provides us a preview of an upcoming item using enumerate()
# which does a bit of unpacking of its own
snacks = [('bacon', 350), ('donut', 240), ('muffin', 190)]
for i in range(len(snacks)):
    item = snacks[i]
    name = item[0]
    calories = item[1]
    print(f"#{i+1}: {name} has {calories} calories.")
print_blank_lines(1)

for rank, (name, calories) in enumerate(snacks, 1):
    print(f"#{rank}: {name} has {calories} calories.")
print_blank_lines(1)
