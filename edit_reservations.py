import tkinter as tk
from tkinter import ttk
from database import update_reservation

def open_edit_window(reservation, refresh_callback):
    edit = tk.Toplevel()
    edit.title("Edit Reservation")
    edit.geometry("400x400")

    fields = ["Name", "Flight No", "Departure", "Destination", "Date", "Seat No"]
    entries = []

    for i, label in enumerate(fields):
        ttk.Label(edit, text=label).pack(pady=5)
        entry = ttk.Entry(edit)
        entry.insert(0, reservation[i+1])
        entry.pack()
        entries.append(entry)

    def save():
        data = [e.get() for e in entries]
        update_reservation(reservation[0], *data)
        edit.destroy()
        refresh_callback()

    ttk.Button(edit, text="Save", command=save).pack(pady=10)
