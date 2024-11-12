import random
import array
import time

# Phase 2
#Mazin part
def binary_Search(sorted_array, target):
    left = 0
    right = len(sorted_array) - 1
    while left <= right:
        mid = (left + right) // 2
        if sorted_array[mid] == target:
            return mid  
        elif sorted_array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return None 

# Phases 1 and 3
def generate_sorted_data(size):
    """
    This function generates and returns a sorted array of integers of the specified size.

    If size <= 100, it generates random integers between 1 and 100 and sorts them using insertion sort.
    If size > 100, generates a larger array and sorts it using merge sort.

    Args:
        size (int): The size of the array to generate.

    Returns:
        array.array: The sorted array of integers.
    """
    # Aiswarya part
    if size <= 100:
        array1 = array.array("i", [0] * size)
        count = 0
        while count < size:
            array1[count] = random.randint(1, 100)
            count += 1
        print("Unsorted array:", array1)

        for i in range(1, size):
            temp = array1[i]
            j = i - 1
            while j >= 0 and array1[j] > temp:
                array1[j + 1] = array1[j]
                j -= 1
            array1[j + 1] = temp
        
        return array1
    
    # Dhanraaj's Work
    else:
        large_data = [55, 22, 89, 34, 67, 90, 15, 72, 39, 44] + [random.randint(1, 100) for _ in range(990)]
        sorted_array = merge_sort(large_data)
        return array.array("i", sorted_array)


def merge_sort(arr):
    """
    This fucntion recursively sorts an array using merge sort.

    Args:
        arr (list): The list of integers to sort.

    Returns:
        list: The sorted list.
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    sorted1 = merge_sort(arr[:mid])
    sorted2 = merge_sort(arr[mid:])

    return merge(sorted1, sorted2)

def merge(sorted1, sorted2):
    """
    Merges two sorted lists into one sorted list.

    Args:
        sorted1 (list): The first sorted list.
        sorted2 (list): The second sorted list.

    Returns:
        list: The merged and sorted list.
    """
    result = [0] * (len(sorted1) + len(sorted2))
    i1 = 0
    i2 = 0
    result_index = 0

    while i1 < len(sorted1) and i2 < len(sorted2):
        if sorted1[i1] <= sorted2[i2]:
            result[result_index] = sorted1[i1]
            i1 += 1
        else:
            result[result_index] = sorted2[i2]
            i2 += 1
        result_index += 1

    while i1 < len(sorted1):
        result[result_index] = sorted1[i1]
        i1 += 1
        result_index += 1

    while i2 < len(sorted2):
        result[result_index] = sorted2[i2]
        i2 += 1
        result_index += 1

    return result

# Phase 4
def linear_search(arr, target):
    """
    Performs a linear search on an array to find the index of a target value.

    Args:
        arr (array.array): The array to search.
        target (int): The value to search for.

    Returns:
        int or None: The index of the target value if found, otherwise None.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return None

def measure_search_time(sorted_array, target):
    """
    Measures and prints the time taken for binary search and linear search on a sorted array to compare the two.

    Args:
        sorted_array (array.array): The sorted array to search.
        target (int): The value to search for.

    Returns:
        None
    """
    start = time.perf_counter()
    binary_Search(sorted_array, target)
    end = time.perf_counter()
    print(f"Binary search time: {end - start:.6f} seconds")
    
    start = time.perf_counter()
    linear_search(sorted_array, target)
    end = time.perf_counter()
    print(f"Linear search time: {end - start:.6f} seconds")


def main():
    """
    The main function to use and run all the previous functions.

    Phases:
    1. Prompts the user to enter a size to generate and display a sorted array.
    2. Asks the user for a target value. Then, measures and compares the time taken for binary and linear searches on the array.

    Returns:
        None
    """

    # Main for Phases 1 and 3
    size = int(input("Input the number of values (e.g., 1000 for large data): "))
    new = generate_sorted_data(size)
    
    # Print the first 10 elements only
    # print("Sorted array:", new[:10], "...")

    # Printing the entire array
    print("Complete sorted array:", new)

    # Main for Phases 2 & 4
    target = int(input("Input a target value for searching: "))
    measure_search_time(new, target)

    # Commented to use 1 user-inputted target to compare linear search and binary search efficiencies.
    # targets = [9,8,7]
    # for i in targets:
    #     index = binary_Search(new, i)
    #     if index != None:
    #         print(f"{i} found at index num {index} ")
    #     else:
    #         print(f"there is no index that has {i}")
    
if __name__ == "__main__":
    main()