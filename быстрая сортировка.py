import time
from random import random


def quick_sort(value):
    if len(value) > 1:
        support_element = value.pop()
        right, left, middle = [], [], [support_element]
        for item in value:
            if item == support_element:
                middle.append(item)
            if item > support_element:
                right.append(item)
            else:
                left.append(item)
        return (quick_sort(left) + middle + quick_sort(right))
    else:
        return value


def delta_time(start_test, stop_test):
    return f'время выполнения = {stop_test - start_test}'


if __name__ == '__main__':
    m = []
    for i in range(0, 10000):
        m.append(int(random()*100))
    start_test = time.time()
    quick_sort(m)
    stop_test = time.time()
    print('алгоритм быстрой сортировки на 10000 элементах,',
          delta_time(start_test, stop_test))
