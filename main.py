import time


def clock(n):
    """ this function creat a list of integer
    from 0 -> n after converting them to string
    as: [o, 1, 2......n] """
    return list(map(str, range(n)))


# start
t_clock_start = time.time()
# call the function
clock_time = clock(n=10000)
# end time
t_clock_end = time.time()
# print the result
modern_fun_exe_time = t_clock_end - t_clock_start
print(f'Execution time for old fashion = {modern_fun_exe_time}')


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
