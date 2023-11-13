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

