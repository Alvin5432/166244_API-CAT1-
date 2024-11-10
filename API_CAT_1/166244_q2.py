class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.assignments = {}

    def add_assignment(self, assignment_name, grade):
        self.assignments[assignment_name] = grade

    def display_grades(self):
        print(f"Grades for {self.name}:")
        for assignment, grade in self.assignments.items():
            print(f"{assignment}: {grade}")

class Instructor:
    def __init__(self, name, course_name):
        self.name = name
        self.course_name = course_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print(f"Added student {student.name} to the course {self.course_name}.")

    def assign_grade(self, student_id, assignment_name, grade):
        for student in self.students:
            if student.student_id == student_id:
                student.add_assignment(assignment_name, grade)
                print(f"Assigned grade {grade} for {assignment_name} to {student.name}.")
                return
        print(f"Student with ID {student_id} not found.")

    def display_students_and_grades(self):
        print(f"Students and grades for course {self.course_name}:")
        for student in self.students:
            print(f"Student: {student.name}")
            student.display_grades()

def main_course_management():
    instructor = Instructor("Dr. Smith", "Introduction to Python")

    while True:
        print("\nCourse Management System")
        print("1. Add a student")
        print("2. Assign a grade")
        print("3. Display all students and their grades")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            student_id = input("Enter student ID: ")
            student = Student(name, student_id)
            instructor.add_student(student)
        elif choice == "2":
            student_id = input("Enter student ID: ")
            assignment_name = input("Enter assignment name: ")
            grade = float(input("Enter grade: "))
            instructor.assign_grade(student_id, assignment_name, grade)
        elif choice == "3":
            instructor.display_students_and_grades()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_course_management()