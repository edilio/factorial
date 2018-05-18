#!/usr/bin/env python

import cProfile


# Some of the code is coming from comments at
#  https://stackoverflow.com/questions/5136447/function-for-factorial-in-python


def fact(n):
    """
    recursive
    """
    if n in [0, 1]:
        return 1
    else:
        return n * fact(n-1)


def factorial(n):
    """
    for loop implementation 0, 1 ==> 1
    """
    ret = 1
    for i in range(2, n+1):
        ret *= i
    return ret


def fact_memoization_gen():
    cache = {0: 1, 1: 1}

    def fact_memoization(n):
        ret = cache.get(n)
        if ret is None:
            ret = n * fact_memoization(n-1)
            cache[n] = ret
        return ret
    return fact_memoization


fact_memo = fact_memoization_gen()


def factorial_iterator():
    i, ret = 0, 1
    yield ret
    while True:
        i += 1
        ret *= i
        yield ret


def fact_while1(n):
    """
    using while loop based on
    :param n:
    :return:
    """
    ret = 1
    if n == 0:
        return 1
    while True:
        if n == 1:
            return ret
        n, ret = n - 1, ret * n


def fact_while2(n):
    ret = 1
    while n > 1:
        n, ret = n - 1, ret * n
    return ret


def factorial_eval(n):
    """
    # Factorials are really just a range of numbers
    # multiplied by each other.
    #
    # So this one liners:
    # 1) converts a range (1,2,3...) to a string,
    # 2) removes the leading & closing brackets, and
    # 3) then multiplies the results together using eval.
    It fails when n = 126000
    :param n:
    :return:
    """
    lst = list(range(1, n+1))
    return eval(str(lst).replace(', ', '*')[1:-1:])


# functional
import functools, operator

factorial_lambda = lambda n: functools.reduce(operator.mul, range(1, n+1), 1)


def factorial_reduce(n):
    return functools.reduce(operator.mul, range(1, n+1), 1)


def main():
    funcs = ['factorial', 'fact_while2', 'fact_while1', 'factorial_lambda', 'factorial_reduce']
    for f in funcs:
        print("### " + f)
        cProfile.run(f + '(126000)')

    print("### Results of using iterator sample")
    for i, f in zip(range(25), factorial_iterator()):
        print(i, f)


if __name__ == '__main__':
    main()
