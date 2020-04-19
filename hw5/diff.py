#!/usr/bin/env python3
''' reference
https://alex.dzyoba.com/blog/writing-diff/
'''
from hashfile import hashfile
import sys
from functools import partial

from lcs import lcslen

arr1=[]
arr2=[]
def print_diff(c, x, y, i, j):
    """Print the diff using LCS length matrix by backtracking it"""

    if i < 0 and j < 0:
        return ""
    elif i < 0 and j >=0:
        print_diff(c, x, y, i, j - 1)
        print("+ " + y[j].strip("\n"))
    elif j < 0 and i >=0:
        print_diff(c, x, y, i - 1, j)
        print("- " + x[i].strip("\n"))
    elif x[i] == y[j]:
        print_diff(c, x, y, i - 1, j - 1)
        print("  " + x[i].strip("\n"))
    elif c[i][j - 1] >= c[i - 1][j]:
        print_diff(c, x, y, i, j - 1)
        print("+ " + y[j].strip("\n"))
    elif c[i][j - 1] < c[i - 1][j]:
        print_diff(c, x, y, i - 1, j)
        print("- " + x[i].strip("\n"))

def print_diff1(c, x, y, i, j):

    if i < 0 and j < 0:
        #print("in2")
        return ""
    elif i < 0 and j >=0:
        print_diff1(c, x, y, i, j - 1)
    elif j < 0 and i >=0:
        print_diff1(c, x, y, i - 1, j)
    elif x[i] == y[j]:
        #print("in")
        print_diff1(c, x, y, i - 1, j - 1)
        arr1.append(i+1)
        arr2.append(j+1)
        #print("2 " + str(j+1))
    elif c[i][j - 1] >= c[i - 1][j]:
        print_diff1(c, x, y, i, j - 1)
    elif c[i][j - 1] < c[i - 1][j]:
        print_diff1(c, x, y, i - 1, j)


def diff(x, y,str1,str2):
    c = lcslen(x, y)
    #print(c)
    print("question part d bonus results")

    return print_diff(c, str1, str2, len(x)-1, len(y)-1)

def diff2(x, y):
    c = lcslen(x, y)
    #print(c)
    print("question part c results")
    print_diff1(c, x, y, len(x)-1, len(y)-1)
    for i in range(len(arr1)):
        print(str(arr1[i]) + " ",end=' ')
    print()
    for i in range(len(arr2)):
        print(str(arr2[i]) + " ",end=' ')
    print()
    return ""

def usage():
    print("Usage: {} <file1> <file2>".format(sys.argv[0]))


f1,str1=hashfile(sys.argv[1])
f2,str2=hashfile(sys.argv[2])
#print(f1)
#print(f2)
diff2(f1,f2)

diff(f1,f2,str1,str2)
