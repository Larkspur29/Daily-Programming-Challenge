def missingNumber(nums):
    n = len(nums)
    x = [-1] * (n + 2)
    for y in nums:
        x[y] = y
    for i in range(1, n + 2):
        if x[i] == -1:
            return i
