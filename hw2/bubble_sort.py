import os
import sys
from dateutil.parser import parse
import datetime
sys.setrecursionlimit(10**6)
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
##########################mergeSort#################################################################
    def partition(self,dataset, timestamp_list, low, high):
        i = (low - 1)
        pivot = timestamp_list[high]  # pivot

        for j in range(low, high):
            # If current element is smaller than the pivot

            if timestamp_list[j] < pivot:
                # increment index of smaller element
                i = i + 1
                dataset[i], dataset[j] = dataset[j], dataset[i]
                timestamp_list[i], timestamp_list[j] = timestamp_list[j], timestamp_list[i]

        dataset[i + 1], dataset[high] = dataset[high], dataset[i + 1]
        timestamp_list[i + 1], timestamp_list[high] = timestamp_list[high], timestamp_list[i + 1]
        return (i + 1)

    # The main function that implements QuickSort
    # arr[] --> Array to be sorted,
    # low  --> Starting index,
    # high  --> Ending index

    # Function to do Quick sort
    def quickSort(self,dataset, timestamp_list, low, high):
        if low < high:
            # pi is partitioning index, arr[p] is now
            # at right place
            pi = self.partition(dataset, timestamp_list, low, high)

            # Separately sort elements before
            # partition and after partition
            self.quickSort(dataset, timestamp_list, low, pi - 1)
            self.quickSort(dataset, timestamp_list, pi + 1, high)
            return dataset

    def merge(self,dataset, timestamp_list, l, m, r):
        n1 = m - l + 1
        n2 = r - m
        L = [0] * (n1)
        L2 = [0] * (n1)
        R = [0] * (n2)
        R2 = [0] * (n2)

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
                timestamp_list[k]=L[i]
                i += 1
            else:
                dataset[k] = R2[j]
                timestamp_list[k] = R[j]
                j += 1
            k += 1

        while i < n1:
            dataset[k] = L2[i]
            timestamp_list[k] = L[i]
            i += 1
            k += 1

        while j < n2:
            dataset[k] = R2[j]
            timestamp_list[k] = R[j]
            j += 1
            k += 1

    def mergeSort(self,dataset, timestamp_list, l, r):
        if l < r:
            m = int((l + (r - 1)) / 2)

            self.mergeSort(dataset, timestamp_list, l, m)
            self.mergeSort(dataset, timestamp_list, m + 1, r)
            self.merge(dataset, timestamp_list, l, m, r)
        return dataset

x=sort()
for filename in os.listdir("HW2_dataset"):
    print()
    date = []
    print(filename)
    if filename.endswith(".log"):
        with open("HW2_dataset/"+filename) as f:
            #print('Timestamp before reading data: {:%Y-%m-%d %H:%M:%S.%f}'.format(datetime.datetime.now()))
            enter = datetime.datetime.now()
            lines=f.read().split("\n")
            #print('Timestamp after reading data: {:%Y-%m-%d %H:%M:%S.%f}'.format(datetime.datetime.now()))
            exit = datetime.datetime.now()
            #print("read time taken  ",exit - enter)
            sub = exit - enter
            print('read time taken  ', +sub.microseconds)
            enter = datetime.datetime.now()
            for line in lines:
                if line:
    #                print(line.split(" ")[0] )
     #               print(type(line.split(" ")[0]))
                    date.append(parse(line.split(" ")[0]))
            #sorted=x.bubble_sort(lines,date,len(date))
            #print('Timestamp before sorting data: {:%Y-%m-%d %H:%M:%S.%f}'.format(datetime.datetime.now()))
            exit = datetime.datetime.now()
            #print("parse time taken  ", exit - enter)
            sub = exit - enter
            print('parse time taken  ', +sub.microseconds)
            enter = datetime.datetime.now()
            #print(enter)
            #sorted = x.quickSort(lines, date, 0,len(date)-1)
            #sorted = x.bubble_sort(lines, date, len(date))
            sorted = x.mergeSort(lines, date,0,len(date)-1)
            #print('Timestamp after sorting data: {:%Y-%m-%d %H:%M:%S.%f}'.format(datetime.datetime.now()))
            exit = datetime.datetime.now()
            #print(exit)
            #print("sort time taken  ", exit - enter)
            sub = exit - enter
            print('sort time taken  ', +sub.microseconds)
        f.close()
        f=open("HW2_dataset/"+filename+"_sorted",'+w')
        for i in sorted:
            f.write(i+"\n")
        f.close()
        #exit()
