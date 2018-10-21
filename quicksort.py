from random import randint
import numpy
import time


def quickSort(L, asc=True, sortTime=False):
    if len(L) <= 1:
        return L
    smaller, equal, larger = [], [], []
    pivot = L[randint(0, len(L) - 1)]

    for x in L:
        if x < pivot:
            smaller.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            larger.append(x)

    larger = quickSort(larger, asc=asc)
    smaller = quickSort(smaller, asc=asc)

    if asc:
        final = smaller + equal + larger
    else:
        final = larger + equal + smaller

    return final

# l2 = numpy.random.randint(1000, size=100)
# t1 = time.time()
# print("\n Ordem Randômica: ", l2)
# t2 = time.time()
# print("Randomico: ", (t2 - t1))
# t3 = time.time()
# print("\n Ordem Crescente: ", quickSort(l2, asc=True, sortTime=False))
# t4 = time.time()
# print("Crescente: ", t4 - t3)
# t5 = time.time()
# print("\n Ordem Descrescente: ", quickSort(l2, asc=False, sortTime=False))
# t6 = time.time()
# print("Decrescente: ", (t6 - t5))
