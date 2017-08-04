import oracle_db as p
from django.utils.encoding import smart_str,smart_unicode

db = p.DB('SCOTT/tiger@127.0.0.1/XE')
cursor = db.execute('select * from dept')
rows = cursor.fetchall()
n = len(rows[0])
for row in rows:
    for i in range(0,n):
        print smart_str(row[i]) + '\t\t',
    print '\n'
db.close()