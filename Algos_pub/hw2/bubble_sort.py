import os
import sys
from dateutil.parser import parse
<<<<<<< HEAD
import datetime
sys.setrecursionlimit(10**6)
=======
# import datetime
import time
import json
import math

sys.setrecursionlimit(10 ** 6)
num_warm = 5
num_execute = 10


>>>>>>> ayushi
class sort:
    def __init__(self):
        print("in constructor\n")

<<<<<<< HEAD
    def bubble_sort(self,dataset,timestamp_list,size):
        for i in range(size):
            for j in range(0,size-i-1):
                if timestamp_list[j]>timestamp_list[j+1]:
                    timestamp_list[j],timestamp_list[j+1]=timestamp_list[j+1],timestamp_list[j]
                    dataset[j],dataset[j+1]=dataset[j+1],dataset[j]
        return dataset
##########################mergeSort#################################################################
    def partition(self,dataset, timestamp_list, low, high):
=======
    def bubble_sort(self, dataset, timestamp_list, size):
        i = 0
        j = 0
        for i in range(size):
            for j in range(0, size - i - 1):
                if timestamp_list[j] > timestamp_list[j + 1]:
                    timestamp_list[j], timestamp_list[j + 1] = timestamp_list[j + 1], timestamp_list[j]
                    dataset[j], dataset[j + 1] = dataset[j + 1], dataset[j]
        return dataset

    ##############################################quickSort#################################################################
    def partition(self, dataset, timestamp_list, low, high):
>>>>>>> ayushi
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
<<<<<<< HEAD
    def quickSort(self,dataset, timestamp_list, low, high):
=======
    def quickSort(self, dataset, timestamp_list, low, high):
>>>>>>> ayushi
        if low < high:
            # pi is partitioning index, arr[p] is now
            # at right place
            pi = self.partition(dataset, timestamp_list, low, high)

            # Separately sort elements before
            # partition and after partition
            self.quickSort(dataset, timestamp_list, low, pi - 1)
            self.quickSort(dataset, timestamp_list, pi + 1, high)
            return dataset

<<<<<<< HEAD
    def merge(self,dataset, timestamp_list, l, m, r):
=======
    #####################################################MergeSort#########################################################
    def merge(self, dataset, timestamp_list, l, m, r):
>>>>>>> ayushi
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
<<<<<<< HEAD
                timestamp_list[k]=L[i]
=======
                timestamp_list[k] = L[i]
>>>>>>> ayushi
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

<<<<<<< HEAD
    def mergeSort(self,dataset, timestamp_list, l, r):
=======
    def mergeSort(self, dataset, timestamp_list, l, r):
>>>>>>> ayushi
        if l < r:
            m = int((l + (r - 1)) / 2)

            self.mergeSort(dataset, timestamp_list, l, m)
            self.mergeSort(dataset, timestamp_list, m + 1, r)
            self.merge(dataset, timestamp_list, l, m, r)
        return dataset

<<<<<<< HEAD
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
=======

########################################################################################################################
def truncate(number, digits) -> float:
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper


x = sort()
sorts = ["merge_ana.csv", "quick_ana.csv", "bb_ana.csv"]

# f_1 = open("bb_ana.csv",'w')
for f_sort in sorts:
    f_1 = open(f_sort, 'w')
    for filename in os.listdir("HW2_dataset"):
        print(filename)

        if filename.endswith(".log"):
            f_1.write(filename + "\n")
            warm_loadtime = []
            exec_loadtime = []
            warm_sorttime = []
            exec_sorttime = []
            warm_parsetime = []
            exec_parsetime = []
            for l in range(num_warm + num_execute):
                date = []
                with open("HW2_dataset/" + filename) as f:
                    enter = time.time()
                    lines = f.read().split("\n")
                    exit = time.time()
                    print("The loading time is {0}".format(exit - enter))
                    sub = truncate(float(exit - enter), 6)
                    if l < num_warm:
                        warm_loadtime.append(str(sub))
                    else:
                        exec_loadtime.append(str(sub))
                    enter = time.time()
                    for line in lines:
                        if line:
                            date.append(parse(line.split(" ")[0]))
                    exit = time.time()
                    sub = truncate(float(exit - enter), 6)
                    print("The parsing time is {0}".format(exit - enter))
                    if l < num_warm:
                        warm_parsetime.append(str(sub))
                    else:
                        exec_parsetime.append(str(sub))

                    if (f_sort == "bb_ana.csv"):
                        enter = time.time()
                        sorteed = x.bubble_sort(lines, date, len(date))
                        exit = time.time()
                    elif (f_sort == "merge_ana.csv"):
                        enter = time.time()
                        sorteed = x.mergeSort(lines, date, 0, len(date) - 1)
                        exit = time.time()
                    else:
                        enter = time.time()
                        sorteed = x.quickSort(lines, date, 0, len(date) - 1)
                        exit = time.time()
                    # sorteed=x.bubble_sort(lines,date,len(date))

                    sub = truncate(float(exit - enter), 6)
                    print("The sorting time is {0}".format(exit - enter))
                    if l < num_warm:
                        warm_sorttime.append(str(sub))
                    else:
                        exec_sorttime.append(str(sub))
                f.close()

                with open(filename.split(".")[0] + "sorted_log_%s.txt" % (f_sort.split(".")[0]), 'w') as f2:
                    for m in sorteed:
                        f2.write(m + '\n')
                f2.close()

            # f_1.write("The %s sort analysis data for " %f_sort + filename[:-4] + " is as following: \n")
            for i in range(num_warm):
                if (i != num_warm - 1):
                    f_1.write("%s_warm_load_%s," % (f_sort, i))
                else:
                    f_1.write("%s_warm_load_%s\n" % (f_sort, i))
            for i in range(num_warm):
                if (i != num_warm - 1):
                    f_1.write(warm_loadtime[i] + ",")
                else:
                    f_1.write(warm_loadtime[i] + "\n\n")
            for i in range(num_execute):
                if (i != num_execute - 1):
                    f_1.write("%s_exec_load_%s," % (f_sort, i))
                else:
                    f_1.write("%s_exec_load_%s\n" % (f_sort, i))
            for i in range(num_execute):
                if (i != num_execute - 1):
                    f_1.write(exec_loadtime[i] + ",")
                else:
                    f_1.write(exec_loadtime[i] + "\n")
            for i in range(num_warm):
                if (i != num_warm - 1):
                    f_1.write("%s_warm_parse_%s," % (f_sort, i))
                else:
                    f_1.write("%s_warm_parse_%s\n" % (f_sort, i))
            for i in range(num_warm):
                if (i != num_warm - 1):
                    f_1.write(warm_parsetime[i] + ",")
                else:
                    f_1.write(warm_parsetime[i] + "\n\n")
            for i in range(num_execute):
                if (i != num_execute - 1):
                    f_1.write("%s_exec_parse_%s," % (f_sort, i))
                else:
                    f_1.write("%s_exec_parse_%s\n" % (f_sort, i))
            for i in range(num_execute):
                if (i != num_execute - 1):
                    f_1.write(exec_parsetime[i] + ",")
                else:
                    f_1.write(exec_parsetime[i] + "\n\n")
            for i in range(num_warm):
                if (i != num_warm - 1):
                    f_1.write("%s_warm_sort_%s," % (f_sort, i))
                else:
                    f_1.write("%s_warm_sort_%s\n" % (f_sort, i))
            for i in range(num_warm):
                if (i != num_warm - 1):
                    f_1.write(warm_sorttime[i] + ",")
                else:
                    f_1.write(warm_sorttime[i] + "\n\n")
            for i in range(num_execute):
                if (i != num_execute - 1):
                    f_1.write("%s_exec_sort_%s," % (f_sort, i))
                else:
                    f_1.write("%s_exec_sort_%s\n" % (f_sort, i))
            for i in range(num_execute):
                if (i != num_execute - 1):
                    f_1.write(exec_sorttime[i] + ",")
                else:
                    f_1.write(exec_sorttime[i] + "\n\n")
            '''f_1.write('warm up load times are: \n')
            json.dump(warm_loadtime, f_1)
            f_1.write('\n Main exectution Load times are \n')
            json.dump(exec_loadtime, f_1)
            f_1.write('\n warm up sort times are: \n')
            json.dump(warm_sorttime, f_1)
            f_1.write('\n Main exectution sort times are \n')
            json.dump(exec_sorttime, f_1)
            f_1.write("\n")'''
    f_1.close()
'''
f_2 = open("merge_ana.txt",'w')
for filename in os.listdir("HW2_dataset"):
    print(filename)
    if filename.endswith(".log"):
        warm_loadtime = []
        exec_loadtime = []
        warm_sorttime = []
        exec_sorttime = []
        for l in range(num_warm + num_execute):
            date = []
            with open("HW2_dataset/"+filename) as f:
                enter = time.time()
                lines=f.read().split("\n")
                exit = time.time()
                print("The loading time is {0}" .format(time.time()-enter))
                sub = truncate(float(exit - enter), 6)
                if l < num_warm:
                    warm_loadtime.append(str(sub))
                else:
                    exec_loadtime.append(str(sub))
                for line in lines:
                    if line:
                        date.append(parse(line.split(" ")[0]))
                enter = time.time()
                m_sort=x.mergeSort(lines, date,0,len(date)-1)
                exit = time.time()
                sub = truncate(float(exit - enter), 6)
                print("The sorting time is {0}".format(exit - enter))
                if l < num_warm:
                    warm_sorttime.append(str(sub))
                else:
                    exec_sorttime.append(str(sub))
            f.close()

            with open(filename+"m_sorted_log.txt", 'w') as f2:
                for m in m_sort:
                    f2.write(m + '\n')
            f2.close()

        f_2.write("The Merge sort analysis data for "+ filename[:-4] + " is as following: \n")
        f_2.write('warm up load times are: \n')
        json.dump(warm_loadtime, f_2)
        f_2.write('\n Main exectution Load times are \n')
        json.dump(exec_loadtime, f_2)
        f_2.write('\n warm up sort times are: \n')
        json.dump(warm_sorttime, f_2)
        f_2.write('\n Main exectution sort times are \n')
        json.dump(exec_sorttime, f_2)
        f_2.write("\n")
f_2.close()

f_3 = open("quick_ana.txt",'w')
for filename in os.listdir("HW2_dataset"):
    print(filename)
    if filename.endswith(".log"):
        warm_loadtime = []
        exec_loadtime = []
        warm_sorttime = []
        exec_sorttime = []
        for l in range(num_warm + num_execute):
            date = []
            with open("HW2_dataset/"+filename) as f:
                enter = time.time()
                lines=f.read().split("\n")
                exit = time.time()
                print("The loading time is {0}" .format(time.time()-enter))
                sub = truncate(float(exit - enter), 6)
                if l < num_warm:
                    warm_loadtime.append(str(sub))
                else:
                    exec_loadtime.append(str(sub))
                for line in lines:
                    if line:
                        date.append(parse(line.split(" ")[0]))
                enter = time.time()

                q_sort=x.quickSort(lines, date,0,len(date)-1)
                exit = time.time()
                sub = truncate(float(exit - enter), 6)
                print("The sorting time is {0}".format(exit - enter))
                if l < num_warm:
                    warm_sorttime.append(str(sub))
                else:
                    exec_sorttime.append(str(sub))
            f.close()

            with open(filename+"m_sorted_log.txt", 'w') as f2:
                for m in q_sort:
                    f2.write(m + '\n')
            f2.close()

        f_3.write("The Quick sort analysis data for "+ filename[:-4] + " is as following: \n")
        f_3.write('warm up load times are: \n')
        json.dump(warm_loadtime, f_3)
        f_3.write('\n Main exectution Load times are \n')
        json.dump(exec_loadtime, f_3)
        f_3.write('\n warm up sort times are: \n')
        json.dump(warm_sorttime, f_3)
        f_3.write('\n Main exectution sort times are \n')
        json.dump(exec_sorttime, f_3)
        f_3.write("\n")
f_3.close()


'''





>>>>>>> ayushi
