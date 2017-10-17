import sqlite3   # enable control of an sqlite database
import csv       # facilitates CSV I/O


f="discobandit.db"

db = sqlite3.connect(f) # open if f exists, otherwise create
c = db.cursor()    # facilitate db ops

def find_student( id ):
    print "===============\n", id[0]
    command = "SELECT mark FROM courses WHERE " + str(id[0]) + " = id"
    student = c.execute(command)
    return student

def print_student():
    # get the ids
    command = "SELECT id FROM peeps"
    ids = c.execute(command)

    for student in ids.fetchall():
        grades = find_student(student)
        for grade in grades:
            print grade[0]




def calc_avg( student ):
    grades = find_student(student)
    average = number = 0
    for grade in grades:
        average += grade[0]
        number += 1
        average /= number
        print "Average for student id " + str(student[0]) + " is: " + str(average)

#print_student()
command = "SELECT id FROM peeps"
ids = c.execute(command)
for student in ids.fetchall():
    calc_avg(student)

