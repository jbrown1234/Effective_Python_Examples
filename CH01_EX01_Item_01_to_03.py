import time
import sys

import pyvisa

print(sys.version_info)
print(sys.version)
print(sys.api_version)

a = 'a\u0300 propos'
print(list(a))
print(a)


def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value    # instance of a string


print(repr(to_str(b'foo')))
print(repr(to_str('bar')))


def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
    return value


print(repr(to_bytes(b'foo')))
print(repr(to_bytes('bar')))

# comparison of byte arrays to string types is not supported
assert b'red' > b'blue' # for info on assert, see https://docs.python.org/3/reference/simple_stmts.html#the-assert-statement
assert 'red' > 'blue'
# assert b'red' > 'blue'    # will raise an error

# same goes for use with % operator...
print(b'red %s' % b'blue')
print('red %s' % 'blue')
#print(b'red %s', 'green')   # will raise an error

