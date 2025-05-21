import tkinter as tk
from tkinter import messagebox
from models import add_bus, get_buses, book_ticket, get_bookings

def run_gui():
    root = tk.Tk()
    root.title("Bus Ticket Booking System")
    root.geometry("600x400")

    def add_bus_gui():
        def save_bus():
            try:
                add_bus(route.get(), date.get(), time.get(), int(seats.get()))
                messagebox.showinfo("Success", "Bus Added!")
                top.destroy()
            except Exception as e:
                messagebox.showerror("Error", str(e))

        top = tk.Toplevel(root)
        top.title("Add Bus")
        tk.Label(top, text="Route").pack()
        route = tk.Entry(top)
        route.pack()
        tk.Label(top, text="Date (YYYY-MM-DD)").pack()
        date = tk.Entry(top)
        date.pack()
        tk.Label(top, text="Time (HH:MM)").pack()
        time = tk.Entry(top)
        time.pack()
        tk.Label(top, text="Seats").pack()
        seats = tk.Entry(top)
        seats.pack()
        tk.Button(top, text="Add", command=save_bus).pack()

    def book_ticket_gui():
        buses = get_buses()
        if not buses:
            messagebox.showinfo("Info", "No buses available to book.")
            return

        top = tk.Toplevel(root)
        top.title("Book Ticket")

        tk.Label(top, text="Select Bus ID").pack()
        bus_id = tk.Entry(top)
        bus_id.pack()
        tk.Label(top, text="Your Name").pack()
        name = tk.Entry(top)
        name.pack()
        tk.Label(top, text="Seats to Book").pack()
        seats = tk.Entry(top)
        seats.pack()

        def confirm_booking():
            try:
                book_ticket(int(bus_id.get()), name.get(), int(seats.get()))
                messagebox.showinfo("Success", "Ticket Booked!")
                top.destroy()
            except Exception as e:
                messagebox.showerror("Error", str(e))

        tk.Button(top, text="Book", command=confirm_booking).pack()

    def view_bookings_gui():
        bookings = get_bookings()
        top = tk.Toplevel(root)
        top.title("View Bookings")
        for booking in bookings:
            tk.Label(top, text=str(booking)).pack()

    tk.Button(root, text="Add Bus", command=add_bus_gui).pack(pady=10)
    tk.Button(root, text="Book Ticket", command=book_ticket_gui).pack(pady=10)
    tk.Button(root, text="View Bookings", command=view_bookings_gui).pack(pady=10)

    root.mainloop()
