import os
target_dir = 'C:\\TEMP\\'
os.system("mysqldump --add-drop-table -c -u username -ppassword database > "+target_dir+"database.bak.sql")