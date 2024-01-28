
# iterates through the string t and checks if each character in s is present in t 
# in the same order. If all characters in s are found in t, the function returns True. 
# Otherwise, it returns False.
def is_subsequence(s: str, t: str) -> bool:
    i = 0 # slow pointer
    for j in range(len(t)): # j is a fast pointer
        if i == len(s):
            return True
        if s[i] == t[j]:
            i += 1
    return i == len(s) # if we iterated over all elements of t without finishing all elements of s

s = "abc" 
t = "ahbgdc" 
print(is_subsequence(s, t)) # Output: True
