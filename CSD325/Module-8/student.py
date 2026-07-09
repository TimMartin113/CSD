"""
Student Management System
This module provides functions to manage student records, including loading, printing, 
and saving student data in JSON format.
Author: Tj Martin
"""

import json

STUDENT_FILE = 'CSD325/Module-8/Student.json'


def load_students(filename=STUDENT_FILE):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f'File "{filename}" not found. Starting with an empty student list.')
        return []
    except json.JSONDecodeError:
        print(f'File "{filename}" contains invalid JSON. Starting with an empty student list.')
        return []


def print_students(students):
    for student in students:
        last = student.get('L_Name', '')
        first = student.get('F_Name', '')
        student_id = student.get('Student_ID', '')
        email = student.get('Email', '')
        print(f'{last}, {first} : ID = {student_id} , Email = {email}')


def save_students(students, filename=STUDENT_FILE):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(students, file, indent=4)


def main():
    students = load_students()
    print('\nOriginal Student list:')
    print("-" * 45)
    print_students(students)

    new_student = {
        'L_Name': 'Martin',
        'F_Name': 'TJ',
        'Student_ID': '98765',
        'Email': 'tjmartin@example.com'
    }
    students.append(new_student)

    print('\nUpdated Student list:')
    print("-" * 45)
    print_students(students)

    save_students(students)
    print('\nThe student.json file was updated.')


if __name__ == '__main__':
    main()
