names = ['Cecilia', 'Lise', 'Marie']
counts = [len(n) for n in names]    # Love this example for populating a new list
print(counts)

longest_name = None
max_count = 0

for i in range(len(names)):     # depending on i can lend itself to messy code
    count = counts[i]
    if count > max_count:
        max_count = count
        longest_name = names[i]
print(f"Longest name is {longest_name} of {max_count} characters")

for i, name in enumerate(names):    # enumerate helps, but not by much
    count = counts[i]
    if max_count < count:
        max_count = count
        longest_name = name
print(f"Longest name is {longest_name} of {max_count} characters")

for count, name in zip(counts, names): # zip keeps the related lists in lock-step and cleans up usage
    if max_count < count:
        max_count = count
        longest_name = name
print(f"Longest name is {longest_name} of {max_count} characters")

# Beware zip performance when lists are not kept in sync
names.append('Rosalind')
for name, count in zip(names, counts):
    print(name)     # zip stop operating per the lenght of the shortest list, so some data could come up missing

import itertools

for name, count in itertools.zip_longest(names, counts):    # zip_longest compensates for this, but doesn't correct
    print(f"{name} {count}")                                # for the mistake of missing data