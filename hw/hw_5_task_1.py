from datetime import timedelta, datetime


class Homework:
    def __init__(self, text: str, deadline):
        self.text = text
        self.deadline = timedelta(deadline)
        self.created = datetime.now()

    def is_active(self) -> bool:
        w_deadline = self.created + self.deadline
        now = datetime.now()
        return not now > w_deadline


class Student:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    def do_homework(self, task: Homework):
        if task.is_active() is False:
            print("You are late")
            return None
        return task


class Teacher:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    def create_homework(self, text: str, deadline):
        return Homework(text, deadline)
