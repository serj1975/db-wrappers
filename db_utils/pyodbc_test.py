import pyodbc_db as p
from django.utils.encoding import smart_str,smart_unicode

# server = 'idns.irisad.net\\mssql1'
# server = '172.25.25.17'
# database = 'GS'
# user = 'app'
# password = '12344321'
# table = 'employee'

# connStr = ( r'DRIVER={SQL Server};SERVER=' +
            # server + ';DATABASE=' + database + ';' +
            # 'Trusted_Connection=yes'    )
# connStr = ( r'DRIVER={SQL Server};SERVER=' +
            # server + ';DATABASE=' + database +
            # ';UID=' + user + ';PWD='+password    )
        
# conn = p.connect(connStr)
# dbCursor = conn.cursor()
# sql = ('select * from '
       # + table)
# dbCursor = conn.cursor()
# dbCursor.execute(sql)
# for row in dbCursor:
    # print smart_str("%s %s %s" %(row[0], row[1],row[2]))
        
# conn.close()

# db = p.DB('172.25.25.17','GS','sa','49991')
# cursor = db.execute('select * from employee')
db = p.DB('.\sqlexpress','msc_sem','sa','1234')
cursor = db.execute('select MeasureCatalogId,MeasureName from SEM.tblMeasureCatalog')
rows = cursor.fetchall()
n = len(rows[0])
for row in rows:
    for i in range(0,n):
        print smart_str(row[i]) + '\t\t',
    print '\n'
db.close()