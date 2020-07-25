import sqlite3
import datetime
from openpyxl import Workbook
from openpyxl.styles import Font 

now= datetime.datetime.now()

def report():
	conn = sqlite3.connect("Attendance.db")
	cursor = conn.cursor()
	temp=("('"+now.strftime("%Y-%m-%d")+"',)")
	
	cursor.execute("""   SELECT ID, name, TT from Employee where DD=(?);         """,(now.strftime("%Y-%m-%d"),))
	data=cursor.fetchall()

	conn.commit()
	cursor.close()
	conn.close()
	return data

def write_to_excel(ids):
    wb = Workbook()
    sh = wb.active
   
    col1_name = 'ID'
    col2_name = 'Name'
    col3_name = 'Time'
    
    columns = ['ID', 'Name', 'Time']
    sh.append(columns)
    cell1=sh['A1']
    cell2=sh['B1']
    cell3=sh['C1']

    cell1.font = Font(bold = True)
    cell2.font = Font(bold = True)
    cell3.font = Font(bold = True)

    for r in ids:
    	sh.append(r)
    wb.save('attendance_files/'+'attendance'+str(now.strftime("%Y-%m-%d"))+'.xlsx')

ids=report()
print(ids)
write_to_excel(ids) 






