class Student:
    def __init__(self, name, course, section, favorite_ai, future_project):
        self.name = name
        self.course = course
        self.section = section
        self.favorite_ai = favorite_ai
        self.future_project = future_project

def display_student_info(student):
    print(f"Name: {student.name}")
    print(f"Course: {student.course}")
    print(f"Section: {student.section}")
    print(f"Favorite AI Technology: {student.favorite_ai}")
    print(f"Future AI Project: {student.future_project}")

if __name__ == "__main__":
    student = Student(
        name="Christine Arroyo",
        course="CSST 101",
        section="CS 3A",
        favorite_ai="Machine Learning",
        future_project="AI-Powered Tutoring System"
    )
    display_student_info(student)

