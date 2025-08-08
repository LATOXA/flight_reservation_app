import tkinter as tk
from tkinter import ttk
from booking import run_booking_page
from reservations import run_reservations_page

def run_home_page():
    root = tk.Tk()
    root.title("FlightMate Home")
    root.geometry("600x400")
    root.configure(bg="#e9f5ff")

    title = tk.Label(root, text="✈️ FlightMate", font=("Helvetica", 24, "bold"), fg="#004080", bg="#e9f5ff")
    title.pack(pady=40)

    btn_frame = tk.Frame(root, bg="#e9f5ff")
    btn_frame.pack(pady=20)

    ttk.Button(btn_frame, text="🛫 Book Flight", command=lambda: [root.destroy(), run_booking_page()]).grid(row=0, column=0, padx=20, ipadx=10, ipady=5)
    ttk.Button(btn_frame, text="📋 View Reservations", command=lambda: [root.destroy(), run_reservations_page()]).grid(row=0, column=1, padx=20, ipadx=10, ipady=5)

    root.mainloop()



if __name__ == "__main__":
    run_home_page()

