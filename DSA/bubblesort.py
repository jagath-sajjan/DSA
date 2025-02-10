def bubble(arr):
    n = len(arr)
    for j in range(n):
        for j in range(0, n-j-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [34, 65, 78, 45, 33, 23]
bubble(arr)
print(arr)