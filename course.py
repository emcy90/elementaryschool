"""
a collection of classes that inherit base attributes from subject-class
"""


class Course:
    """
    subject class that all other subject at the school can inherit
    attributes from which are subject_time and subject_name
    as all subjects require that
    """
    def __init__(self, course_time, course_name, course_plan, course_grading, course_schedule):
        self.course_time = course_time
        self.course_name = course_name
        self.course_plan = course_plan
        self.course_grading = course_grading
        self.course_schedule = course_schedule

    def __repr__(self):
        return f"Course(name='{self.course_name}', time='{self.course_time}')"

    def __str__(self):
        return self.short_string()

    def get_course(self) -> str:
        """Returns which course"""

    def short_string(self) -> str:
        """function to return course-name as string"""
        return f"Course name {self.course_name}"

    def long_string(self) -> str:
        """function to return course-name as string"""
        return f"Course name {self.course_name}, time {self.course_time}, plan {self.course_plan}," \
               f" grading {self.course_grading} , schedule {self.course_schedule} "
