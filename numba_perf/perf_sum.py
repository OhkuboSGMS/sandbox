import time

from numba import jit
from block_timer.timer import Timer


@jit(nopython=True, cache=True)
def calc_sum_numba(max=10000):
    sum = 0
    for i in range(max):
        sum += i

    return sum


def calc_sum(max=10000):
    max_time = 10  # seconds
    start = time.perf_counter()
    sum = 0
    for i in range(max):
        sum += 1
        if (time.perf_counter() - start) > max_time:
            print('Over Time Limit')
            return 0
    return sum


def compare(max: int):
    with Timer(print_title=False) as pure_time:
        calc_sum(max)

    with Timer(print_title=False) as numba_time:
        calc_sum_numba(max)
    print('Count:', max)
    print(f'Python:{pure_time.elapsed:.7f}', ' seconds')
    print(f'Numba {numba_time.elapsed:.7f}', ' seconds')


if __name__ == '__main__':
    max = [10, 10, 1000, 100000000, 1000000000]
    for i in max:
        compare(i)
