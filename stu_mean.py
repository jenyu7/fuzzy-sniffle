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

def student_info( student, dictionary):
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
    dictionary[student[0]] = [names, avg]

def create_averages_table( dictionary ):
    '''
    Creates table with each student's id and their associated average.
    '''
    command = "CREATE TABLE peeps_avg (id INTEGER PRIMARY KEY, avg INTEGER)"
    c.execute(command)
    for student in dictionary:
        command = "INSERT INTO peeps_avg VALUES ( " +\
                str(student) + ", " + str(dictionary[student][1]) + ")"
        #print command
        c.execute(command)

def update_table():
    f = open('courses.csv')
    courses = csv.DictReader(f)
    marks = {}
    for mark in courses:
        print mark
        if marks.get(mark['id']) == None:
            marks[ mark['id'] ] = [0, 0]
        else:
            marks[ mark['id'] ][0] += int(mark['mark'])
            marks[ mark['id'] ][1] += 1
    print marks
    for mark in marks:
        if marks[mark][1] != 0:
            command = "UPDATE peeps_avg SET avg=" + str(marks[mark][0]/marks[mark][1]) +\
                    " WHERE id = " + mark
            print command
            c.execute(command)

#print_student()
command = "SELECT id FROM peeps"
ids = c.execute(command)
students = {}
for student_id in ids.fetchall():
    #calc_avg(student_id)
    student_info(student_id, students)
#print students
create_averages_table( students )
update_table()


db.commit() #save changes
db.close() #close database
