#!/usr/bin/env python3
import sys

with open(sys.argv[1]) as f:
    for linea in f.read():
        print(linea, end='')
