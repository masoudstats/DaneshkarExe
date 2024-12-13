import numpy as np
from random import randint

def find_min(list_num: list) -> list:
    '''
    This function returns list of mins and their indexes from list numbers.
    list_num: list of numbers
    Returns: list of min values 
    '''
    arr_nums = np.array(list_num)

    idx_mins = list(np.where(arr_nums == np.min(arr_nums))[0])
    val_mins = list(arr_nums[arr_nums == np.min(arr_nums)])

    return val_mins, idx_mins


########################################################################################
########################################################################################

def find_max(list_num: list) -> list:
    '''
    This function returns list of max and their indexes from list numbers.

    list_num: list of numbers
    Returns: list of max values 
    '''
    arr_nums = np.array(list_num)

    idx_maxs = list(np.where(arr_nums == np.max(arr_nums))[0])
    val_maxs = list(arr_nums[arr_nums == np.max(arr_nums)])

    return val_maxs, idx_maxs


########################################################################################
########################################################################################

def concat_lists(val1: list, val2: list) -> list:
    '''
    Concatinate of two lists.

    val1: list 
    val2: list
    Returns: list of concatenated two list 
    '''

    conc = val2 + val1

    return conc


########################################################################################
########################################################################################

def sort_list(val: list) -> list:
    '''
    Sort of list in ascending form.

    val: list 
    Returns: sorted list 
    '''

    sorted_nums = []
    while len(val) :
        _, idx = find_min(val)
        sorted_nums.append(val.pop(idx[0]))
  
    return sorted_nums
    


########################################################################################
########################################################################################

def find_intersection(val1: list, val2: list) -> list:
    """
    This func return intersection of two lists.

    val1: list
    val2: list

    Returns: new list
    """
    
    list_intersection = []

    for num in val1:
        if num in val2: 
            list_intersection.append(num)

    return list(set(list_intersection))




########################################################################################
########################################################################################

def find_union(val1: list, val2: list) -> list:
    """
    This func returns union of two lists.

    val1: list
    val2: list
    Returns: new list
    """
    
    len_val1 = len(val1)
    len_val2 = len(val2)
    list_union = []

    if len_val1 < len_val2:
        for num in val1:
            if num not in val2: 
                list_union.append(num)

        total_list = concat_lists(list_union, val2)
    else:
        for num in val2:
            if num not in val1: 
                list_union.append(num)        
        total_list = concat_lists(list_union, val1)

    return list(set(total_list))





if __name__ == '__main__':

    n, m = input('Input two numbers:').split()

    list_num1, list_num2 = [], []
    for i in range(int(n)):
        list_num1.append(randint(0, int(m)))
        list_num2.append(randint(0, int(m)))

    print(list_num1, list_num2)

    # Find union and sort them
    union = find_union(list_num1, list_num2)
    sorted_union = sort_list(union)
    print(sorted_union)


    # Find intersection and sort them
    intersection = find_intersection(list_num1, list_num2)
    sorted_intersection = sort_list(intersection)
    print(sorted_intersection)


    # Concat and sort them
    concatination = concat_lists(list_num1, list_num2)
    sorted_concatination = sort_list(concatination)
    print(sorted_concatination)    


    # Find min of two lists
    min1, _ = find_min(list_num1)
    min1 = list(set(min1))[0]

    min2, _ = find_min(list_num2)
    min2 = list(set(min2))[0]

    if min1 ==  min2:
        print("Mins of two lists are equale to:", min1) 


    # Find max of two lists
    max1, _ = find_max(list_num1)
    max1 = list(set(max1))[0]

    max2, _ = find_max(list_num2)
    max2 = list(set(max2))[0]

    if max1 ==  max2:
        print("Mins of two lists are equale to:", max1) 


    # Remove min value from lists
    min1, _ = find_min(list_num1)
    min2, _ = find_min(list_num2)

    for val in min1:
        list_num1.remove(val)

    for val in min2:
        list_num2.remove(val)
    
    print("Removed min(s) from list1:", list_num1)
    print("Removed min(s) from list2:", list_num2)



    # Remove max value from lists
    max1, _ = find_max(list_num1)
    max2, _ = find_max(list_num2)

    for val in max1:
        list_num1.remove(val)

    for val in max2:
        list_num2.remove(val)
    
    print("\nRemoved max(s) from list1:", list_num1)
    print("Removed max(s) from list2:", list_num2)
