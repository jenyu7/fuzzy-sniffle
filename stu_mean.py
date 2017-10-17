import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

command = "SELECT id FROM peeps"
identifiers = c.execute(command)
#print identifiers.fetchall()
#print identifiers.fetchall()


for stu in identifiers.fetchall():
    #print "Student:", stu[0]
    grades = c.execute("SELECT mark FROM courses WHERE " + str(stu[0]) + " = id")
    #print grades
    average = length = 0
    for mark in grades:
        #print "Mark for " + str(stu[0]) + ": " + str(mark[0])
        average += mark[0]
        length += 1
    average /= length
    #print "Average for Student " + str(stu[0]) + ": " + str(average)
    names = c.execute("SELECT name FROM peeps WHERE " + str(stu[0]) + " = id")
    for name in names:
        print "Average for student " + name[0] + " who has id " +\
                str(stu[0]) + " is " + str(average)


