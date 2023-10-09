import math 

def get_index(arr, target):
    l = 0; 
    h = len(arr)-1 
    m = -1 
    while (l <= h):
        m = int(((l+h)/2))
        val = arr[m] 
        if (val == target):
            return m 
        if (target > val):
            l = m+1  
        else:
            h = m-1
    return l



arr = [1,2,3,4,5,6,7,8,9,10,15] 
assert get_index(arr, 1) == 0 
assert get_index(arr, 2) == 1 
assert get_index(arr, 3) == 2 
assert get_index(arr, 4) == 3 
assert get_index(arr, 5) == 4 
assert get_index(arr, 6) == 5 
assert get_index(arr, 7) == 6 
assert get_index(arr, 8) == 7
assert get_index(arr, 9) == 8

arr = [1,3,5,6]
assert get_index(arr,5) == 2
assert get_index(arr,2) == 1 
assert get_index(arr,7) == 4


