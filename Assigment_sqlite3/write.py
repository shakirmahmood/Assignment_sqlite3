import sqlite3

conn = sqlite3.connect('employee.db')

c = conn.cursor()

# c.execute("""CREATE TABLE employee (
#             first text,
#             last text,
#             pay integer
#             )""")

# c.execute("""CREATE TABLE employee1 (
#             first text,
#              last text,
#              pay integer
#              )""")
#
# c.execute("INSERT INTO employee VALUES ('Shakir','Mahmood',70000)")
# c.execute("INSERT INTO employee VALUES ('Shakir','Mughal',70000)")
# conn.commit()

c.execute("SELECT * FROM employee1 WHERE last = 'Mahmood'")

print(c.fetchone())

c.execute("SELECT * FROM employee WHERE last = 'Mahmood'")

print(c.fetchone())

tables = c.execute("SELECT name FROM sqlite_master WHERE type='table';")

for name in tables:
    print(name[0])


conn.close()