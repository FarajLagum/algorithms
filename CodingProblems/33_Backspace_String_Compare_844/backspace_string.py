
def build_string(st: str) -> str:
    stack = []
    for char in st:
        if char != '#':
            stack.append(char)
        elif stack:
            stack.pop()
    return ''.join(stack)

import re

def remove_hash(s: str) -> str:
    return re.sub('.?#', '', s)

s1 = 'ab#c'
s2 = 'ad#c'

print(remove_hash(s1))  # Output: ac
print(remove_hash(s2))  # Output: ac


def backspace_compare(s: str, t: str) -> bool:
    return build_string(s) == build_string(t)

# Test Case Examples
print(backspace_compare("ab#c", "ad#c"))  # Output: True
print(backspace_compare("ab##", "c#d#"))  # Output: True
print(backspace_compare("a#c", "b"))      # Output: False
