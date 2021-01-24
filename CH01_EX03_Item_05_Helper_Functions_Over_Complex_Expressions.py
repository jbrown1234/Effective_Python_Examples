# My first question for this item was, "what exactly is pithy syntax?" This is something I've not had much
# awareness of considering that most of the time I'm coding in a bubble. It's good for me that the text is
# using "pithy" as and adjective, in terms of precise and brief. Yes, I had to look it up - "pithy" is not
# part of my regular vocabulary.

# The other thing I had/have yet to make use of are query strings from a URL. A search yield info that
# such queries are common when building web pages, something that, to date, I don't have any experience
# with. So this is a new thing.... beautiful!

def print_blank_lines(count):
    for j in range(0, count):
        print("")
        #print(f"{j}")

from urllib.parse import parse_qs
my_values = parse_qs('red=5&blue=0&green=',keep_blank_values=True)
print(repr(my_values))
print_blank_lines(1)
# Whe parse_qs() function breaks up the URL string by ampersand (&) and creates a dictionary of key/value pairs
# for the items defined around the '=' character. We can then use the get() function to pull values out per
# their keys....
print("Red: ", my_values.get('red'))
print("Blue: ", my_values.get('blue'))
print("Green: ", my_values.get('green'))
print("Opacity: ", my_values.get('opacity'))
print_blank_lines(2)
# For assigning a 0 when a value isn't available or no key exists, Because the dictionary values were churned
# out as lists, this can be convenient because the empties/non-existents evaluate to 0 or False, making things nice.
# For query string 'red=5&blue=0&green='
red = my_values.get('red', [''])[0] or 0
green = my_values.get('green', [''])[0] or 0
opacity = my_values.get('opacity', [''])[0] or 0
print(f"Red: {red!r}")
print(f"Green: {green!r}")
print(f"Opacity: {opacity!r}")
# The point the book makes is the statements for defining red, green, and opacity are difficult to comprehend
# for the basic coder. In my case this meant me since this was a bit on difficult side to consume. Both green
# and opacity evaluate to False because they don't have an assigned value nor exist, respectively. FOr the get()
# function, the second parameter defines what to return if no value exists for the key; the [0] after the
# function somewhat helps bound the returned value expactations. If this were [1] then an exception would be
# raised indicating that we are out of range. If the value were '52' were entered then we would be able to pass
# [1] but not [2]. You can play around with the code above by setting red to '52' and seeing what's returned.
print_blank_lines(1)
# Now if we want to print our returned values as integers, the statement gets a little bit more complex...
red = int(my_values.get('red', [''])[0] or 0)
print(f"Red: {red!r}")
print_blank_lines(1)
# While you could opt for using if/else statements to help clarify....
red_str = my_values.get('red', [''])
red = int(red_str[0]) if red_str[0] else 0
print(f"Red: {red!r}")
print_blank_lines(1)
# But even this may prove unwieldy, mostly because this form of if/else is less common than
green_str = my_values.get('green', [''])
if green_str[0]:
    green = int(green_str[0])
else:
    green = 0
print(f"Green: {green!r}")
print_blank_lines(1)
# Note how we might (and did) repeat the operation for different key values. It makes the
# most sense to build this into a function:
def get_first_int(values, key, default=0):
    found = values.get(key, [''])
    if found[0]:
        return int(found[0])
    return default

print(f"Opacity: {get_first_int(my_values, 'green')}")

# DRY = Don't Repeat Yourself