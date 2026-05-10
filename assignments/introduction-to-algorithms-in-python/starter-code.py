def bubble_sort(arr):
    # TODO: implement bubble sort
    pass

def binary_search(arr, target):
    # TODO: implement binary search
    pass

# Test code
if __name__ == "__main__":
    # Test bubble sort
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", arr)
    sorted_arr = bubble_sort(arr.copy())
    print("Sorted array:", sorted_arr)

    # Test binary search
    target = 22
    index = binary_search(sorted_arr, target)
    print(f"Index of {target}: {index}")