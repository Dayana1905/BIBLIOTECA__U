import tkinter as tk
from tkinter import ttk
import requests

API_URL = "http://127.0.0.1:8000/api/"

def cargar_libros():
    response = requests.get(f"{API_URL}libros/")
    if response.status_code == 200:
        libros = response.json()
        for libro in libros:
            tree.insert("", tk.END, values=(libro['codigo'], libro['titulo'], libro['autor'], libro['genero']))

# Interfaz principal
root = tk.Tk()
root.title("Gestión de Biblioteca")

# Tabla para mostrar libros
columns = ("codigo", "titulo", "autor", "genero")
tree = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
tree.pack(fill=tk.BOTH, expand=True)

# Botón para cargar libros
btn_cargar = tk.Button(root, text="Cargar Libros", command=cargar_libros)
btn_cargar.pack()

root.mainloop()