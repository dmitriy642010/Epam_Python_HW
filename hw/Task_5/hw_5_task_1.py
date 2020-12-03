from datetime import timedelta, datetime
from dataclasses import dataclass


@dataclass()
class Homework:
    text: str
    created: datetime.now()
    deadline: int = timedelta()

    @classmethod
    def is_active(cls) -> bool:
        w_deadline = cls.created + cls.deadline
        now = datetime.now()
        return not now > w_deadline


@dataclass(order=True)
class Student:
    first_name: str
    last_name: str

    @staticmethod
    def do_homework(task=Homework):
        if task.is_active() is False:
            print("You are late")
            return None
        return task


@dataclass(order=True)
class Teacher:
    first_name: str
    last_name: str

    @staticmethod
    def create_homework(text: str, deadline):
        return Homework(text, deadline)
