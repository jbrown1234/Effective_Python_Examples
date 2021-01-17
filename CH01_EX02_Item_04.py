# Prefer interpolated F-style over C-style format strings
# This is the example # 2 no-no, indicating that the c-style setup can make things difficult to read
pantry = [
    ('avacados', 1.25),
    ('bananas', 2.5),
    ('cherries', 15.0)
]

for i, (item, price) in enumerate(pantry): # important here is that we get to see enumerate() in action, too
    print("#%d: %-10s = %.2f" % (i, item, price))

print("")
# add some tweaks to pretty up presentation.....
for i, (item, price) in enumerate(pantry):
    print("#%d: %-10s = %.2f" % (i, item.title(), round(price))) # the book notes that this statement wouldn't fit
                                                                 # on one line, but, look how we have room for comments
print("")

# This is the example # 3 for c-style string formatting - having to repeat variables if you want to use them
# multiple times in the same string
template = "%s loves food. See %s cook"
name = "Max"
formatted = template % (name, name)  # see the repeat? How would we simplify this? Maybe not necessarily simplify, but
                                     # help guard against re-use or wrong use issues.
print(formatted)
# this time we establish a template string that leverages keywords
template = "%(name)s loves food. See %(name)s cook"
after = template % {'name': name}  # each time "name" is encountered it will be replaced by the name variable
                                   # helping to ensure no rogue substitutions happen
print(after)
print("\n")

# Oh, the great things about Python 3....
# who doesn't love the format() function?
a = 1234.5678
formatted = format(a, ",.2f")    # note how the ',' character is used to modify the numerical string
print(formatted)

b = 'my string'
formatted = format(b, "^20s")   # the carat character is used to center the string in the padded space provided
print("*", formatted, "*")

key = "my_var"
value = 1.234
formatted = "{} = {}".format(key, value)
print(formatted)

# or....
formatted = "{:<10} = {:.2f}".format(key, value) # check out the left-justified padding
print(formatted)
print("")
# also, placing a numeric value within the formatted brace permits easy value replication within a string
formatted = "{0} loves food. See {0} eat".format(name, "Dirk")
print(formatted)
# ...or...
formatted = "{1} loves food. See {1} eat".format(name, "Dirk")
print(formatted)
print("")

# some advanced formatting sass....
menu = {
    'soup': "lentil",
    'oyster': "kuamato",
    'special': "schnitzel",
}
print("First letter is {menu[oyster][0]!r}".format(menu=menu)) # notice how we're picking off the first letter in the
                                                               # 'oyster' string per the index specifier and effectively
                                                               # coercing the value to Unicode with !r which is the
                                                               # same as repr. Try with/without !r to see the difference

# BUT THE TEXT GOES ON TO NOTE THAT format() STYLE IS OLD-SCHOOL.... OH, THAT HURTS!
# So what could be better?