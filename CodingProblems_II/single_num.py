from collections import defaultdict

def single_number(nums):


    num_dict = defaultdict(int)
    for num in nums:
            num_dict[num] += 1

    
    for num in num_dict:
          if num_dict[num] == 1:
                return num
    
    return None


nums = [4,1,2,1,2]

print(single_number(nums))



# def find_key_by_value(dictionary, value):
#     for key, val in dictionary.items():
#         if val == value:
#             return key
#     return None  # Return None if value not found

# # Example usage:
# my_dict = {'a': 1, 'b': 2, 'c': 3}
# search_value = 2
# result = find_key_by_value(my_dict, search_value)
# print(f"Key for value {search_value} is: {result}")



# v = nums.index(4)

# print(v)

# def find_key_by_value(dictionary, value):
#     return list(dictionary.keys())[list(dictionary.values()).index(value)]

# # Example usage:
# my_dict = {'a': 1, 'b': 2, 'c': 3}
# search_value = 1
# result = find_key_by_value(my_dict, search_value)
# print(f"Key for value {search_value} is: {result}")
