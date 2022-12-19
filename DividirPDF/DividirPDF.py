# Creado por Adrián Ramírez por medio de chat.openai.com

import tkinter as tk
import os
from tkinter import filedialog
import PyPDF2

# Crear la ventana principal
root = tk.Tk()
root.withdraw()

# Abrir la ventana de diálogo de archivos
file_path = filedialog.askopenfilename(parent=root)

# Abrir el archivo seleccionado
with open(file_path, 'rb') as file:
    # Crear un objeto PDF
    pdf = PyPDF2.PdfFileReader(file)

    # Pedir al usuario la ruta de destino y el tamaño de cada archivo de salida
    ruta_destino = filedialog.askdirectory(title="Seleccionar carpeta de destino", parent=root)
    tamaño = int(input("Creado por Adrián F. Ramírez (adrian.f.ramirez1@gmail.com)\n\nIngresa cantidad de páginas de cada archivo de salida: "))

    # Calcular cuántos archivos se deben crear
    cantidad_archivos = pdf.getNumPages() // tamaño
    if pdf.getNumPages() % tamaño > 0:
        cantidad_archivos += 1

    # Crear cada archivo
    for i in range(cantidad_archivos):
        # Calcular el rango de páginas de este archivo
        inicio = i*tamaño + 1
        fin = (i+1)*tamaño
        if fin > pdf.getNumPages():
            fin = pdf.getNumPages()

        # Crear un nuevo archivo PDF
        output_pdf = PyPDF2.PdfFileWriter()

        # Agregar cada página al nuevo archivo
        for j in range(inicio, fin+1):
            output_pdf.addPage(pdf.getPage(j-1))

        # Crear el nombre del archivo de salida
        output_name = f"rango_{inicio}_a_{fin}.pdf"

        # Crear el archivo de salida en la ruta de destino especificada
        with open(f"{ruta_destino}/{output_name}", 'wb') as output:
            output_pdf.write(output)

# Abrir la carpeta donde se encuentran los archivos
os.startfile(ruta_destino)


