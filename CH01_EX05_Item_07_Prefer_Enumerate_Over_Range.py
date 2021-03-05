from random import randint

random_bits = 0
for i in range(32):
    if randint(0, 1):
        random_bits |= 1 << i
        print(bin(random_bits))

print(bin(random_bits))

# looping over a list...
flavor_list = ['vanilla', 'chocolate', 'pecan', 'strawberry']
for flavor in flavor_list:
    print(f"{flavor} is delicious")

# Interesting is that when I attempted to do this per memory of the example
# this is what I came up with; something closer to the simplified enumerate example
for i in range(len(flavor_list)):
    print(f"{i+1}: {flavor_list[i]}")

# However, the book wanted to show a more complicated version, like the following:
for i in range(len(flavor_list)):
    flavor = flavor_list[i]
    print(F"{1 + i}: {flavor}")

# Enumerate may have some advantages... note that the next() function provides the
# tuple output for the next item in the enumeration, so there is some inherent
# state tracking at play
it = enumerate(flavor_list)
print(next(it))
print(next(it))
print(next(it))
print(next(it))

# Really another way to iterate over lists
for i, flavor in enumerate(flavor_list):
    print(f"{i}: {flavor}")

# enumerate allows for the user to specify a start index number to be reported in
# place of the default of 0 per the second argument passed
for i, flavor in enumerate(flavor_list, 1): # here we use 1, but could make this any integer
    print(f"{i}: {flavor}")
