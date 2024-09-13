
def printLeaders(arr, n):
    ans = []
    max_elem = arr[n - 1]
    ans.append(arr[n - 1])
    for i in range(n - 2, -1, -1):
        if arr[i] > max_elem:
            ans.append(arr[i])
            max_elem = arr[i]

    return ans


n = 6
arr = [16, 17, 4, 3, 5, 2]

ans = printLeaders(arr, n)
print(ans)


