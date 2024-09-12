def merge(arr1, arr2, n, m):
    left = n - 1
    right = 0
    while left >= 0 and right < m:
        if arr1[left] > arr2[right]:
            arr1[left], arr2[right] = arr2[right], arr1[left]
            left -= 1
            right += 1
        else:
            break

    arr1.sort()
    arr2.sort()

arr1 = [2, 3, 8]
arr2 = [4, 6, 10]
n = len(arr1)
m = len(arr2)
merge(arr1, arr2, n, m)
print(arr1,arr2)

