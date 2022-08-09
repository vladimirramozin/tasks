#! /usr/bin/env python
# -*- coding: utf-8 -*-
import time


class Quee():
    def __init__(self, max = 0):
        self.quee = []
        self.max = max

    def push(self, value):
        if len(self.quee)!= self.max:
            self.quee.append(value)
        else:
            return 'error'

    def print_quee(self):
        print(self.quee)

    def pop(self):
        if len(self.quee) >= 1:
            for i in range(0, len(self.quee)-1):
                self.quee[i] = self.quee[i+1]
            self.quee.pop()
        elif len(self.quee) == 1:
            self.quee.pop()
        else:
            return 'error'


def delta_time(start_test, stop_test):
    return stop_test - start_test


if __name__ == '__main__':
    quee = Quee(10000)
    start_test = time.time()
    for i in range(0, 10000):
        quee.push(i)
    stop_test = time.time()
    print 'put 10000, time'
    print delta_time(start_test, stop_test)
    start_test = time.time()
    for i in range(0, 10000):
        quee.pop()
    stop_test = time.time()
    print 'pop 10000, time'
    print delta_time(start_test, stop_test)
