#!/usr/bin/env python3
## -*- coding: utf-8 -*- vim:shiftwidth=4:expandtab:

import sys

if len(sys.argv) != 3:
    print(f'Usage: {sys.argv[0]} FILENAME SIZE')
    exit(1)

fname = sys.argv[1]
stop = int(sys.argv[2]) // 4

with open(fname, 'wb') as f:
    for b in range(stop):
        f.write(b.to_bytes(4))
