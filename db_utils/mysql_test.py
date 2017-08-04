import mysql_db as m

db_mysql = m.DB('tms','app2','12344321','172.25.25.17',3306)

db_mysql.execute('SELECT * from mycalendar_daylog')
cursor = db_mysql.cursor
rows = cursor.fetchall()
for row in rows:
    print row[0]
