def count_down(n):
    """ Count down from a number  """
    
    if n > -1:
        print(n)
    else:
        return 
    return count_down(n-1)


count_down(3)


def count_down2(start):
    """ Count down from a number  """
    print(start)

    # call the count_down if the next
    # number is greater than 0
    next = start - 1
    if next > 0:
        count_down(next)


#count_down2(3)
