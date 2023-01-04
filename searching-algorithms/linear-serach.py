"""
-> Linear Search Algorithm
    Linear search is a very basic and simple search algorithm. In Linear search,
    we search an element or value in a given array by traversing the array from the starting,
    till the desired element or value is found.
-> Implementing Linear Search
    1. Traverse the array using a for loop.
    2. In every iteration, compare the target value with the current value of the array.
        a. If the values match, return the current index of the array.
        b. If the values do not match, move on to the next array element.
    3. If no match is found, return -1.
-> Time Complexity - O(n)
"""


def linear_search(target, num_array):
    for i in range(len(num_array)):
        if num_array[i] == target:
            return i
    return -1


num_array = [4, 7, 11, 3, 5, -4, -7, 9, 8, 10, -9, 15, 32, 0]
print(linear_search(-7, num_array))
