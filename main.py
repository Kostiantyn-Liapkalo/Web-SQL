import sqlite3
import sys


help_message = """
Choose which request you want to perform?
0 -- Exit
1 -- Find the 5 students with the highest GPA across all subjects.
2 -- Find the student with the highest GPA in the discipline (First discipline).
3 -- Find the average score in the discipline group (Second discipline).
4 -- Find the average grade on the stream (over the entire grades table).
5 -- What courses does the teacher teach (First id=1).
6 -- List of students in the group (First group).
7 -- Evaluations of students in a separate group according to a specific discipline.
8 -- Find the average score given by the teacher in his subjects (First teacher).
9 -- Find the list of courses that the student is attending.
10 -- Find a list of courses taught by a specific teacher to a specific student.
11 -- The average score given by a specific teacher to a specific student.
12 -- Grades of students in the discipline group at the last lesson.
"""

def query_sql(file):
    
    with open(file) as f:
        sql = f.read()
        
    with sqlite3.connect('university.db') as conn:
        cursor = conn.cursor()
        cursor.execute(sql)
        return cursor.fetchall()
    
    
def main():
    
    print(help_message)
    
    while True:
        task = int(input("Select a request number: "))
        if task == 0:
            sys.exit()
        result = query_sql(f'query_{task}.sql')
        print(result)
        
        
if __name__ == '__main__':
    
    try:
        exit(main())
    except KeyboardInterrupt:
        exit()
