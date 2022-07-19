def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands are different lengths")

    dist = 0
    for idx in range(len(strand_a)):
        if strand_a[idx] != strand_b[idx]:
            dist += 1
    return dist


