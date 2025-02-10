def mer(arr):
    if len(arr) > 1:
        mid = len(arr) //2
        left = arr[:mid]
        right = arr[mid:]
        mer(left)
        mer(right)
        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
                k += 1
            else:
                arr[k] = right[j]
                j += 1
                k +=1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

            
arr = [54, 26, 93, 17, 77, 31, 45, 55, 20]
mer(arr)
print(arr)                            