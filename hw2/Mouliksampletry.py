
this is me learning




copied code in case of a disaster:

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