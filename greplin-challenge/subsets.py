import itertools

def get_all_subsets(_list, min_subset_size = 3):
    """
    Given a list, returns all subsets of that list as a list of lists
    """
    subsets = []
    for i in range(min_subset_size, len(_list)+1):
        subsets.append(itertools.combinations(_list, i))
        
    return_list = []
    for subset in subsets:
        for _tuple in subset:
            return_list.append(list(_tuple))
    return return_list

def max_element_equals_sum_of_other_elements(_list):
    """
    Given a sorted list, say: [1, 2, 3], we remove the max element: 3
    The remaining list becomes [1, 2]
    The sum of the remaining list = 3. So does the max element.
    Therfore, we return True.
    """
    target = _list.pop()
    if target == sum(_list):
        print str(_list) + " = " + str(target)
        return True
    return False
    

if __name__ == "__main__":
    print "I will find all subsets of this list, and run a calculation on it:"
    l = [3, 4, 9, 14, 15, 19, 28, 37, 47, 50, 54, 56, 59, 61, 70, 73, 78, 81, 92, 95, 97, 99]
    print l
    subsets = get_all_subsets(l)
    sum_matches = 0
    for subset in subsets:
        if max_element_equals_sum_of_other_elements(subset):
            sum_matches += 1
    print "The number of subsets where the other elements add up to the max element is: " + str(sum_matches)