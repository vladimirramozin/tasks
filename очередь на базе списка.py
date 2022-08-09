#! /usr/bin/env python
# -*- coding: utf-8 -*-
import time


class Quee():
    def __init__(self):
        self.quee = []

    def push(self, value):
        self.quee.append(value)

    def print_quee(self):
        print(self.quee)

    def pop(self):
        if len(self.quee) != 1:
            for i in range(0, len(self.quee)-1):
                self.quee[i] = self.quee[i+1]
            self.quee.pop(i)
        else:
            self.quee.pop()


def delta_time(start_test, stop_test):
    return stop_test - start_test


if __name__ == '__main__':
    quee = Quee()
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
