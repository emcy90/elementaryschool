from person import Person


class Admin(Person):
    '''Have following attributes
    working hours
    ...
    '''
    def __init__(self, person_id, name, birthday, work_hours):
        super().__init__(
            person_id=person_id,
            name=name,
            birthday=birthday
            )
        self.work_hours = work_hours

    def __str__(self):
        return self.short_string()

    def short_string(self) -> str:
        """function to return admin name as string"""
        return f"Student name {self.name}"
