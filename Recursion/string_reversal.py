
def reverse_string_recursive(string):
    if len(string) <= 1:
        return string
    else:
        return string[-1] + reverse_string_recursive(string[:-1])


# Example 
original_string = "Hello, world!"
reversed_string = reverse_string_recursive(original_string)
#print(reversed_string)






def reverse_string_iter(string):
    string_list = list(string)
    length = len(string_list)
    for i in range(length // 2):
        temp = string_list[i]
        string_list[i] = string_list[length - i - 1]
        string_list[length - i - 1] = temp
    return ''.join(string_list)

original_string = "Hello, world!"
reversed_string = reverse_string_iter(original_string)
#print(reversed_string)


def reverse_string_iter2(string):
    string_list = list(string)
    length = len(string_list)
    #print(length)
    reversed_list = []
    for i in range(length):
        # print(i)
        # print(string_list[length-i-1])
        reversed_list.append(string_list[length-i-1])
    return ''.join(reversed_list)

original_string = "Hello, world!"
reversed_string = reverse_string_iter2(original_string)
print(reversed_string)




 


def reverse_string(input_string):
    return input_string[::-1]

# Example 
original_string = "Hello, world!"
reversed_string = reverse_string(original_string)
#print(reversed_string)

