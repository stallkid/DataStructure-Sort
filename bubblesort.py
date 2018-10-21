import numpy
import time

def bubble_sort(lst, asc=True):
    lst = list(lst) # transforma em lista
    for left in range(len(lst)-1, 0, -1):
        for i in range(left):
            if asc:
                if lst[i] > lst[i + 1]:
                    lst[i], lst[i + 1] = lst[i + 1], lst[i]
            else:
                if lst[i] < lst[i + 1]:
                    lst[i], lst[i + 1] = lst[i + 1], lst[i]
    return lst


ls = numpy.random.randint(100, size=10)

t1 = time.time()
print("\n Ordem Randômica: ", ls)
t2 = time.time()
print("Randomico: ", (t2 - t1))
t3 = time.time()
print("\n Ordem Crescente: ", bubble_sort(ls, asc=True))
t4 = time.time()
print("Crescente: ", t4 - t3)
t5 = time.time()
print("\n Ordem Descrescente: ", bubble_sort(ls, asc=False))
t6 = time.time()
print("Decrescente: ", (t6 - t5))
