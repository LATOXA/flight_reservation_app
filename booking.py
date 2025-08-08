import tkinter as tk
from tkinter import ttk
from database import insert_reservation, initialize_db
import home

initialize_db()

def run_booking_page():
    def show_temp_message(text, duration=3000):
        msg = tk.Label(root, text=text, bg="#d4edda", fg="#155724", font=("Arial", 12), relief="solid", bd=1)
        msg.pack(pady=10)
        root.after(duration, msg.destroy)

    def submit_booking():
        name = name_entry.get()
        flight_number = flight_number_entry.get()
        departure = departure_entry.get()
        destination = destination_entry.get()
        date = date_entry.get()
        seat_number = seat_number_entry.get()

        if not all([name, flight_number, departure, destination, date, seat_number]):
            show_temp_message("⚠️ Please fill in all fields!")
            return

        insert_reservation(name, flight_number, departure, destination, date, seat_number)
        show_temp_message(" Booking submitted successfully!")
        for e in [name_entry, flight_number_entry, departure_entry, destination_entry, date_entry, seat_number_entry]:
            e.delete(0, tk.END)

    root = tk.Tk()
    root.title("Book a Flight")
    root.geometry("600x600")
    root.configure(bg="#e9f5ff")

    title = tk.Label(root, text="Book Your Flight", font=("Helvetica", 24, "bold"), fg="#004080", bg="#e9f5ff")
    title.pack(pady=20)

    form = tk.Frame(root, bg="white", bd=2, relief="groove")
    form.pack(padx=20, pady=10, fill="both")

    def create_field(label):
        frame = ttk.Frame(form)
        frame.pack(pady=8, padx=20, fill="x")
        ttk.Label(frame, text=label, width=15).pack(side="left")
        entry = ttk.Entry(frame)
        entry.pack(side="left", fill="x", expand=True)
        return entry

    name_entry = create_field("Name:")
    flight_number_entry = create_field("Flight No:")
    departure_entry = create_field("Departure:")
    destination_entry = create_field("Destination:")
    date_entry = create_field("Date:")
    seat_number_entry = create_field("Seat No:")

    submit_button = ttk.Button(root, text="Book Now", command=submit_booking)
    submit_button.pack(pady=20)

    ttk.Button(root, text="⬅️ Back to Home", command=lambda: [root.destroy(), home.run_home_page()]).pack(pady=10)

    name_entry.bind("<Return>", lambda e: flight_number_entry.focus_set())
    flight_number_entry.bind("<Return>", lambda e: departure_entry.focus_set())
    departure_entry.bind("<Return>", lambda e: destination_entry.focus_set())
    destination_entry.bind("<Return>", lambda e: date_entry.focus_set())
    date_entry.bind("<Return>", lambda e: seat_number_entry.focus_set())
    seat_number_entry.bind("<Return>", lambda e: submit_button.focus_set())

    root.mainloop()


