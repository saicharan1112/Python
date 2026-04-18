import re
s = input("Enter a string: ")
pattern = r'^[a-z]$|^([a-z]).*\1$'
"""
^[a-z]$ → matches a single lowercase letter (start and end are same automatically)
^([a-z]).*\1$ →
([a-z]) → captures first lowercase letter
.* → any characters in between
\1 → same character at the end
"""
if re.match(pattern, s):
    print("String starts and ends with the same character.")
else:
    print("String does NOT start and end with the same character.")
