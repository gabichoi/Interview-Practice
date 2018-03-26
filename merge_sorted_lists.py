# Given two sorted lists, it returns a new merged list
def merge(lst1, lst2):
    
    """
    >>> merge([1, 3, 5], [2, 4, 6])
    [1, 2, 3, 4, 5, 6]
    >>> merge([], [2, 4, 6])
    [2, 4, 6]
    >>> merge([1, 2, 3], [])
    [1, 2, 3]
    >>> merge([5, 7], [2, 4, 6])
    [2, 4, 5, 6, 7]

    """
    new_list = []
    if list_1 == []:
        return list_2
    elif list_2 == []:
        return list_1
    else:
        while list_1 and list_2: 
            if list_1[0] <= list_2[0]:
                new_list.append (lst_1[0])
                list_1 = list_1 [1:]
                if list_1 == []:
                    new_list = new_list + list_2
            else:
                new_list.append (list_2[0])
                list_2 = list_2 [1:]
                if list_2 == []: 
                    new_lst = new_lst + list_1
        return new_lst

            
