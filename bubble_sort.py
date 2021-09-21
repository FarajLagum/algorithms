def swap(array, a, b):
    temp = array[a]
    array[a] = array[b]
    array[b] = temp


def swap2(array, a, b):
    array[a], array[b] = array[b], array[a]
    #return array

def swap3(list, pos1, pos2):
     
    # popping both the elements from list
    first_ele = list.pop(pos1)  
    second_ele = list.pop(pos2-1)
    
    # inserting in each others positions
    list.insert(pos1, second_ele) 
    list.insert(pos2, first_ele) 


# test swap function
array = [0, 1, 2, 3]
swap3(array, 0, 3)
print(array)


def buuble_sort(array):
    """ burt force implementation"""
    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1): # the used len(array) - i - 1 because the last element is the bigest number after the first iteration
            if array[j] > array [j+1]:
                swap(array, j, j+1)
    
    return array


# test buuble sort

array = [8, 3, 6, 0, -10, 2, -2]


print(buuble_sort(array))