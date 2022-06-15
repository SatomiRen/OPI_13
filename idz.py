#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from multiprocessing import Process
from math import cos


eps = .0000001


def inf_sum(x,  num):
    a = 1
    summa = 1
    i = 1
    prev = 0
    while abs(summa - prev) > eps:
        a = a * x ** 2 / ((2 * i) * (2 * i - 1))
        prev = summa
        if i % 2 == 0:
            summa += a
        else:
            summa += -1 * a
        i += 1
    print(f"The sum number: {num} is: {summa}")
    print(f"Check: cos({x}) = {cos(x)}")


if __name__ == '__main__':
    process1 = Process(target=inf_sum, args=(0, 1))
    process1.start()
    process2 = Process(target=inf_sum, args=(3, 2))
    process2.start()
