''' reference
https://alex.dzyoba.com/blog/writing-diff/
'''
##!/usr/bin/python3
from hashfile import hashfile
import sys
#!/usr/bin/env python3
from functools import partial

from lcs import lcslen

# Print without newline because input files already have it
_print = partial(print, end='')

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

def diff(x, y,str1,str2):
    c = lcslen(x, y)
    #print(c)
    print("question part d bonus results")
    return print_diff(c, str1, str2, len(x)-1, len(y)-1)

def diff2(x, y):
    c = lcslen(x, y)
    #print(c)
    print("question part c results")
    return print_diff(c, x, y, len(x)-1, len(y)-1)

def usage():
    print("Usage: {} <file1> <file2>".format(sys.argv[0]))


f1,str1=hashfile(sys.argv[1])
f2,str2=hashfile(sys.argv[2])
#print(f1)
#print(f2)
diff2(f1,f2)
diff(f1,f2,str1,str2)
