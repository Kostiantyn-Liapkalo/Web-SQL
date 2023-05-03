from datetime import datetime
import faker
from faker import providers
from random import randint, choice
import sqlite3

fake_data = faker.Faker(locale='uk_UA')


def create_db():
    
    with open('create_tables.sql', 'r') as f:
        sql = f.read()

    with sqlite3.connect('university.db') as connect:
        cur = connect.cursor()
        cur.executescript(sql)


def prepare_data() -> tuple():
    
    number_students = 30
    number_groups = 3
    number_subjects = 8
    number_teachers = 5
    number_grades = 150

    for_groups = []

    for _ in range(number_groups):
        for_groups.append((fake_data.bothify(text='Group ?#'),))

    for_students = []

    for _ in range(number_students):
        name = fake_data.name()
        *_, firstname, lastname = name.split(' ')
        for_students.append((name, firstname, lastname, randint(1, len(for_groups))))

    for_teachers = []

    for _ in range(number_teachers):
        name = fake_data.name()
        *_, firstname, lastname = name.split(' ')
        for_teachers.append((name, firstname, lastname))

    for_subjects = []

    for _ in range(number_subjects):
        for_subjects.append((fake_data.job(), randint(1, len(for_teachers))))

    for_grades = []

    for _ in range(number_grades):
        for_grades.append((randint(4, 12), randint(1, len(for_students)), randint(1, len(for_subjects)),
                           fake_data.date_between_dates(datetime(2022, 1, 1), datetime(2022, 12, 31))))

    return for_students, for_groups, for_subjects, for_teachers, for_grades


def insert_data_to_db(students, groups, subjects, teachers, grades) -> None:
    
    with sqlite3.connect('university.db') as connect:
        cur = connect.cursor()

        sql_to_students = """INSERT INTO students(fullname, firstname, lastname, group_id)
                               VALUES (?, ?, ?, ?)"""
        cur.executemany(sql_to_students, students)

        sql_to_groups = """INSERT INTO groups(name)
                               VALUES (?)"""
        cur.executemany(sql_to_groups, groups)

        sql_to_subjects = """INSERT INTO subjects(name, teacher_id)
                              VALUES (?, ?)"""
        cur.executemany(sql_to_subjects, subjects)

        sql_to_teachers = """INSERT INTO teachers(fullname, firstname, lastname)
                              VALUES (?, ?, ?)"""
        cur.executemany(sql_to_teachers, teachers)

        sql_to_grades = """INSERT INTO grades(grade, student_id, subject_id, date_of)
                              VALUES (?, ?, ?, ?)"""
        cur.executemany(sql_to_grades, grades)

        connect.commit()


if __name__ == "__main__":
    
    create_db()
    
    students, groups, subjects, teachers, grades = prepare_data()
    
    insert_data_to_db(students, groups, subjects, teachers, grades)