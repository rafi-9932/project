class Student:
    def __init__(self, name, current_class, id):
        self.name = name
        self.current_class = current_class
        self.id = id

    def __repr__(self) -> str:
        return f'Student(name: {self.name}, class: {self.current_class}, id: {self.id})'


class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def __repr__(self) -> str:
        return f'Teacher(name: {self.name}, subject: {self.subject})'


class School:
    def __init__(self, name) -> None:
        self.name = name
        self.teachers = []
        self.students = []

    def add_teacher(self, name, subject):
        teacher = Teacher(name, subject)
        self.teachers.append(teacher)

    def enroll(self, name, fee):
        if fee < 6500:
            return 'Not enough fee'
        else:
            id = len(self.students) + 1
            student = Student(name, 'C', id)
            self.students.append(student)
            return f'{name} is enrolled with ID: {id}, extra money: {fee - 6500}'

    def __repr__(self) -> str:
        school_repr = f'Welcome to {self.name}\n'
        school_repr += '--- Our Teachers ---\n'
        for teacher in self.teachers:
            school_repr += repr(teacher) + '\n'
        school_repr += '--- Our Students ---\n'
        for student in self.students:
            school_repr += repr(student) + '\n'
        return school_repr


# Example usage
phitron = School('Phitron')
print(phitron.enroll('Alia', 5500))  # Not enough fee
print(phitron.enroll('Rani', 8000))  # Successful enrollment
print(phitron.enroll('Aishwarya', 7000))  # Successful enrollment
print(phitron.enroll('Vaijaan', 90000))  # Successful enrollment

phitron.add_teacher('Tom Cruise', 'DS')
phitron.add_teacher('Leonardo DiCaprio', 'Algorithm')

print(phitron)
