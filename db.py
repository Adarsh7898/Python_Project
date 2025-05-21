import sqlite3

def connect_db():
    return sqlite3.connect('bus_booking.db')

def init_db():
    conn = connect_db()
    cur = conn.cursor()
    
    cur.execute('''
        CREATE TABLE IF NOT EXISTS buses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            route TEXT,
            date TEXT,
            time TEXT,
            seats INTEGER
        )
    ''')

    cur.execute('''
        CREATE TABLE IF NOT EXISTS bookings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            bus_id INTEGER,
            name TEXT,
            seats_booked INTEGER,
            FOREIGN KEY(bus_id) REFERENCES buses(id)
        )
    ''')

    conn.commit()
    conn.close()
