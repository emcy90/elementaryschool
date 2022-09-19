"""
Class for persons at school which includes but not limited to teachers, administrators and students
"""

class Person:
    """class with attributes person_id and name and birthday which is shared by all"""
    def __init__(self, person_id, name, birthday):
        self.person_id = person_id
        self.name = name
        self.birthday = birthday
