import MySQLdb
class DB(object):
    '''
	 cursor_type: 0- Normal  1- DictCursor
     '''
    def __init__(self,p_dbname,puser,ppasswd,phost='',pport=0, cursor_type=0):
        self.conn = MySQLdb.connect(host=phost,user=puser,passwd= ppasswd,port=pport,db=p_dbname,charset= 'utf8')
        self.cursor = None
        if cursor_type == 0:
            self.cursor = self.conn.cursor()
        else:
            self.cursor = self.conn.cursor(MySQLdb.cursors.DictCursor)
					
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
            # self.conn.query(command)
            self.cursor.execute(command)
        else:
            # self.conn.query(command,params)
            self.cursor.execute(command,params)  
        
        return self.cursor
