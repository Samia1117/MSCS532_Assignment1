"""
Insertion sort treats the array as two parts:
a sorted part on the left
an unsorted part on the right
The first element (arr[0]) is already considered sorted by itself
"""

def insertion_sort_desc(arr):
    """
    Sort a list in monotonically decreasing order using insertion sort.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


if __name__ == "__main__":

    # Try a variety of different sort orders
    test_cases = [
        [5, 2, 9, 1, 5, 6],
        [1, 2, 3, 4],
        [9, 7, 5, 3],
        [],
        [4, 2, 4, 1, 2],
        [-3, -1, -7, -2],
    ]

    for index, original_list in enumerate(test_cases, start=1):
        print(f"Test case {index}:")
        print("Original:", original_list)
        print(
            "Sorted (monotonically decreasing order):",
            insertion_sort_desc(original_list.copy()), # copy to create a new list
        )
        print()