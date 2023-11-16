"""
Example 2-1. Build a list of Unicode codepoints from a string, using a listcomp
"""



import itertools
symbols = '$¢£¥€¤'
codes = [ord(symbol) for symbol in symbols]
print(f'{codes=}')

x = 'ABC'
codes = [ord(x) for x in x]
print(f'{x = }')
print(f'{codes = }')

codes = [last := ord(c) for c in x]
print(f'{last = }')

"""
Example 2-3. The same list built by a listcomp and a map/filter composition
"""

symbols = '$¢£¥€¤'
beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
print(f'{beyond_ascii = }')

beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
print(f'{beyond_ascii = }')

"""
Example 2-4. Cartesian product using a list comprehension
"""

colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]
print(f'{tshirts = }')

# for color in colors:
#     for size in sizes:
#         print((color, size))
for color, size in itertools.product(colors, sizes):
    print((color, size))

tshirts = [(color, size) for size in sizes for color in colors]
print(f'{tshirts = }')

"""
Example 2-5. Initializing a tuple and an array from a generator expression
"""

symbols = '$¢£¥€¤'
print(tuple(ord(symbol) for symbol in symbols))

import array

print(array.array('I', (ord(symbol) for symbol in symbols)))

"""
Example 2-6. Cartesian product in a generator expression
"""

colors = ['black', 'white']
sizes = ['S', 'M', 'L']

for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
    print(tshirt)
    
#######################################
# Tuples Are Not Just Immutable Lists #
#######################################

"""
Example 2-7. Tuples used as records
"""
lax_coordinates = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32_450, 0.66, 8014)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]

for passport in sorted(traveler_ids):
    print('%s/%s' % passport)

# BRA/CE342567
# ESP/XDA205856
# USA/31195855

for country, _ in traveler_ids:
    print(country)

# USA
# BRA
# ESP

#############################
# Tuples as Immutable Lists #
#############################

"""
Tuples as Immutable Lists
"""

a = (10, 'alpha', [1, 2])
b = (10, 'alpha', [1, 2])
print(a == b)  # True

b[-1].append(99)
print(a == b)  # False

print(b)  # (10, 'alpha', [1, 2, 99])

def fixed(o):
    try:
        hash(o)
    except TypeError:
        return False
    return True


tf = (10, 'alpha', (1, 2))  # Contains no mutable items
tm = (10, 'alpha', [1, 2])  # Contains a mutable item (list)
print(fixed(tf))  # True
print(fixed(tm))  # False

#####################################
# Unpacking sequences and iterables #
#####################################

lax_coordinates = (33.9425, -118.408056)
latitude, longitude = lax_coordinates  # unpacking
print(latitude)  # 33.9425

print(longitude)  # -118.408056

print(divmod(20, 8))  # (2, 4)

t = (20, 8)
print(divmod(*t))  # (2, 4)

quotient, remainder = divmod(*t)
print(quotient, remainder)  # (2, 4)
