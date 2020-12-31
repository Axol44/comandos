#!/usr/bin/env python3
import sys

f = open(sys.argv[1])
for linea in f.read():
    print(linea, end='')
f.close()