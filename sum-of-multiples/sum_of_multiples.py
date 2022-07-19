def sum_of_multiples(limit, multiples):
    mult_set = set()
    for x in multiples:
        if x == 0:
            mult_set.add(0)
            continue
        mult_set.update([*range(x, limit, x)])

    return sum(mult_set)
