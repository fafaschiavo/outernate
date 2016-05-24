import csv
import os
import mysql.connector

csvfile = open('SKILL TREE.xlsx - Final.csv')
st = csv.reader(csvfile, delimiter=',')
dic=[]

for row in st:
    if row[1]:
        #print (row)
        dic.append(row)

#print (dic)

seen = []
repeat =[]
for row in dic: 
	row[1]=row[1].title()
	if row[1] in seen: 
		repeat.append(row)
	
	#print(row)
	seen.append(row[1])

#.title() 

cnx = mysql.connector.connect(user='root',password='root', database='outernate_life')
cursor = cnx.cursor()

#print (seen)
print (dic)
print (repeat)
for row in dic:
	sql_command = """INSERT INTO members_skills (
		id, skill_name, father_id)
    	VALUES (""" + row[0] + """,'"""+row[1]+"""',"""+row[2]+""");"""
	print sql_command
	cursor.execute(sql_command)



# sql_command = """INSERT INTO members_skills (
# 	id, skill_name, father_id)
#     VALUES (""" + row[0] + """,'"""+row[1]+"""',"""+row[2]+""");"""

# sql_command = """INSERT INTO members_skills (
# 	id, skill_name, father_id)
#     VALUES (1, 'soma', 0);"""
# cursor.execute(sql_command)


# Make sure data is committed to the database
cnx.commit()

cursor.close()
cnx.close()