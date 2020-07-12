#!/usr/bin/env python3
from hash_func import hash10
import sys
def hashfile(filename):
    f1=open(filename, 'r')
    arr=[]
    arr_str=[]
    for line in f1.readlines():
        #print(line.strip('\n')+ " " + str(hash10(line)))
        arr.append(str(hash10(line)))
        arr_str.append(line)
    return (arr,arr_str)

#hashfile(sys.argv[1])