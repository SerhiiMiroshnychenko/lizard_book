"""
Example 2-1. Build a list of Unicode codepoints from a string
"""


symbols = '$¢£¥€¤'
codes = [ord(symbol) for symbol in symbols]
print(f'{codes=}')
