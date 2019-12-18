def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i  
    return smallest_index

def selectionSort(arr):
    newarr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newarr.append(arr.pop(smallest)) 
    print(newarr)
    return newarr


sp = [100, 2, 43, 12, 123, 564]
selectionSort(sp)