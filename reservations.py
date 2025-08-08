import tkinter as tk
from tkinter import ttk
from database import fetch_reservations, update_reservation, delete_reservation
import home

def run_reservations_page():
    def load_data():
        for i in tree.get_children():
            tree.delete(i)
        for row in fetch_reservations():
            tree.insert("", "end", values=row)

    def edit_selected():
        selected = tree.selection()
        if not selected:
            return
        values = tree.item(selected[0], "values")

        edit = tk.Toplevel(root)
        edit.title("Edit Reservation")
        edit.geometry("400x400")

        fields = ["Name", "Flight No", "Departure", "Destination", "Date", "Seat No"]
        entries = []

        for i, label in enumerate(fields):
            ttk.Label(edit, text=label).pack(pady=5)
            entry = ttk.Entry(edit)
            entry.insert(0, values[i+1])
            entry.pack()
            entries.append(entry)

        def save():
            data = [e.get() for e in entries]
            update_reservation(values[0], *data)
            edit.destroy()
            load_data()

        ttk.Button(edit, text="Save", command=save).pack(pady=10)

    def delete_selected():
        selected = tree.selection()
        if not selected:
            return
        res_id = tree.item(selected[0], "values")[0]
        delete_reservation(res_id)
        load_data()

    root = tk.Tk()
    root.title("All Reservations")
    root.geometry("1000x550")
    root.configure(bg="#e9f5ff")

    tk.Label(root, text="📋 Reservation List", font=("Helvetica", 20, "bold"), fg="#004080", bg="#e9f5ff").pack(pady=20)

    cols = ("ID", "Name", "Flight No", "Departure", "Destination", "Date", "Seat No")
    tree = ttk.Treeview(root, columns=cols, show="headings")
    for col in cols:
        tree.heading(col, text=col)
        tree.column(col, width=120)
    tree.pack(padx=20, fill="both", expand=True)

    load_data()

    btn_frame = tk.Frame(root, bg="#e9f5ff")
    btn_frame.pack(pady=15)

    ttk.Button(btn_frame, text="✏️ Edit", command=edit_selected).grid(row=0, column=0, padx=10)
    ttk.Button(btn_frame, text="🗑️ Delete", command=delete_selected).grid(row=0, column=1, padx=10)
    ttk.Button(btn_frame, text="🔄 Refresh", command=load_data).grid(row=0, column=2, padx=10)
    ttk.Button(btn_frame, text="⬅️ Back to Home", command=lambda: [root.destroy(), home.run_home_page()]).grid(row=0, column=3, padx=10)

    root.mainloop()

