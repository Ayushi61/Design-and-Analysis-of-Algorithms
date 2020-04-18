import os
from dateutil.parser import parse

def partition(dataset,timestamp_list, low, high):
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
def quickSort(dataset,timestamp_list, low, high):
    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(dataset,timestamp_list, low, high)

        # Separately sort elements before
        # partition and after partition
        quickSort(dataset,timestamp_list, low, pi - 1)
        quickSort(dataset,timestamp_list, pi + 1, high)


# Driver code to test above
'''
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr,0,n-1)
print ("Sorted array is:")
for i in range(n):
    print ("%d" %arr[i]),
'''
with open("HW2_dataset/" + "syslog10k.log") as f:
    date = []
    lines = f.read().split("\n")
    #print(lines)
    #(parse(line.split(" ")[0]))
    for line in lines:
        if line:
            date.append(parse(line.split(" ")[0]))
    quickSort(lines, date, 0, len(date) - 1)
    for m in range(len(lines)):
        print(lines[m])
    #for i in range(len(lines)):
        #print("%s" % lines[i]),
