import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

command = "SELECT id FROM peeps"
identifiers = c.execute(command)

for stu in identifier:
    grades = c.execute("SELECT mark FROM courses WHERE " + stu + " = id")
    for mark in grades:
        average += mark
        count += 1
    
