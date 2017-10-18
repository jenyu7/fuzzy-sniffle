import sqlite3   # enable control of an sqlite database
import csv       # facilitates CSV I/O


f="discobandit.db"

db = sqlite3.connect(f) # open if f exists, otherwise create
c = db.cursor()    # facilitate db ops

def find_student( id ):
    '''
    Returns cursor object for marks from courses of student with id 'id'.
    '''
    #print "===============\n", id[0]
    command = "SELECT mark FROM courses WHERE " + str(id[0]) + " = id"
    student = c.execute(command)
    return student

def print_students():
    '''
    Prints all student info.
    '''
    # get the ids
    command = "SELECT id FROM peeps"
    ids = c.execute(command)

    for student in ids.fetchall():
        grades = find_student(student)
        for grade in grades:
            print grade[0]


def calc_avg( student ):
    '''
    Calculates average for a given student.
    '''
    grades = find_student(student)
    average = number = 0
    for grade in grades:
        average += grade[0]
        number += 1
    average /= number
    #print "Average for student id " + str(student[0]) + " is: " + str(average)
    return average

students = {}
def student_info( student ):
    '''
    Populates dictionary students with students id as the key and and array as the value.

    The array that is the value holds the name of the student and their average.
    '''
    avg = calc_avg(student)
    command = "SELECT name FROM peeps WHERE " + str(student[0]) + "=id"
    names = c.execute(command)
    for name in names:
        names = name[0]
    print names + " with id " + str(student[0]) + " has average: " + str(avg)
    students[student[0]] = [names, avg]

#print_student()
command = "SELECT id FROM peeps"
ids = c.execute(command)
for student_id in ids.fetchall():
    #calc_avg(student_id)
    student_info(student_id)

print students

