import sqlite3
import csv

f=open('sample_data.csv','r') # open the csv data file
next(f, None) # skip the header row
reader = csv.reader(f)

sql = sqlite3.connect('sample_data.db')
cur = sql.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS measurements
            (TimeStamp Datetime, Pressure1 real, Pressure2 real, Pressure3 real, Temperature1 real, Temperature2 real, Temperature3 real, FlowRate real)''') # create the table if it doesn't already exist

for row in reader:
	cur.execute("INSERT INTO measurements VALUES (?, ?, ?, ?, ?, ?, ?, ?)", row)

f.close()
sql.commit()
sql.close()