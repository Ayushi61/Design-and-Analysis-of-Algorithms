import os
from dateutil.parser import parse

def merge(dataset, timestamp_list, l, m, r):
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


def mergeSort(dataset, timestamp_list, l, r):
    if l < r:
        m = (l + (r - 1)) // 2

        mergeSort(dataset, timestamp_list, l, m)
        mergeSort(dataset, timestamp_list, m + 1, r)
        merge(dataset, timestamp_list, l, m, r)


with open("HW2_dataset/" + "syslog10k.log") as f:
    date = []
    lines = f.read().split("\n")
    #print(lines)
    #(parse(line.split(" ")[0]))
    for line in lines:
        if line:
            date.append(parse(line.split(" ")[0]))
    print(date)
    print(len(date))
    mergeSort(lines, date, 0, len(date) - 1)
    #for i in range(len(lines)):
        #print("%s" % lines[i]),
