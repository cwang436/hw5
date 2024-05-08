#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def gcd(a, b):
    if b>a:
        temp = a
        a = b
        b = temp
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
    
def remove_pairs(string):
    opposites = {"N": "S", "S": "N", "E": "W", "W": "E"}
    if len(string) <= 1:
        return string
    if string[0] == opposites[string[1]]:
        return remove_pairs(string[2:])
    else:
        return string[0] + remove_pairs(string[1:])
    
def sign(x):
    if x > 0:
        return "pos"
    if x < 0:
        return "neg"

import math

def bisection_root(function, x1, x2):
    print(function(x1))
    print(function(x2))
    if function(x1) > 0  and function(x2) > 0:
        raise ValueError()
    if function(x1) < 0  and function(x2) < 0:
        raise ValueError()
    if function(x1) <= 0.001 and function(x1) >= -0.001:
        return x1
    if function(x2) <= 0.001 and function(x2) >= -0.001:
        return x2
    else:
        xnew = (x1 + x2)/2
        if sign(function(xnew)) != sign(function(x1)):
            return bisection_root(function, xnew, x1)
        if sign(function(xnew)) != sign(function(x2)):
            return bisection_root(function, xnew, x2)
    
bisection_root(math.sin, 2, 4)
    