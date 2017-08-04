import pyodbc as p
class DB(object):
    def __init__(self,server,database,user,password):
        self.conn_str = ( r'DRIVER={SQL Server};SERVER=' +
            server + ';DATABASE=' + database +
            ';UID=' + user + ';PWD='+password)
        self.connection = p.connect(self.conn_str)
        self.cursor = self.connection.cursor()
        
    def close(self):
        self.cursor.close()
        self.connection.close()
        
    def commit(self):
        self.conn.commit()
        
    def execute(self,command,params=None):
        if params == None:
            self.cursor.execute(command)
        else:
            self.cursor.execute(command,params)  
        
        return self.cursor

        