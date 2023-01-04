"""
-> Binary Search Algorithm
    Binary Search is applied on the sorted array or list of large size.
    The limitation is that the array or list of elements must be sorted for the binary search algorithm to work on it.
-> Implementing Binary Search Algorithm
    1. Find the middle element and start with the middle element:
        a. If the target value is equal to the middle element of the array, then return the index of the middle element.
    2. If not, then compare the middle element with the target value,
        a. If the target value is greater than the number in the middle index, then pick the elements to the
           right of the middle index, and start with Step 1.
        b. If the target value is less than the number in the middle index, then pick the elements to the left of the
           middle index, and start with Step 1.
    3. When a match is found, return the index of the element matched.
    4. If no match is found, then return -1
-> Time complexity - O(log n)
*** This binary search is modified. This binary search is modified in a way to handle ascending and descending,
    both kind of sorted array without any change required.
"""


def binary_search_with_loop(target, num_array):
    first, last = 0, len(num_array)-1
    is_asc = num_array[first] < num_array[last]
    while first<=last:
        # finding middle element this way to make sure not to cross the range of integer
        middle = first + ((last-first)//2)
        if target == num_array[middle]:
            return middle
        elif target<num_array[middle]:
            if is_asc:
                last = middle-1
            else:
                first = middle+1
        else:
            if is_asc:
                first = middle+1
            else:
                last = middle-1
    return -1


ascending_num_array = [1, 3, 4, 5, 6, 8, 9, 15, 28, 31, 39, 45, 49]
print('ascending binary search - ', binary_search_with_loop(50, ascending_num_array))
descending_num_array = [49, 45, 39, 31, 28, 15, 9, 8, 6, 5, 4, 3, 1]
print('descending binary search - ', binary_search_with_loop(31, descending_num_array))
