#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
this is the code for pa5
'''


def gcd(num1, num2):
    '''finds the greatest common denominator of two numbers'''
    if num2 > num1:
        temp = num1
        num1 = num2
        num2 = temp
    if num2 == 0:
        return num1
    return gcd(num2, num1 % num2)


def remove_pairs(string):
    '''removes repetitive pairs in a maze path'''
    opposites = {"N": "S", "S": "N", "E": "W", "W": "E"}
    if len(string) <= 1:
        return string
    if string[0] == opposites[string[1]]:
        return remove_pairs(string[2:])
    return string[0] + remove_pairs(string[1:])


def sign(number):
    '''helper function for bisection_root'''
    if number > 0:
        return "pos"
    if number < 0:
        return "neg"


def bisection_root(function, x1, x2):
    '''finds the x intercept of a function given two guesses'''
    if function(x1) > 0 and function(x2) > 0:
        raise ValueError()
    if function(x1) < 0 and function(x2) < 0:
        raise ValueError()
    if function(x1) <= 0.0000001 and function(x1) >= -0.0000001:
        return x1
    if function(x2) <= 0.0000001 and function(x2) >= -0.0000001:
        return x2
    xnew = (x1 + x2)/2
    if sign(function(xnew)) != sign(function(x1)):
        return bisection_root(function, xnew, x1)
    if sign(function(xnew)) != sign(function(x2)):
        return bisection_root(function, xnew, x2)
