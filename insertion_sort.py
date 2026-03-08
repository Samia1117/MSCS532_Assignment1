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
    sample_data = [5, 2, 9, 1, 5, 6]
    print("Original:", sample_data)
    print("Sorted (monotonically decreasing order):", insertion_sort_desc(sample_data))
    