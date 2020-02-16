import sqlite3

class Table:
    def __init__(self):
        pass

    def homes_table(self):
        conn = sqlite3.connect('houses', isolation_level=None)
        curs = conn.cursor()
        tblcmd = 'create table if not exists homes (price int(8), rooms int(3), rent int(6), addr char(50))'
        curs.execute(tblcmd)
        conn.close()

    def add_home(self, home): #home is list [price, rooms, rent, address]
        conn = sqlite3.connect('houses', isolation_level=None)
        curs = conn.cursor()
        curs.execute('INSERT INTO Homes VALUES (?, ?, ?, ?)', home)
        conn.commit()
        conn.close()

    def add_homes(self, homes): #for adding multiple homes
        conn = sqlite3.connect('houses', isolation_level=None)
        curs = conn.cursor()
        curs.executemany('INSERT INTO homes VALUES (?, ?, ?, ?)', homes)
        conn.commit()
        conn.close()

    def row_count(self):
        conn = sqlite3.connect('houses', isolation_level=None)
        curs = conn.cursor()
        curs.execute('select * from homes')
        print(curs.fetchall())
        conn.close()

    def compare_rent(self):
        conn = sqlite3.connect('houses', isolcation_level=None)
        curs = conn.cursor()
        curs.fetchall()
        curs.execute('delete form homes where rent < min_rent')
        curs.commit()
        curs.close()

    def delete_entire_table(self, password):
        if password == 'super secret password':
            conn = sqlite3.connect('houses', isolation_level=None)
            curs = conn.cursor()
            curs.execute('delete from homes')
        else:
            print('wrong password')

        

table = Table()
table.homes_table()
table.add_home([1,1,1,'123'])
table.delete_entire_table('super secret password')
table.add_home([1,1,1,'123'])
table.row_count()
