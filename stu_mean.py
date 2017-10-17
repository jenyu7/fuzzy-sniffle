import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

command = "SELECT id FROM peeps"
identifiers = c.execute(command)
#print identifiers


for stu in identifiers:
    print "Student:", stu
    grades = c.execute("SELECT mark FROM courses WHERE " + str(stu[0]) + " = id")
    #print grades
    for mark in grades:
        print "Mark for" + str(stu[0]) + ":" + str(mark[0])
        '''
        average += mark
        count += 1
        '''
