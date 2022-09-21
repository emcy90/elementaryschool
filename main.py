import sys
import time
import pympler
from course import Course


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


def create_courses():
    art = Course("1h/week", "art", "teach how to do art", "A->F")
    english = Course("2h/week", "english", "teach english", "A->F")
    handcraft = Course("2h/week", "handcraft", "teach handcraft", "A->F")
    music = Course("1h/week", "music", "teach music", "A->F")
    nature_oriented = Course("2h/week", "nature-oriented", "teach biology"
                                                          ", physics and chemistry", "A->F")
    society_oriented = Course("2h/week", "society-oriented", "teach history, religion"
                                                            ", society, geography", "A->F")
    swedish = Course("4h/week", "swedish", "teach about swedish including grammar", "A->F")
    math = Course("4h/week", "mathmatics", "teach mathmatics", "A-F")
    """by using slots we have saved 18% memory on the course-class instance"""
    print("Art", sys.getsizeof(art))
    print("English", sys.getsizeof(english))
    print("Handcraft", sys.getsizeof(handcraft))
    print("Music", sys.getsizeof(music))
    print("Nature-oriented", sys.getsizeof(nature_oriented))
    print("Society-oriented", sys.getsizeof(society_oriented))
    print("Swedish", sys.getsizeof(swedish))
    print("Math", sys.getsizeof(math))
    print("Class course", sys.getsizeof(Course))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    create_courses()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
