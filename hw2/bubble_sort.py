import os
from dateutil.parser import parse
class sort:
    def __init__(self):
        print("in constructor\n")

    def bubble_sort(self,dataset,timestamp_list,size):
        for i in range(size):
            for j in range(0,size-i-1):
                if timestamp_list[j]>timestamp_list[j+1]:
                    timestamp_list[j],timestamp_list[j+1]=timestamp_list[j+1],timestamp_list[j]
                    dataset[j],dataset[j+1]=dataset[j+1],dataset[j]
        return dataset

    def merge(self,dataset, timestamp_list, l, m, r):
        n1 = m - l + 1
        n2 = r - m
        L = [0] * n1
        R = [0] * n2

        for i in range(0, n1):
            L[i] = timestamp_list[l + i]
            L2[i] = dataset[l + i]

        for j in range(0, n2):
            R[j] = timestamp_list[m + 1 + j]
            R2[j] = dataset[m + 1 + j]

        i = 0
        j = 0
        k = l

        while i < n1 and j < n2:
            if L[i] <= R[j]:
                dataset[k] = L2[i]
                i += 1
            else:
                dataset[k] = R2[j]
                j += 1
            k += 1

        while i < n1:
            dataset[k] = L2[i]
            i += 1
            k += 1

        while j < n2:
            dataset[k] = R2[j]
            j += 1
            k += 1

    def mergeSort(self,dataset, timestamp_list, l, r):
        if l < r:
            m = (l + (r - 1)) // 2

            mergeSort(dataset, timestamp_list, l, m)
            mergeSort(dataset, timestamp_list, m + 1, r)
            merge(dataset, timestamp_list, l, m, r)


x=sort()

for filename in os.listdir("HW2_dataset"):
    date = []
    print(filename)
    if filename.endswith(".log"):
        with open("HW2_dataset/"+filename) as f:
            lines=f.read().split("\n")
            for line in lines:
                if line:
                    print(line.split(" ")[0] )
                    print(type(line.split(" ")[0]))
                    date.append(parse(line.split(" ")[0]))
            sorted=x.bubble_sort(lines,date,len(date))
            for i in sorted:
                print(i)
