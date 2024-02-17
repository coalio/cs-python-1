from .classes import Student

# Lets create three students
students = [
    Student(1, "Juan", "Ing. Civ"),
    Student(2, "Jose", "Ing. Sist"),
    Student(3, "Julio", "Arquitectura")
]

# Print all of them
for student in students:
    print(student)