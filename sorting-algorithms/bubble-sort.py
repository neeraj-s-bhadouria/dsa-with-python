"""
-> Bubble Sort Algorithm
    Bubble Sort is a simple algorithm which is used to sort a given set of n elements provided in form of an array
    with n number of elements. Bubble Sort compares all the element one by one and sort them based on their values.
    If the given array has to be sorted in ascending order, then bubble sort will start by comparing the first element
    of the array with the second element, if the first element is greater than the second element, it will swap both
    the elements, and then move on to compare the second and the third element, and so on.
    If we have total n elements, then we need to repeat this process for n-1 times.
-> Time complexity - O(n2)
-> Space complexity - O(1)
"""


def bubble_sort(num_array):
    for i in range(len(num_array)):
        is_sorted = True
        for j in range(len(num_array)-i-1):
            if num_array[j] > num_array[j+1]:
                num_array[j], num_array[j+1] = num_array[j+1], num_array[j]
                is_sorted = False
        if is_sorted:
            break
    return num_array


num_array = [41, 27, 68, 11, 3, 45, 60, 17, 44, 35, 23, 23, 47]
print(bubble_sort(num_array))
