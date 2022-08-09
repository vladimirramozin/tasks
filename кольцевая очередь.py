#! /usr/bin/env python
# -*- coding: utf-8 -*-
import time


class Quee:
    def __init__(self, n):
        self.quee = [None]*n
        self.start = 0
        self.current = 0
        self.__max = n

    def push(self, value):
        if self.current == self.start and self.quee[self.current] is None:
            self.quee[self.current] = value
            self.current = (self.current + 1) % self.__max
        elif (self.current == self.start
              and self.quee[self.current] is not None):
            print 'очередь переполнена'
        else:
            self.quee[self.current] = value
            self.current = (self.current + 1) % self.__max

    def pop(self):
        self.quee[self.start] = None
        self.start += 1

    def print_quee(self):
        for i in range(0, self.__max):
            if self.quee[(self.start + i) % self.__max] is not None:
                print(self.quee[(self.start + i) % self.__max])


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
