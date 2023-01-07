"""
-> Jump Search Algorithm
    Jump Search Algorithm is a relatively new algorithm for searching an element in a sorted array.
    The fundamental idea behind this searching technique is to search fewer number of elements compared to linear search
    algorithm (which scans every element in the array to check if it matches with the element being searched or not).
    This can be done by skipping some fixed number of array elements or jumping ahead by fixed number of steps in every
    iteration. The limitation is that list should be sorted.
-> Time complexity - O(√n)
-> Space complexity - O(1)
"""

import math


def jump_search(target, num_array):
    block_size = int(math.sqrt(len(num_array)))
    end, first, list_size = block_size, 0, len(num_array)
    while first <= end <= list_size:
        if num_array[end] == target:
            return end
        elif num_array[end] > target:
            for i in range(first, end):
                if num_array[i] == target:
                    return i
        else:
            first = end+1
            end = end + block_size if end+block_size < list_size else list_size-1
    return -1


num_array = [2, 3, 5, 6, 9, 11, 13, 15, 19, 24, 26, 28, 29, 35]
print(jump_search(35, num_array))
