def qksort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) //2]
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return qksort(left) + mid + qksort(right)
arr = [10, 3, 8, 15, 6, 22, 2, 8, 17]
sorted_arr = qksort(arr)
print(sorted_arr)