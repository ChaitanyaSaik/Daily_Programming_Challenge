def sort(arr):
    low = 0
    mid = 0
    high = len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        elif arr[mid] == 2:
            arr[high], arr[mid] = arr[mid], arr[high]
            high -= 1
        else:
            print()


arr = [0, 1, 2, 1, 0, 2, 1, 0]
sort(arr)
print(arr) 
# Test case 2
arr1 = [2, 0, 1, 2, 0, 1, 0, 2, 1]
sort(arr1)
print(arr1) 

# Test case 3
arr2 = [1, 2, 0, 1, 2, 0, 1, 2, 0]
sort(arr2)
print(arr2) 

# Test case 4
arr3 = [1, 0, 2]
sort(arr3)
print(arr3) 

# Test case 5
arr4 = [2, 2, 2, 2, 2]
sort(arr4)
print(arr4) 

# Test case 6
arr5 = [0, 0, 0, 0]
sort(arr5)
print(arr5) 

