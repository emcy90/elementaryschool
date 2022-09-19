"""class student inherits attributes from class person"""
from person import Person


class Student(Person):
    """class student that inherits from class person attributes for person_id, name and birthday"""
    def __init__(self, person_id, name, birthday):
        super().__init__(person_id=person_id, name=name, birthday=birthday)

    def __str__(self):
        return self.short_string()

    def short_string(self) -> str:
        """function to return student-name as string"""
        return f"Student name {self.name}"
