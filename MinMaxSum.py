def minMaxSum(array):
    """ Finds the minimum and maximum value when adding 4 out of 5 items in the array
    Args:
        array (string): the array written as 5 numbers separated by spaces

    Returns:
        The minimum and maximum values separated by a space
    """
    array = array.split()
    whole = 0
    for number in array:
        whole += int(number)
    array.sort()
    mini = whole - int(array[4])
    maxi = whole - int(array[0])

    print("%s %s" % (mini, maxi))
