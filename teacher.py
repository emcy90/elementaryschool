import person


class Teacher(person):

    def __init__(self, person_id, name, birthday, course, work_hours):
        super().__init__(person_id=person_id, name=name, birthday=birthday)
        self.Course = course
        self.work_hours = work_hours

    def __str__(self):
        return self.short_string()

    def short_string(self) -> str:
        """function to return teacher-name as string"""
        return f"Teacher name {self.name}"


def working_hours():
    pass


def class_time():
    pass





