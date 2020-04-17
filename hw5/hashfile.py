#!/usr/bin/python3
from hash_func import hash10
import sys
def hashfile(filename):
    f1=open(filename, 'r')
    arr=[]
    for line in f1.readlines():
        #print(line.strip('\n')+ " " + str(hash10(line)))
        arr.append(str(hash10(line)))
    return arr

#hashfile(sys.argv[1])