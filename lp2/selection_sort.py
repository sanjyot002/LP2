def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Example usage:
arr = [64, 25, 12, 22, 11]
selection_sort(arr)
print("Sorted array:", arr)



'''In the Selection Sort algorithm, the list is divided into two parts: the sorted portion at the beginning and the unsorted portion at the end. In each iteration, the algorithm finds the minimum element in the unsorted portion and swaps it with the element at the current position, effectively expanding the sorted portion by one element.

The selection_sort function takes an input list arr and sorts it in-place using the Selection Sort algorithm. The outer loop iterates through each position in the list, and the inner loop finds the minimum element starting from the current position. If a smaller element is found, the indices of the minimum element and the current position are swapped.

After the algorithm completes, the original list is sorted in non-decreasing order. In the example usage, the arr list is sorted using the selection_sort function, and the sorted array is printed.

Note that Selection Sort has a time complexity of O(n^2), where n is the number of elements in the list. While it is a simple and intuitive sorting algorithm, it is not the most efficient for large lists. Other sorting algorithms like Merge Sort or Quick Sort generally offer better performance.






'''


# Bubble sort
# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n - 1):
#         # Last i elements are already in place
#         for j in range(n - i - 1):
#             # Swap if the element found is greater than the next element
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]

# # Example usage:
# numbers = [5, 2, 9, 1, 3]
# bubble_sort(numbers)
# print("Sorted array:", numbers)