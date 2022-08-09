import time


def is_even_modul(value):
    name = 'метод с использованием остатка от деления,'
    return name, value % 2 == 0


def is_even_bit_multiplication(value):
    name = 'метод с использованием оператора побитового и, '
    return name, value & 1 == 0


def is_even_bit_shift(value):
    name = 'метод с использованием оператора побитового сдвига, '
    return name, ((value >> 1) << 1 == value)


def delta_time(start_test, stop_test):
    return f'время выполнения = {stop_test - start_test}'


if __name__ == '__main__':
    start_test = time.time()
    for i in range(1, 100000000):
        result = is_even_bit_multiplication(1234564325452464654344353454355645)
    stop_test = time.time()
    print(result[0], delta_time(start_test, stop_test))

    for i in range(1, 100000000):
        result = is_even_bit_shift(1234564325452464654344353454355645)
    stop_test = time.time()
    print(result[0], delta_time(start_test, stop_test))

    for i in range(1, 100000000):
        result = is_even_modul(1234564325452464654344353454355645)
    stop_test = time.time()
    print(result[0], delta_time(start_test, stop_test))
