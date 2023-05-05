# -*- coding: utf-8 -*-
"""
Created on Fri May  5 09:37:12 2023

@author: lab
"""
from tkinter import *
import tkinter as tk
# ventana = tk.Tk()
# ventana.geometry("500x500")
# ventana.title("mi primera ventana")
# ventana.mainloop()
######################################
root = tk.Tk()
root.geometry("500x500")
root.title("Prgramacion")

boton = tk.Button(root,text= "haz clic aqui")
boton.pack()
boton1 = tk.Button(root,text = "Menu")
boton1.pack()
boton2 = tk.Button(root,text = "salir",command=root.destroy) #
boton2.pack()

marco = tk.Frame(root)
marco.pack()

boton3 = tk.Button(marco,text = "Boton 1").pack(side = tk.LEFT)
boton4 = tk.Button(marco,text = "Boton 2")
boton4.pack(side = tk.RIGHT)
############################################
def clic():
    print("Haz clik en el boton")

boton5 = tk.Button(root,text= "haz clic aqui.......",command = clic)
boton5.pack()

"""cuadro de texto"""

cuadro_texto = tk.Entry(root)
cuadro_texto.pack()

"""etiqueta"""

etiqueta = tk.Label(root,text="hola Olger!")
etiqueta.pack()

"""lista"""

elemento = ["Elemento 1","Elemento 2","Elemento 3"]
lista = tk.Listbox(root)
for elemento in elemento:
    lista.insert(tk.END,elemento)
    
lista.pack()
    
def abrir_ventana():
    ventana_emergente = tk.Toplevel(root)
    etiqueta1 = tk.Label(ventana_emergente,text ="Esta es una ventana emergente!")
    etiqueta1 =pack()
    
boton6 = tk.Button(marco, text="Abrir ventana emergente",command = abrir_ventana)
boton6.pack()

    
def obtener_texto():
    ventana_emergente1 = tk.Toplevel(root)
    etiqueta3 = tk.Label(ventana_emergente1,text ="Esta es una ventana emergente!")
    etiqueta3 =pack()
    
boton8 = tk.Button(marco, text="obtener texto",command = abrir_ventana)
boton8.pack()





















root.mainloop()