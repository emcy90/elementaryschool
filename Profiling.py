import functools
import profile


@functools.lru_cache(maxsize=None)
def fib_memoized(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_memoized(n - 1) + fib_memoized(n - 2)


def fib_seq_memoized(n):
    seq = []
    if n > 0:
        seq.extend(fib_seq_memoized(n - 1))
    seq.append(fib_memoized(n))
    return seq


profile.run('print(fib_seq_memoized(20)); print()')
