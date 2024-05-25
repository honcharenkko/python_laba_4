import customtkinter as ctk
import sqlite3

conn = sqlite3.connect('kunden.db')

cur = conn.cursor()

def print_array():
    for item, item1 in zip(my_array, my_array1):
        new_frame = ctk.CTkFrame(root, width=200)
        new_frame.pack(pady = 10)

        label = ctk.CTkLabel(new_frame, text=item, justify=ctk.LEFT)
        label.grid(row = 0, column =0, padx= (20,20))  # Вирівнюємо текст ліворуч
        label1 = ctk.CTkLabel(new_frame, text=item1, justify=ctk.LEFT)
        label1.grid(row = 0, column =1, padx= (20,20))
root = ctk.CTk()
root.title("Вивід масиву у вікно")


cur.execute("SELECT nickname from kunden")
nik = cur.fetchall()
my_array = [item[0] for item in nik]

cur.execute("SELECT password from kunden")
nik1 = cur.fetchall()
my_array1 = [item[0] for item in nik1]

button = ctk.CTkButton(root, text="Вивести масив", command=print_array)
button.pack()

root.mainloop()
