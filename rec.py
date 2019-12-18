def recmas(arr):
    if arr == []:
        return 0
    return arr[0] + sum(arr[1:])

def count(arr):
    if arr == []:
        return 0
    return 1 + count(arr[1:])

def max(arr):
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    sub_max = max(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max

mas = [1, 10, 12, 2]

print(recmas(mas))
print(count(mas))
print(max(mas))