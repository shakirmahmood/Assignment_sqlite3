import sqlite3
from xlwt import Workbook
import time

t1 = time.time()
conn = sqlite3.connect('database.db')
c = conn.cursor()

# c.execute("""CREATE TABLE employee (first text,last text,pay integer)""")
# c.execute("""CREATE TABLE employer (first text,last text,pay integer)""")
#
# c.execute("INSERT INTO employee VALUES ('Shahid','Jamil',98765)")
# c.execute("INSERT INTO employee VALUES ('Umar','Hayat',123456)")
# conn.commit()

# c.execute("INSERT INTO employer VALUES ('Shakir','Mahmood',700000)")
# c.execute("INSERT INTO employer VALUES ('Musab','Raheem',999999)")
# conn.commit()

tables = c.execute("SELECT name FROM sqlite_master WHERE type='table'")

wb = Workbook()
# sheet = [wb.add_sheet('Query 1'), wb.add_sheet('Query 2')]

sheet = []
names = []
for nam in tables:
    sheet.append(wb.add_sheet(nam[0]))
    names.append(nam[0])

k = 0
for nam in names:
    print("SELECT * FROM " + nam)
    c.execute("SELECT * FROM "+nam)

    data = c.fetchall()
    p = 0
    for i in data:
        q = 0
        for j in i:
            sheet[k].write(p, q, j)
            q += 1
        p += 1
    k += 1
    wb.save('example2.xls')

t2 = time.time()
print(t2-t1)
