from random import randint


def a(n):
    buffer = []
    for i in n:
        for j in i:
            if j not in buffer:
                buffer.append(j)

    return buffer


n = [[randint(0, 10) for i in range(5)] for j in range(5)]
print(n)