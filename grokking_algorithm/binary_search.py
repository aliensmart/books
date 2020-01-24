def binary_search(arr, item):
    first = 0
    last = len(arr)-1
    while first <= last:  #
        mid = (first + last)/2 #get the middle
        guess = arr[mid]
        if guess == item: #item founded
            return mid
        if guess > item : #means guess was too high
            last = mid - 1
        else:              #means guess was too low
            first = mid + 1
    return None            #The item doesn’t exist.