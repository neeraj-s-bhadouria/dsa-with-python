"""
-> Insertion Sort Algorithm
    This sorting algorithm makes no sense at all but still I am implementing this because some idiots at big tech
    companies are obsessed with it.
-> Implementation of insertion sort
    1. We start by making the second element of the given array, i.e. element at index 1, the key.
    2. We compare the key element with the element(s) before it, in this case, element at index 0
        a. If the key element is less than the first element, we insert the key element before the first element.
    3. Then, we make the third element of the array as key and will compare it with elements to it's left and insert
        it at the right position.
    4. And we go on repeating this, until the array is sorted.
-> Time complexity - O(n2)
-> Space complexity - O(1)
"""


def insertion_sort(num_array):
    for i in range(len(num_array)):
        j = i
        # swap the indexs of 2nd condition of this while loop to get descending sorted array
        # i.e. num_array[j] > num_array[j-1]
        while j > 0 and num_array[j-1] > num_array[j]:
            num_array[j], num_array[j-1] = num_array[j-1], num_array[j]
            j -= 1
    return num_array


num_array = [41, 27, 68, 11, 3, 45, 60, 17, 44, 35, 23, 23, 47]
print(insertion_sort(num_array))
