def get_next_char(st: str, index: int) -> int:
    skip = 0
    while index >= 0:
        if st[index] == '#':
            skip += 1
        elif skip > 0:
            skip -= 1
        else:
            return index
        index -= 1
    return -1


def backspaceCompare(s: str, t: str) -> bool:
    i = len(s) - 1
    j = len(t) - 1
    while i >= 0 or j >= 0:
        i = get_next_char(s, i)
        j = get_next_char(t, j)
        if i < 0 and j < 0:
            return True
        elif i < 0 or j < 0:
            return False
        elif s[i] != t[j]:
            return False
        i -= 1
        j -= 1
    return True

# Test Case Examples
print(backspaceCompare("ab#c", "ad#c"))  # Output: True
print(backspaceCompare("ab##", "c#d#"))  # Output: True
print(backspaceCompare("a#c", "b"))      # Output: False
