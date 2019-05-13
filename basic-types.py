from typing import Union
from functools import reduce


def sum(*args: Union[int, float]) -> float:
    return float(reduce(lambda acc, cur: acc + cur, args))


if __name__ == '__main__':
    total = sum(1, 2.1, 3.2, 4.32, 5.432)
    print(total)
