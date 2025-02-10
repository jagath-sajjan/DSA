def inse(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j = j - 1

        arr[j+1] = key   

arr = [45, 67, 89, 23, 45, 67, 31]
inse(arr)
print(arr)