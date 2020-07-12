# assuming we have sorted list from a to b and b+1 to c
import os
from dateutil.parser import parse


def merg(input1, a, b, c):
    num1 = b - a + 1
    num2 = c - b
    left = [input1[a + y] for y in range(num1)]
    right = [input1[b + 1 + z] for z in range(num2)]
    left.append(float('inf'))
    right.append(float('inf'))

    u = 0
    v = 0
    for i in range(a, c + 1):
        if left[u] <= right[v]:
            input1[i] = left[u]
            u += 1
        else:
            input1[i] = right[v]
            v += 1


def merge_sort(input1, a, c):
    if a < c:
        b = (a + c) // 2
        merge_sort(input1, a, b)
        merge_sort(input1, b + 1, c)
        merg(input1, a, b, c)
    elif a == c:
        return input1[c]


# this is tested
# input1 = [5,1,7,3,6,8,3,1,5,6,7,11,22,68,98]
# merge_sort(input1,0,len(input1)-1)
# print(input1)

'''
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
            merge_sort(data,0,len(data)-1)
            for i in sorted:
                print(i)
'''

with open("HW2_dataset/" + "syslog10k.log") as f:
    date = []
    lines = f.read().split("\n")

    for line in lines:
        if line:
            date.append(parse(line.split(" ")[0]))
    merge_sort(date, 0, len(date) - 1)
    print(date)
