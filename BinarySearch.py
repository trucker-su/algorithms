def binarysearch(list, item):
    low = 0
    high = len(list)-1
    
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            print('''
            
Искомое число занимает позицию:''', mid)
            return mid

        if guess > item:
            high = mid - 1
            print('''
            
Новый low:''', low)
            print('Новый high:', high)

        if guess < item:
            low = mid + 1
            print('''
            
Новый low:''', low)
            print('Новый high:', high)

    return None

myList = [i for i in range(100)]
#print(myList)
itm = int(input('Введите число:'))

binarysearch(myList, itm)
