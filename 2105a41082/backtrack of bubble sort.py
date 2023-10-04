def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def is_sorted(arr):
    n = len(arr)
    for i in range(1, n):
        if arr[i-1] > arr[i]:
            return False
    return True

def backtrack_sort(arr, index=0):
    n = len(arr)
    if index == n:
        if is_sorted(arr):
            print(arr)  
        return

    for i in range(index, n):
        arr[index], arr[i] = arr[i], arr[index] 
        backtrack_sort(arr, index + 1)
        arr[index], arr[i] = arr[i], arr[index]  
arr = [3, 1, 2]
backtrack_sort(arr)

