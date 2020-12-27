#!/usr/bin/env python3
import sys

def verificacion(cadena):
    x = cadena.replace('\\n','\n')
    x = x.replace('\\t','\t')

    return x

for x in range(1, len(sys.argv)):
    print(verificacion(sys.argv[x]))
