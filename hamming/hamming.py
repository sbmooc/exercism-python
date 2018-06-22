def distance(strand_a, strand_b):

    if strand_a == strand_b:
        return 0

    if len(strand_a) != len(strand_b):
        print(len(strand_a))
        print(len(strand_b))
        raise ValueError("TEST")

    strand_a = list(strand_a)

    strand_b = list(strand_b)

    counter = 0

    for ind, item in enumerate(strand_a):
        if item != strand_b[ind]:
            counter += 1

    return counter
