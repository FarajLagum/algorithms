def create_frequency_dict(data):
    """
    Calculate the frequency of each item in the given data.

    Parameters:
    - data: List or array-like object containing the data.

    Returns:
    - frequency_dict: Dictionary containing item frequencies.
    """
    frequency_dict = {}

    for item in data:
        if item in frequency_dict:
            frequency_dict[item] += 1
        else:
            frequency_dict[item] = 1

    return frequency_dict


def get_item_with_highest_frequency(frequency_dict):
    """
    Get the item with the highest frequency from the frequency dictionary.

    Parameters:
    - frequency_dict: Dictionary containing item frequencies.

    Returns:
    - item_with_highest_frequency: Item with the highest frequency.
    """

    # item_with_highest_frequency = max(
    #     frequency_dict, key=frequency_dict.get, default=None)
    item_with_highest_frequency = max(list(frequency_dict.keys()))

    return item_with_highest_frequency


if __name__ == "__main__":

    data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
    # data = [1, 4, 1, 4, 2, 1, 3, 5, 6]
    frequency_result = create_frequency_dict(data)
    print(frequency_result)

    print(max(list(frequency_result.keys())))

    highest_frequency_item = get_item_with_highest_frequency(frequency_result)
    print(highest_frequency_item)
