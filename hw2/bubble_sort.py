import os
import sys
from dateutil.parser import parse
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


x=sort()
for filename in os.listdir("HW2_dataset"):
    print()
    date = []
    print(filename)
    if filename.endswith(".log"):
        with open("HW2_dataset/"+filename) as f:
            lines=f.read().split("\n")
            for line in lines:
                if line:
    #                print(line.split(" ")[0] )
     #               print(type(line.split(" ")[0]))
                    date.append(parse(line.split(" ")[0]))
            #sorted=x.bubble_sort(lines,date,len(date))
            sorted = x.quickSort(lines, date, 0,len(date)-1)
        f.close()
        f=open("HW2_dataset/"+filename+"_sorted",'+w')
        for i in sorted:
            f.write(i+"\n")
        f.close()
        #exit()
