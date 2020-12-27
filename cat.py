#!/usr/bin/env python3
import sys

""" f = open("text.txt")
print(f.read()) """

"""
f = open(sys.argv[1])
print(f.read())
f.close()"""

"""
f = open(sys.argv[1])
for linea in f.read():
    print(linea ,end='')

print('')
f.close()"""
for x in range(1, len(sys.argv)):

    with open(sys.argv[x]) as f:
        for linea in f.read():
            print(linea ,end='')

