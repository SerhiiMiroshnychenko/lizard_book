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

import os

_, filename = os.path.split('/home/luciano/.ssh/id_rsa.pub')
print(filename)  # 'id_rsa.pub'

################################
# Using * to grab excess items #
################################

a, b, *rest = range(5)
print(a, b, rest)  # (0, 1, [2, 3, 4])

a, b, *rest = range(3)
print(a, b, rest)  # (0, 1, [2])

a, b, *rest = range(2)
print(a, b, rest)  # (0, 1, [])

a, *body, c, d = range(5)
print(a, body, c, d)  # (0, [1, 2], 3, 4)

*head, b, c, d = range(5)
print(head, b, c, d)  # ([0, 1], 2, 3, 4)

############################################################
# Unpacking with * in function calls and sequence literals #
############################################################

def fun(a, b, c, d, *rest):
    return a, b, c, d, rest


print(fun(*[1, 2], 3, *range(4, 7)))  # (1, 2, 3, 4, (5, 6))

print(*range(4), 4)  # (0, 1, 2, 3, 4)

print([*range(4), 4])  # [0, 1, 2, 3, 4]

print({*range(4), 4, *(5, 6, 7)})  # {0, 1, 2, 3, 4, 5, 6, 7}

####################
# Nested unpacking #
####################

"""
Example 2-8. Unpacking nested tuples to access the longitude
"""

"""
metro_lat_lon.py

Demonstration of nested tuple unpacking::

    >>> main()
                    |  latitude | longitude
    Mexico City     |   19.4333 |  -99.1333
    New York-Newark |   40.8086 |  -74.0204
    São Paulo       |  -23.5478 |  -46.6358

"""

"""
# tag::MAIN[]
metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),  # <1>
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('São Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

def main():
    print(f'{"":15} | {"latitude":>9} | {"longitude":>9}')
    for name, _, _, (lat, lon) in metro_areas:  # <2>
        if lon <= 0:  # <3>
            print(f'{name:15} | {lat:9.4f} | {lon:9.4f}')

if __name__ == '__main__':
    main()
# end::MAIN[]
"""

###################################
# Pattern Matching with Sequences #
###################################
