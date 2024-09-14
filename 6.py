def zero_sum_subarrays(arr):
    cum_sum_map = {}
    cum_sum = 0
    res = []

    for i, num in enumerate(arr):
        cum_sum += num
        
        if cum_sum == 0:
            res.append((0, i))
        
        if cum_sum in cum_sum_map:
            start_idx = cum_sum_map[cum_sum] + 1
            res.append((start_idx, i))
        
        cum_sum_map[cum_sum] = i
    
    return res

arr = [1, 2, -3, 3, -1, 2]
print(zero_sum_subarrays(arr))  
