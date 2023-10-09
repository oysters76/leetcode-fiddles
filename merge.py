def merge_list(list1, list2):
    i, j = 0, 0 
    merged = [] 
    while (i < len(list1) or j < len(list2)):
        
        if (i >= len(list1)):
            merged.append(list2[j]) 
            j += 1 
            continue 
        if (j >= len(list2)):
            merged.append(list1[i])
            i += 1 
            continue 

        v1, v2 = list1[i], list2[j] 
        
        if (v1 <= v2):
            merged.append(v1) 
            i += 1 
        elif (v1 > v2):
            merged.append(v2) 
            j += 1


    return merged 


assert merge_list([1,3,4], [1,2,4]) == [1,1,2,3,4,4]
assert merge_list([],[]) == [] 
assert merge_list([],[0]) == [0] 
