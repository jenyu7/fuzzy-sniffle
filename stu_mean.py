import sqlite3   # enable control of an sqlite database
import csv       # facilitates CSV I/O


f="discobandit.db"

db = sqlite3.connect(f) # open if f exists, otherwise create
c = db.cursor()    # facilitate db ops

# get the ids
command = "SELECT id FROM peeps"
identifiers = c.execute(command)

for stu in identifiers.fetchall():
    #print "Student:", stu[0]
    # Get the marks from courses where the id is equal to stu
    grades = c.execute("SELECT mark FROM courses WHERE " + str(stu[0]) + " = id")
    #print grades
    # calculate the average for the student
    average = length = 0
    for mark in grades:
        #print "Mark for " + str(stu[0]) + ": " + str(mark[0])
        average += mark[0]
        length += 1
    average /= length
    #print "Average for Student " + str(stu[0]) + ": " + str(average)
    # get the name of the student from their id
    names = c.execute("SELECT name FROM peeps WHERE " + str(stu[0]) + " = id")
    # Print student name, their id, and average
    for name in names.fetchall():
        print "Average for student " + name[0] + " who has id " +\
                str(stu[0]) + " is " + str(average)


