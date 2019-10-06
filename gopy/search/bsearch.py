"""Binary Search Implementation
Takes in an item & array & returns the index of match
"""
def search(item,array):
    beg = 0
    end = len(array)
    while(end >= beg):
        mid = beg + ((end - beg)//2)
        # if mid goes out of bound report element not present
        if mid >= len(array):
            break
        if array[mid] > item:
            end = mid - 1
        elif array[mid] < item:
            beg = mid + 1
        else:
            return mid
    return "Not Found"