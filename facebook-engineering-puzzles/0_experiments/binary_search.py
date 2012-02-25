def binary_search(l, t):
    """
    Returns the index at which an element exists.
    Else returns none
    
    l = list you are searching
    t = target element
    """
    low = 0
    high = len(l)-1
    
    while low < high:
        mid = (low+high)/2
        if l[mid] < t:
            low = mid + 1
        elif t < l[mid]:
            high = mid 
        else:
            return mid                
    return None