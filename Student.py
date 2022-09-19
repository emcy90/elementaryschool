import Person

class Student(Person):
    def __init__(self, person_id, name, birthday):
        super().__init__(person_id=person_id, name=name, birthday=birthday)
