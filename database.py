import sqlite3

class Table:
    def __init__(self):
        self.table = None
        pass

    def homes_table(self):
        conn = sqlite3.connect('house', isolation_level=None)
        curs = conn.cursor()
        tblcmd = 'create table if not exists homes (price int(8), cash_on_cash int(4), rooms int(3), estrent int(6), addr char(50), min_rent int(6), property_tax int(6))'
        curs.execute(tblcmd)
        conn.close()

    def add_home(self, home): #home is list [price, rooms, rent, address, property_tax]
        conn = sqlite3.connect('house', isolation_level=None)
        curs = conn.cursor()
        curs.execute('INSERT INTO homes (price, rooms, estrent, addr, property_tax) VALUES (?, ?, ?, ?, ?)', home)
        conn.commit()
        conn.close()

    def add_homes(self, homes): #for adding multiple homes
        conn = sqlite3.connect('house', isolation_level=None)
        curs = conn.cursor()
        curs.executemany('INSERT INTO homes VALUES (?, ?, ?, ?, ?)', homes)
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
        conn.close()

    def filter_by_coc(self, coc=.1): #remove anything less than current coc
        conn = sqlite3.connect('house', isolation_level=None)
        curs = conn.cursor()
        curs.execute('DELETE FROM homes where cash_on_cash < .1')
        conn.close()

    def filter_by_price(self, coc=.1): #remove anything less than current coc
        conn = sqlite3.connect('house', isolation_level=None)
        curs = conn.cursor()
        curs.execute('DELETE FROM homes where price < 50000')
        conn.close()

    def filter_by_city(self, city=None):
        conn = sqlite3.connect('house', isolation_level=None)
        curs = conn.cursor()
        if city:
            command = f'SELECT distinct * FROM homes where addr like "%{city}%" ORDER BY cash_on_cash, price'
        else:
            command = f'SELECT distinct * FROM homes ORDER BY cash_on_cash, price'
        homes = curs.execute(command)
        return homes

    def filter_all(self, city=None, coc=None, finance=None):
        conn = sqlite3.connect('house', isolation_level=None)
        curs = conn.cursor()
        cityCheck = lambda x: f'addr like "%{x}%" ' else ''
        cocCheck = lambda x: f'coc < {x} ' else ''
        financeCheck = lambda x: f'finance < profit ' else ''
        finalCheck = lambda x, y, z: 'where ' if x or y or z else ''
        command = f'SELECT distinct * from homes {finalCheck(city, cic, finance}{cityCheck(city)}{cocCheck(coc)}{financeCheck(finance)} ORDER BY cash_on_cash, price'
        homes = curs.execute(command)

    def delete_entire_table(self, password):
        if password == 'super secret password':
            conn = sqlite3.connect('house', isolation_level=None)
            curs = conn.cursor()
            curs.execute('delete from homes')
            conn.commit()
            conn.close()
        else:
            print('wrong password')

        

