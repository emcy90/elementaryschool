"""main-file that creates the various objects needed for the project
 such as teacher, student, admin and courses
 developed using python-version 3.10"""

import sys
import time
import memory_profiler
from course import Course
from teacher import Teacher
from admin import Admin
from student import Student


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


@memory_profiler.profile
def create_courses():
    """function for creating the objects for the various courses"""
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
    # by using slots we have saved 18% memory on the course-class instance
    print("Art", sys.getsizeof(art))
    print("English", sys.getsizeof(english))
    print("Handcraft", sys.getsizeof(handcraft))
    print("Music", sys.getsizeof(music))
    print("Nature-oriented", sys.getsizeof(nature_oriented))
    print("Society-oriented", sys.getsizeof(society_oriented))
    print("Swedish", sys.getsizeof(swedish))
    print("Math", sys.getsizeof(math))
    print("Class course", sys.getsizeof(Course))


@memory_profiler.profile
def create_people():
    """function to create objects of students, teachers, admin"""
    no1 = Teacher(1, 'Ford Prefect', '880211', 4, 'art')
    no2 = Student(
        2,
        'Arthur Dent',
        '770722',
        '6',
        False,
        'A11',
        ['are', 'music'],
        ['A', 'B']
        )
    no3 = Admin(3, 'Marvin', '0', 99)

    print(no1, sys.getsizeof(no1))
    print(no2, sys.getsizeof(no2))
    print(no3, sys.getsizeof(no3))
    print('Teacher', sys.getsizeof(Teacher))
    print('Student', sys.getsizeof(Student))
    print('Admin', sys.getsizeof(Admin))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    create_courses()
    create_people()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
