"""
Binary Search

Input: A sorted (ascending) array of integers
Output: Index of item if found, otherwise -1

"""

a = [i for i in range(10)]
b = [i for i in range(20) if i % 3 == 0]

def binary_search(l, target):
    min = 0
    max = len(l) - 1
    mid = (min + max) / 2
    if l[max] == target: return max

    while not min == mid == (max - 1):
        if target == l[mid]:
            return mid
        elif target < l[mid]:
            max = mid
        else:
            min = mid
        mid = (min + max) / 2

    return -1

if __name__ == "__main__":
   print binary_search(b, 15)
