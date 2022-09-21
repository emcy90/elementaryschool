"""
class for all objects that are courses at the school
"""


class Course:
    """
    course class and each course is an object of the class. Entire
     class-structure for the courses should be in slot as they are not edited
    """
    __slots__ = ('course_time', 'course_name', 'course_plan', 'course_grading')

    def __init__(self, course_time, course_name, course_plan, course_grading):
        self.course_time = course_time
        self.course_name = course_name
        self.course_plan = course_plan
        self.course_grading = course_grading

    def __repr__(self):
        return f"Course(name='{self.course_name}', time='{self.course_time}')"

    def __str__(self):
        return self.short_string()

    def get_course(self) -> str:
        """Returns which course"""
        return self.course_name

    def short_string(self) -> str:
        """function to return course-name as string"""
        return f"Course name {self.course_name}"

    def long_string(self) -> str:
        """function to return course-name as string"""
        return f"Course name {self.course_name}, time {self.course_time}, plan" \
               f" {self.course_plan}, grading {self.course_grading}"
