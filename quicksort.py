from random import randint
import numpy
import time


def quickSort(L, ascending=True):
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

    larger = quickSort(larger, ascending=ascending)
    smaller = quickSort(smaller, ascending=ascending)

    if ascending:
        final = smaller + equal + larger
    else:
        final = larger + equal + smaller
    return final


l2 = numpy.random.randint(100, size=10)
t1 = time.time()
print("\n Ordem Randômica: ", l2)
t2 = time.time()
print("Randomico: ", (t2 - t1))
t3 = time.time()
print("\n Ordem Crescente: ", quickSort(l2, ascending=True))
t4 = time.time()
print("Crescente: ", t4 - t3)
t5 = time.time()
print("\n Ordem Descrescente: ", quickSort(l2, ascending=False))
t6 = time.time()
print("Decrescente: ", (t6 - t5))
