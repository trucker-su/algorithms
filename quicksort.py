def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        piv = arr[0]
        less = [i for i in arr[1:] if i <= piv]
        great = [i for i in arr[1:] if i > piv]

        return quicksort(less) + [piv] + quicksort(great)

print(quicksort([3, 4, 7, 5, 1, 8, 2]))