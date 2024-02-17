def search_nested_dict(dictionary, value):
    for val in dictionary.values():
        if val == value:
            return True
        if isinstance(val, dict):
            if search_nested_dict(val, value):
                return True
    return False

# Example usage:
nested_dict = {
    'a': {
        'b': {
            'c': 1,
            'd': {
                'e': 2,
                'f': None
            }
        },
        'g': [3, 4, 5]
    },
    'h': {
        'i': {
            'j': 6
        }
    }
}

search_value = None
result = search_nested_dict(nested_dict, search_value)
print(f"Value {search_value} {'exists' if result else 'does not exist'} in the nested dictionary.")



# DF
def search_nested_dict(dictionary, value):
    stack = [dictionary]
    while stack:
        current_dict = stack.pop()
        for val in current_dict.values():
            if val == value:
                return True
            elif isinstance(val, dict):
                stack.append(val)
    return False


search_value = 2
result = search_nested_dict(nested_dict, search_value)
print(f"Value {search_value} {'exists' if result else 'does not exist'} in the nested dictionary.")

