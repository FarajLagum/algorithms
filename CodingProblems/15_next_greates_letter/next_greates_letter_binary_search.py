def next_greatest_letter(letters, target):
    left, right = 0, len(letters)
    while left < right:
        mid = left + (right - left) // 2
        if letters[mid] <= target:
            left = mid + 1
        else:
            right = mid

    # return letters[left % len(letters)] # elegant way to replace the code below. either consider index left or 0
    if left == len(letters):
        return letters[0]
    else:
        return letters[left]
    
    


print(next_greatest_letter(["c","f","j"], "a"))  # Output: "c"
print(next_greatest_letter(["c","f","j"], "c"))  # Output: "f"
print(next_greatest_letter(["x","x","y","y"], "z"))  # Output: "x"
