class Empty:
    pass


class Person:
    def __init__(self):
        self.firstname = ""
        self.lastname = ""
        self.age = 0


class Student:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age