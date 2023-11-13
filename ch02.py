"""
Example 2-1. Build a list of Unicode codepoints from a string, using a listcomp
"""


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
