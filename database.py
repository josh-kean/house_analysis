import sqlite3

class Table:
    def __init__(self):
        self.table = None
        pass

    def homes_table(self):
        conn, curs = self.start_table()
        tblcmd = 'create table if not exists homes (price int(8), rooms int(3), estrent int(6), addr char(50), min_rent int(6))'
        curs.execute(tblcmd)
        conn.close()

    def start_table(self):
        self.homes_table()
        conn = sqlite3.connect('house', isolation_level=None)
        curs = conn.cursor()
        return conn, curs

    def add_home(self, home): #home is list [price, rooms, rent, address]
        conn = sqlite3.connect('house', isolation_level=None)
        curs = conn.cursor()
        curs.execute('INSERT INTO homes (price, rooms, estrent, addr) VALUES (?, ?, ?, ?)', home)
        conn.commit()
        conn.close()

    def add_homes(self, homes): #for adding multiple homes
        conn, curs = self.start_table()
        curs.executemany('INSERT INTO homes VALUES (?, ?, ?, ?)', homes)
        conn.commit()
        conn.close()

    def add_min_rent(self, min_rent, address):
        conn = sqlite3.connect('house', isolation_level=None)
        curs = conn.cursor()
        curs.execute('UPDATE homes SET min_rent=(?) WHERE addr=(?)', (min_rent, address))

    def add_cash_on_cash(self, coc, address):
        conn = sqlite3.connect('house', isolation_level=None)
        curs = conn.cursor()
        curs.execute('UPDATE homes SET cash_on_cash=(?) WHERE addr=(?)', (coc, address))

    def get_table(self):
        conn = sqlite3.connect('house', isolation_level=None)
        curs = conn.cursor()
        curs.execute('select * from homes')
        homes = curs.fetchall()
        conn.close()
        return homes

    def compare_rent(self):
        conn = sqlite3.connect('house', isolation_level=None)
        curs = conn.cursor()
        curs.fetchall()
        curs.execute('delete from homes where rent < min_rent')
        curs.commit()
        curs.close()

    def filter_by_coc(self, coc=.1): #remove anything less than current coc
        conn = sqlite3.connect('house', isolation_level=None)
        curs = conn.cursor()
        curs.execute('DELETE FROM homes where cash_on_cash < .1')


    def delete_entire_table(self, password):
        if password == 'super secret password':
            conn, curs = self.start_table()
            curs.execute('delete from homes')
        else:
            print('wrong password')

        

