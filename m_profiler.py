import memory_profiler


@memory_profiler.profile
def test_func():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    addition = 0

    for num in numbers:
        addition += num

    return addition


test_func()
