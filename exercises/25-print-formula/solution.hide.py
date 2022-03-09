#!/usr/bin/env python
import math
def print_formula(n1,n2,n3):
    value = []
    items=[x for x in "{},{},{}".format(n1,n2,n3).split(',')]
    for d in items:
        value.append(str(int(round(math.sqrt(2*50*float(d)/30)))))

    return (','.join(value))
