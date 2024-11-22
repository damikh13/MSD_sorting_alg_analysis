def msd_radix_sort(arr, counter):
    if len(arr) <= 1:
        return arr

    max_num = max(arr)
    exp = len(str(max_num))
    
    return bucket_sort(arr, exp, counter)
def bucket_sort(arr, exp, counter):
    if exp == 0 or len(arr) <= 1:
        return arr
    
    buckets = [[] for _ in range(10)]
    
    # distribute all numbers among diffirent buckets
    for cur_num in arr:
        cur_num_digit = (cur_num // (10 ** (exp - 1))) % 10
        buckets[cur_num_digit].append(cur_num)
        counter.increment() # moved number (1 basic operation)
    
    sorted_arr = []
    for bucket in buckets:
        if bucket:
            sorted_bucket = bucket_sort(bucket, exp - 1, counter)
            sorted_arr.extend(sorted_bucket)
            counter.increment()
    
    return sorted_arr
