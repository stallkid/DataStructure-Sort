def selectionSort(alist, asc=True):
   for fillslot in range(len(alist)-1, 0, -1):
       positionOfMax = 0
       for location in range(1, fillslot+1):
           if asc:
               if alist[location] > alist[positionOfMax]:
                    positionOfMax = location
           else:
               if alist[location] < alist[positionOfMax]:
                    positionOfMax = location

       temp = alist[fillslot]
       alist[fillslot] = alist[positionOfMax]
       alist[positionOfMax] = temp

       return alist


ls = [54, 26, 93, 17, 77, 31, 44, 55, 20]

print(selectionSort(ls, asc=True))
print(selectionSort(ls, asc=False))
# print(alist)
