input_string = "kayak"


def is_palindrome(input_string):
    length = len(input_string)
    if length < 2:
        return True
    if input_string[0] == input_string[length-1]:
        return is_palindrome(input_string[1:length-1])
    
    return False

print(is_palindrome(input_string))



def is_palindrome_iteritive(input_string):
    left = 0
    right = len(input_string) - 1
    
    while left < right:
        if input_string[left] != input_string[right]:
            return False
        left += 1
        right -= 1
        
    return True

input_string = "kayak"
result = is_palindrome_iteritive(input_string)
print(result)


def is_palindrome_recursive_2(input_string, left, right):
    if left >= right:
        return True
    if input_string[left] != input_string[right]:
        return False
    return is_palindrome_recursive_2(input_string, left + 1, right - 1)

input_string = "kayak"
result = is_palindrome_recursive_2(input_string, 0, len(input_string) - 1)
print(result)

