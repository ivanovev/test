
from collections import OrderedDict as OD
from util import find_from_table
import random

test_table1 = OD([(7,1), (11,1), (12.8, 0.8), (13.2, 0.2), (14,0), (15,0)])
test_table2 = OD([(7,0), (10,0), (10.8, 0.2), (11.2, 0.8), (12,1), (15,1)])

def TXC2_mntr1():
    return '%g' % (find_from_table(test_table1, TXC2_ctrl1.c) + random.randrange(-5, 5)/100)

def TXC2_mntr2():
    return '%g' % (find_from_table(test_table2, TXC2_ctrl2.c) + random.randrange(-5, 5)/100)

def TXC2_ctrl1(c=''):
    if c:
        TXC2_ctrl1.c = float(c)
        return c
    else:
        return '%g' % TXC2_ctrl1.c
TXC2_ctrl1.c = 7

def TXC2_ctrl2(c=''):
    if c:
        TXC2_ctrl2.c = float(c)
        return c
    else:
        return '%g' % TXC2_ctrl2.c
TXC2_ctrl2.c = 15

