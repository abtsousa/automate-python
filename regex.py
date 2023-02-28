import re

message = 'My number is 415-555-1011, or call 415-555-1012'
phoneNumRegex = re.compile(r'(\d{3})-(\d{3}-\d{4})')
mo = phoneNumRegex.search(message)

print(mo.group())
print(mo.groups())
print(mo.group(1))
print(mo.group(2))