#!/usr/bin/env python3
import sys

def sustituir_caracteres_escape(s):
    s = s.replace('\\n','\n')
    s = s.replace('\\t','\t')

    return s

print(sustituir_caracteres_escape(" ".join(sys.argv[1:])))