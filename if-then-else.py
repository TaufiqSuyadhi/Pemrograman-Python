import tkinter as tk
from tkinter import ttk

# 1. Buat form

root = tk.Tk()
root.title('Kondisi Percabangan')

"""
root.geometry("600x400+50+50")

------------------------------------------------------------------------
---------------- Atur letak posisi form di tengah layar ----------------
------------------------------------------------------------------------
"""
window_width = 300
window_height = 200

# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

#variabel awal input date
input = tk.StringVar()
hasil = tk.StringVar()

# 2. Buat Sign in frame
#buat frame
signin = ttk.Frame(root)
signin.pack(padx=10, pady=10, fill='x', expand=True)

#buat label
input_label = ttk.Label(signin, text="Input Data :")
input_label.pack(fill='x', expand=True)
#buat input data
input_entry = ttk.Entry(signin, textvariable=input)
input_entry.pack(fill='x', expand=True)
input_entry.focus()
#buat label
hasil_label = ttk.Label(signin, text="Keterangan :")
hasil_label.pack(fill='x', expand=True)
#buat input data
hasil_entry = ttk.Entry(signin, textvariable=hasil)
hasil_entry.pack(fill='x', expand=True)

#3.Proses
def clear_form():
    input_entry.delete(0, tk.END)
    input_entry.insert(0, '')
    hasil_entry.delete(0, tk.END)
    hasil_entry.insert(0, '')
    hasil_entry.configure(state="readonly")

def proses_click():
    input_nilai = input_entry.get()
    if (input_nilai == "Pascal"):
        ket = "Low level langguage"
    elif(input_nilai == "C++"):
        ket = "Midle level langguage"
    elif(input_nilai == "Delphi"):
        ket = "Visual langguage"
    elif(input_nilai == "Oracle"):
        ket = "Database software"
    elif(input_nilai == "Ansaf"):
        ket = "Anti virus"
    else:
        ket = "Tool Software"
    hasil_entry.configure(state='')
    hasil_entry.delete(0, tk.END)
    hasil_entry.insert(0, ket)
    hasil_entry.configure(state="readonly")

def keluar():
    root.destroy()

#4.Bersihkan form input data
clear_form()

#buat tombol proses
proses_button = ttk.Button(signin, text='Proses', command=proses_click)
proses_button.pack(fill='x', expand=True, pady=10)
#buat tombol keluar
keluar_button = ttk.Button(signin, text='Keluar', command=keluar)
keluar_button.pack(fill='x', expand=True, pady=10)

root.mainloop()