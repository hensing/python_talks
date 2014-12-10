#!/usr/bin/python
# coding: utf-8
import numpy as np
from time import sleep

def sub1():
    sleep(0.02)
    return ''.join([str(number) for number in xrange(100)])

def sub2():
    sleep(0.001)
    return [(x, x) for x in xrange(1000)]

def test():
    res = []
    for _ in xrange(15):
        res.append(sub1())
        for _ in xrange(20):
            res.append(sub2())
