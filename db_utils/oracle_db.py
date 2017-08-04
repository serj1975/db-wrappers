import cx_Oracle
import os
    
class DB(object):
    def __init__(self,conn_str):
        '''
        conn_str will be as:
        user/pass@host/sid
        'pythonhol/welcome@127.0.0.1/orcl'
        '''
        os.environ["NLS_LANG"] = ".UTF8"
        self.conn_str = (conn_str)
        self.connection = cx_Oracle.connect(self.conn_str)
        self.cursor = self.connection.cursor()
        
    def close(self):
        self.cursor.close()
        self.connection.close()
        
    def commit(self):
        self.connection.commit()
        
    def execute(self,command,params=None):
        if params == None:
            self.cursor.execute(command)
        else:
            self.cursor.execute(command,params)  
        
        return self.cursor

        