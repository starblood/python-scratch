'''
Created on 2013. 3. 21.

@author: starblood
'''

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
    
    leftList = []
    rightList = []
    

    mid = len(list) / 2
    
    leftList = list[:mid]
    rightList = list[mid:]
    
    leftList = merge_sort(leftList)
    rightList = merge_sort(rightList)
    
    return merge(leftList, rightList)

''' Test code for sorting algorithm '''
list = [101, 5, -1, 20, 13, 11]
print list

newList = merge_sort(list)
print newList
