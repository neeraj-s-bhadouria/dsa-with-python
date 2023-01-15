"""
-> Selection Sort Algorithm
    Selection sort is conceptually the most simplest sorting algorithm. This algorithm will first find the smallest
    element in the array and swap it with the element in the first position, then it will find the second smallest
    element and swap it with the element in the second position, and it will keep on doing this until the entire array
    is sorted. It is called selection sort because it repeatedly selects the next-smallest element and swaps it
    into the right place.
-> Implementation of selection sort
    1. Starting from the first element, we search the smallest element in the array, and replace it with the element
        in the first position.
    2. We then move on to the second position, and look for smallest element present in the subarray, starting from
        index 1, till the last index.
    3. We replace the element at the second position in the original array, or we can say at the first position in the
        subarray, with the second smallest element.
    4. This is repeated, until the array is completely sorted.
-> Time complexity - O(n2)
-> Space complexity - O(1)
"""


def selection_sort(num_array):
    is_sorted = True
    for i in range(len(num_array)-1):
        min_index = i
        min_value = num_array[min_index]
        for j in range(min_index+1, len(num_array)):
            if num_array[j] < min_value:
                min_index = j
                min_value = num_array[min_index]
                is_sorted = False
        if is_sorted:
            return num_array
        num_array[min_index], num_array[i] = num_array[i], num_array[min_index]
    return num_array


num_array = [41, 27, 68, 11, 3, 45, 60, 17, 44, 35, 23, 23, 47]
print(selection_sort(num_array))
