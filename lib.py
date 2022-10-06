def a(n):
    sum_of_elem = sum([len(i) for i in n])
    buffer = []
    for i in n:
        for j in i:
            if j not in buffer:
                buffer.append(j)
    return sum_of_elem - len(buffer)
