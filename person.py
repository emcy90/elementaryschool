from dataclasses import dataclass
from typing import Optional
from course import Course


@dataclass
class Person:
    """Person at the elementary school."""

    name: str
    person_id: int
    birthday: str
    course: Optional[Course] = None

    def courses(self) -> str:
        """which person is specific course."""
        witch_course = self.course.get_course()
        if self.course is not None:
            return witch_course
