
#Write a program for sorting algorithms using appropriate knowledge representation and
#reasoning techniques

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

def merge(arr, p, q, r):
    left = arr[p:q+1]
    right = arr[q+1:r+1]
    
    i = j = 0
    k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i+=1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # Copy remaining elements
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

def Merge_sort(arr, p, r):
    if p < r:
        q = (p + r) // 2
        Merge_sort(arr, p, q)
        Merge_sort(arr, q + 1, r)
        merge(arr, p, q, r)

# Get user input for array
input_str = input("Enter space-separated integers for the array: ")
arr = list(map(int, input_str.split()))

'''
arr = list(map(int, input("Enter the numbers you want to sort: ").split()))

'''

# Get user input for sorting method
sorting_method = input("Enter sorting method (bubble/selection/merge): ").lower()

# Perform the selected sorting method
if sorting_method == 'bubble':
    bubble_sorted_arr = list(arr)
    bubble_sort(bubble_sorted_arr)
    print("Bubble Sorted Array:", bubble_sorted_arr)
elif sorting_method == 'selection':
    selection_sorted_arr = list(arr)
    selection_sort(selection_sorted_arr)
    print("Selection Sorted Array:", selection_sorted_arr)
elif sorting_method == 'merge':
    merge_sorted_arr = list(arr)
    Merge_sort(merge_sorted_arr,0,len(merge_sorted_arr))
    print("Merge Sorted Array:", merge_sorted_arr)
else:
    print("Invalid sorting method. Please enter 'bubble', 'selection', or 'merge'.")

# *********
# Output- 
# Enter space-separated integers for the array: 2 6 2 3 7
# Enter sorting method (bubble/selection/merge): bubble
# Bubble Sorted Array: [2, 2, 3, 6, 7]

# Enter space-separated integers for the array: 6 2 4 1 8
# Enter sorting method (bubble/selection/merge): selection
# Selection Sorted Array: [1, 2, 4, 6, 8]

# Enter space-separated integers for the array: 5 2 9 1 7
# Enter sorting method (bubble/selection/merge): merge
# Merge Sorted Array: [1, 2, 5, 7, 9]



