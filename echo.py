#!/usr/bin/env python3
import sys

def verificacion(cadena):
    x = cadena.replace('\\n','\n')
    x = x.replace('\\t','\t')

    return x

for x in sys.argv[1:]:
    print(verificacion(x), end=" ")
print("")
