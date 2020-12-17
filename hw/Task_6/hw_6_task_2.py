from collections import defaultdict
from dataclasses import dataclass
from datetime import timedelta, datetime
from typing import Optional


class DeadlineError(Exception):
    def __init__(self):
        super().__init__("You are late.")


@dataclass
class Person:
    """Create an instance of a person."""

    first_name: str
    last_name: str


class Homework:
    def __init__(self, text: str, deadline: int):
        """Create an instance of a homework."""
        self.text = text
        self.deadline = timedelta(days=deadline)
        self.created = datetime.now()

    def is_active(self) -> bool:
        """Return False if deadline is expired, True otherwise."""
        hw_deadline = self.created + self.deadline
        now = datetime.now()
        return now <= hw_deadline


class Student(Person):
    def do_homework(self, hw: Homework, solution: str) -> Optional[Homework]:
        """Raise an exception if deadline is passed, return an instance of HomeworkResult otherwise."""
        if hw.is_active():
            return HomeworkResult(self, hw, solution)
        raise DeadlineError()


class HomeworkResult:
    def __init__(self, student: Student, homework: Homework, solution: str):
        if not isinstance(homework, Homework):
            raise TypeError("You gave a not Homework object.")
        self.homework = homework
        self.solution = solution
        self.author = student
        self.created = datetime.now()


class Teacher(Person):

    homework_done = defaultdict(list)

    def create_homework(self, text: str, deadline: int) -> Homework:
        """Return an instance of created homework."""
        return Homework(text, deadline)

    def check_homework(self, hw: HomeworkResult) -> bool:
        if len(hw.solution) > 5:
            if hw not in self.homework_done[hw.homework]:
                self.homework_done[hw.homework].append(hw)
                return True

        return False

    def reset_results(hw: Optional[Homework] = None) -> None:
        if hw is None:
            Teacher.homework_done.clear()
        else:
            del Teacher.homework_done[hw]
