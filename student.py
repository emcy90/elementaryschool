"""class student inherits attributes from class person"""
from person import Person


class Student(Person):
    """class student that inherits from class person attributes for person_id, name and birthday"""
    def __init__(self, person_id, name, birthday, schedule, busses, classroom, course, grade):
        super().__init__(person_id=person_id, name=name, birthday=birthday)
        self.schedule = schedule
        self.busses = busses
        self.classroom = classroom
        self.course = course
        self.grade = grade

    def __str__(self):
        return self.short_string()

    def short_string(self) -> str:
        """function to return student-name as string"""
        return f"Student name {self.name}"

    def show_schedule(self):
        """function to return student-buss as string"""
        return f"Student schedule {self.schedule}"

    def show_busses(self):
        """function to return student-name as string"""
        return f"Student busses {self.busses}"

    def show_classroom(self):
        """function to return student-busses as string"""
        return f"Student classroom {self.classroom}"

    def show_course(self):
        """function to return student-course as string"""
        return f"Student course {self.course}"

    def show_grade(self):
        """function to return student-grade as string"""
        return f"Student grade {self.grade}"
