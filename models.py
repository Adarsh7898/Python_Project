from db import connect_db

def add_bus(route, date, time, seats):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO buses (route, date, time, seats) VALUES (?, ?, ?, ?)",
                (route, date, time, seats))
    conn.commit()
    conn.close()

def get_buses():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM buses")
    buses = cur.fetchall()
    conn.close()
    return buses

def book_ticket(bus_id, name, seats):
    conn = connect_db()
    cur = conn.cursor()
    # Check available seats before booking
    cur.execute("SELECT seats FROM buses WHERE id = ?", (bus_id,))
    available_seats = cur.fetchone()
    if not available_seats:
        conn.close()
        raise ValueError("Bus ID not found")
    if available_seats[0] < seats:
        conn.close()
        raise ValueError("Not enough seats available")
    # Insert booking
    cur.execute("INSERT INTO bookings (bus_id, name, seats_booked) VALUES (?, ?, ?)",
                (bus_id, name, seats))
    # Update seats
    cur.execute("UPDATE buses SET seats = seats - ? WHERE id = ?", (seats, bus_id))
    conn.commit()
    conn.close()

def get_bookings():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM bookings")
    bookings = cur.fetchall()
    conn.close()
    return bookings
