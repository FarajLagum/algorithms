def next_greatest_letter(letters, target):
    for letter in letters:
        if letter > target:
            return letter
    return letters[0]


print(next_greatest_letter(["c","f","j"], "a"))  # Output: "c"
print(next_greatest_letter(["c","f","j"], "c"))  # Output: "f"
print(next_greatest_letter(["x","x","y","y"], "z"))  # Output: "x"
