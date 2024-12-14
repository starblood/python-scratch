"""
@author: mong
"""

def merge(left, right):
    result = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]
        elif len(left) > 0:
            result.append(left[0])
            left = left[1:]
        elif len(right) > 0:
            result.append(right[0])
            right = right[1:]
    
    return result

def merge_sort(list):
    if len(list) <= 1:
        return list
    
    mid: int = int(len(list) / 2)
    
    left_list = list[:mid]
    right_list = list[mid:]
    
    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)
    
    return merge(left_list, right_list)

''' Test code for sorting algorithm '''
sample_list = [101, 5, -1, 20, 13, 11]
print(sample_list)

newList = merge_sort(sample_list)
print(newList)
