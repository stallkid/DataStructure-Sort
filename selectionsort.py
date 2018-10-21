import numpy
import time

def selectionSort(alist, asc=True):
   for i in range(len(alist)):
      # Find the minimum element in remaining
       minPosition = i
       for j in range(i+1, len(alist)):
           if asc:
               if alist[minPosition] > alist[j]:
                   minPosition = j
           else:
                if alist[minPosition] < alist[j]:
                   minPosition = j
       # Swap the found minimum element with minPosition
       temp = alist[i]
       alist[i] = alist[minPosition]
       alist[minPosition] = temp

   return alist


# ls = numpy.random.randint(1000, size=100)

# t1 = time.time()
# print("\n Ordem Randômica: ", ls)
# t2 = time.time()
# print("Randomico: ", (t2 - t1))
# t3 = time.time()
# print("\n Ordem Crescente: ", selectionSort(ls, asc=True))
# t4 = time.time()
# print("Crescente: ", t4 - t3)
# t5 = time.time()
# print("\n Ordem Descrescente: ", selectionSort(ls, asc=False))
# t6 = time.time()
# print("Decrescente: ", (t6 - t5))
