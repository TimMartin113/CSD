#CSD 205 Assignment 9.2
# Author: Timothy Martin
# Date: 05/06/26

# --- Class Creation ---

class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.total_points = 0
        self.total_credits = 0

    def add_course(self, credits, grade):
        grade_map = {'A': 4, 'B': 3, 'C': 2, 'D': 1, 'F': 0}
        points = grade_map.get(grade, 0) 
        self.total_points += points * credits
        self.total_credits += credits

    def calculate_gpa(self):
        if self.total_credits == 0:
            return 0
        return self.total_points / self.total_credits

    def display_gpa(self):
        gpa = self.calculate_gpa()
        print(f"\nStudent: {self.first_name} {self.last_name}")
        print(f"Cumulative GPA: {gpa:.2f}")


# --- Main Program ---

# Get student name
first = input("Enter student's first name: ")
last = input("Enter student's last name: ")

# Create student object
student = Student(first, last)

# Loop for courses
while True:
    credits = float(input("Enter course credits: "))
    grade = input("Enter grade (A, B, C, D, F): ").upper()

    student.add_course(credits, grade)

    cont = input("Add another course? (y/n): ").lower()
    if cont != 'y':
        break

# Display GPA
student.display_gpa()