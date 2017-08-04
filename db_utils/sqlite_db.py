import sqlite3
class DB(object):
    def __init__(self,conn_str):
        self.conn_str = conn_str
        self.conn = sqlite3.connect(conn_str)
        self.cursor = self.conn.cursor()
    def commit(self):
        self.conn.commit()
    def close(self):
        self.cursor.close()
    def execute(self,command,params=None):
        '''
            command : sql command to execute (use ? for parametric commands)
                like INSERT INTO skl_desc VALUES (null, ?, ?, ?, ?, ?)
            params  : tuple of parameters to use on sql command
        '''
        # INSERT INTO skl_desc
        # VALUES (null, ?, ?, ?, ?, ?)
        # '''
        # t = (parent,
        # row[1],
        # unicode(row[4].strip(), 'utf8'),
        # unicode(row[2].strip(), 'utf8'),
        # rValue)

        if params == None:
            self.cursor.execute(command)
        else:
            self.cursor.execute(command,params)  
        
        return self.cursor