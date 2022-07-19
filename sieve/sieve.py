def primes(limit):
    # if LIMIT is 0 or 1, return empty list
    if limit < 2:
        return []

    # start to_filter with interval [2, LIMIT + 1). When LIMIT is 2, range(2, 3) returns [2].
    # bitmap starts will all indices set to prime (1). As we filter, we mark them not prime (0).
    to_filter = [*range(2, limit + 1)]
    bitmap = [1 for i in range(2, limit + 1)]

        
    for num in to_filter:
        idx = num - 2
        
        # skip num if has been marked as not prime
        if bitmap[idx] == 0:
            continue
        
        # mark all multiples of num in bitmap as not prime
        size = limit // num
        bitmap[idx::num] = [0] * size
        bitmap[idx] = 1

    # use bitmap and to_filter to generate list of primes
    filtered =  filter(lambda n: bitmap[n-2] == 1, to_filter)
    return list(filtered)
