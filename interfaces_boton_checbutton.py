# -*- coding: utf-8 -*-
"""
Created on Mon May  8 09:23:27 2023

@author: Patricio Haro
"""
###########################################################
"""Entry"""
# import tkinter as tk 
# root = tk.Tk()

# root.geometry("300x200")
# label = tk.Label(root, text = "Ingresa tu nombre:")
# label.pack()

# entry = tk.Entry(root, width = 30)
# entry.pack()
# root.mainloop()

#########################################
"""Radio button"""
# import tkinter as tk 
# root = tk.Tk()
# root.geometry("300x200")

# label=tk.Label (root ,text = "Selecciona tu opcion")
# label.pack()

# var = tk.StringVar()
# var.set("opcion 1")

# def seleccionado():
#     label.config(text= f"Seleccionaste {var.get()}")

# rb1 = tk.Radiobutton(root,text ="Opcion 1", variable = var, value ="Opcion 1", command = seleccionado)
# rb1.pack()
# rb2 = tk.Radiobutton(root,text ="Opcion 2", variable = var, value ="Opcion 2", command = seleccionado)
# rb2.pack()
# root.mainloop()

######################################################
"""Checkbutton"""

# import tkinter as tk 
# root = tk.Tk()
# root.geometry("300x200")

# label = tk.Label(root ,text = "Selecciona tus opciones:")
# label.pack()

# var1 = tk.BooleanVar()
# var1.set(False)

# var2 = tk.BooleanVar()
# var2.set(False) 

# def seleccionado():
#     opciones=[]
#     if var1.get():
#         opciones.append("Opccion 1")
        
#     if var2.get():
#         opciones.append("Opccion 2")   
#     label.config(text = f"Seleccionaste {', '.join(opciones)}")
    
# cb1 = tk.Checkbutton(root, text ="Opcion 1", variable = var1, onvalue = True, offvalue = False, command = seleccionado)
# cb1.pack()    
    
# cb2 = tk.Checkbutton(root, text ="Opcion 2", variable = var2, onvalue = True, offvalue = False, command = seleccionado)
# cb2.pack()  

# root.mainloop()

#######################################################
"""Combobox"""

# import tkinter as tk
# from tkinter import ttk
# root = tk.Tk()
# root.geometry("300x200")

# label = tk.Label(root, text = "Selecciona tu opcion:")
# label.pack()

# opciones = ["Opciones 1","Opciones 2","Opciones 3"]

# combo = ttk.Combobox(root, values = opciones)
# combo.pack()

# def seleccionado(event):
#     label.config(text =f"Seleccionaste {combo.get()}")
    
# combo.bind("<<ComboboxSelected>>",seleccionado)

# root.mainloop()

###################################################
"""Menu"""
# import tkinter as tk 

# root = tk.Tk()
# root.geometry("300x200")

# def funcion_menu():
#     print("Se selecciono la opcion del menu")
    
# menu_bar = tk.Menu(root)

# menu_op = tk.Menu(menu_bar, tearoff = 0)
# menu_op.add_command(label="Opcion 1", command = funcion_menu)
# menu_op.add_command(label="Opcion 2", command = funcion_menu)
# menu_op.add_separator()
# menu_op.add_command(label="Salir", command = root.quit)

# menu_bar.add_cascade(label="Archivo", menu = menu_op)

# root.config(menu = menu_bar)
# root.mainloop()

##################################################33
"""Geometria de cuadricula en tkinter"""
# import tkinter as tk 
# root = tk.Tk()

# label1 = tk.Label(root, text = "Widget 1")
# label2 = tk.Label(root, text = "Widget 2")
# label3 = tk.Label(root, text = "Widget 3")

# label1.grid(row = 0 , column = 0)
# label2.grid(row = 1 , column = 1)
# label3.grid(row = 2 , column = 2, rowspan = 2, columnspan= 2, padx= 10, pady = 10, ipadx = 5,ipady = 5)

# root.mainloop()

####################################################################
"""Geometria de cuadricula en tkinter"""

import tkinter as tk 
root = tk.Tk()

root.grid_rowconfigure(0, weight = 1)
root.grid_rowconfigure(1, weight = 1)
root.grid_columnconfigure(0, weight = 1)
root.grid_columnconfigure(1, weight = 1)

label1 = tk.Label(root, text = "Etiqueta 1")
label1.grid(row = 0 , column = 0)

label2 = tk.Label(root, text = "Etiqueta 2")
label2.grid(row = 0 , column = 1)

boton = tk.Label(root, text = "Boton 1")
boton.grid(row = 1, column = 0)

boton1 = tk.Label(root, text = "Boton 2")
boton1.grid(row = 1, column = 1)

root.mainloop()
##################################################
from tkinter import Tk, Label, Button
class VentanaEjemplo:
    def __init__(self, master):
        self.master = master
        master.title("Una simple interfaz gráfica")
        self.etiqueta = Label(master, text="Esta es la primera ventana!")
        self.etiqueta.pack()
        self.botonSaludo = Button(master, text="Saludar", command=self.saludar)
        self.botonSaludo.pack()
        self.botonCerrar = Button(master, text="Cerrar", command=master.quit)
        self.botonCerrar.pack()
    def saludar(self):
        print("¡Hey!")
root = Tk()
miVentana = VentanaEjemplo(root)
root.mainloop()

###########################################################################

import tkinter as tk
from tkinter import ttk


class Vehiculo:
    def __init__(self):
        self.color = "Blanco"
    
    def setColor(self,newColor):
        self.color=newColor
    
    def getColor(self):
        return self.color

class Model:
    def __init__(self):
        self.auto = Vehiculo()
    def inputData(self,color):
        self.auto.setColor(color)

    def outputData(self):
        return self.auto.getColor()
        
##################################################################
class View:
    def __init__(self,root,model):
        self.root = root
        self.model = model
        self.widgets()


    def getData(self,event):
        getCombo = self.combo.get()
        self.label.config(text=getCombo)
        self.model.inputData(getCombo)
        retrievedData = self.model.outputData()
        self.label2.config(text="retrieved data: "+retrievedData)

    def widgets(self):
        self.options = ["verde","negro","amarillo"]
        self.combo = ttk.Combobox(self.root,values=self.options)
        self.combo.set("select option")
        self.combo.pack()

        self.combo.bind("<<ComboboxSelected>>",self.getData)


        self.label=ttk.Label(self.root,text = "hola")
        self.label.pack()

        self.label2=ttk.Label(self.root,text = "dato de la variable:")
        self.label2.pack()
        

##################################################################

class Controller:
    def __init__(self):
        self.root = tk.Tk()
        self.model = Model()
        self.view = View(self.root,self.model)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    control = Controller()
    control.run()







