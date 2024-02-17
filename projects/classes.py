class Student:
    def __init__(self, id, name, major):
        self.id = id
        self.name = name
        self.major = major

    def __str__(self):
        return f"ID: {self.id}\nName: {self.name}\nMajor: {self.major}"