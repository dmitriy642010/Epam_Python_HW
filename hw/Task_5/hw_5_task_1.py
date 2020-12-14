import datetime
from typing import Optional


class Homework:
    def __init__(self, text: str, deadline: int):
        self.text = text
        self.deadline = datetime.timedelta(deadline)
        self.created = datetime.datetime.now()

    def is_active(self) -> bool:
        return self.created + self.deadline > datetime.datetime.now()


class Student:
    def __init__(self, first_name: str, last_name: str):
        self.last_name = last_name
        self.first_name = first_name

    @staticmethod
    def do_homework(homework: Homework) -> Optional[Homework]:
        if homework.is_active():
            return homework
        print("You are late")
        return None


class Teacher:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    @staticmethod
    def create_homework(text: str, deadline: int) -> Homework:
        return Homework(text, deadline)
