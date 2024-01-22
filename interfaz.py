# interfaz.py
import tkinter as tk
from tkinter.font import Font
from tkinter import Text, Entry, Button
from tkinter.messagebox import showerror
from ecuaciones import especificarfuncion

class Interfaz:

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Criterio de Estabilidad")
        self.ventana.geometry("660x180+3+10")
        self.font_label = Font(family="Arial", size=12)

        # Atributos de Entry
        self.entry_a1 = None
        self.entry_b1 = None
        self.entry_a2 = None
        self.entry_b2 = None

        self.crear_label()
        self.crear_text()
        self.crear_entry()
        self.crear_button()
        self.crear_grafica()

    def crear_label(self):
        # Titulos principales
        titulo = tk.Label(self.ventana, text="\tSistema de ecuaciones\t\t\tEl punto crítico (0,0)", font=self.font_label)
        titulo.place(x=20, y=5)

        # el label donde se muestra la solucion
        solucion = tk.Label(self.ventana, text="Solucion", font=self.font_label)
        solucion.place(x=300, y=45)

        # el label para indicar el tipo de sistema lineal
        tipo_lb = tk.Label(self.ventana, text="Tipo" , font=self.font_label)
        tipo_lb.place(x=300, y=80)

        # Label de datos del sistema de funciones

        # para la funcion x'
        derivadax = tk.Label(self.ventana, text="x'= ", font=self.font_label)
        derivadax.place(x=30, y=45)

        # valores de x y y
        value_xx = tk.Label(self.ventana, text="x + " , font=self.font_label)
        value_xx.place(x=100, y=45)
        value_xy = tk.Label(self.ventana, text="y" , font=self.font_label)
        value_xy.place(x=170, y=45)

        # para la funcion y'
        derivaday = tk.Label(self.ventana, text="y'= ", font=self.font_label)
        derivaday.place(x=30, y=80)    
        # valores de x y y   
        value_yx = tk.Label(self.ventana, text="x + " , font=self.font_label)
        value_yx.place(x=100, y=80)
        value_yy = tk.Label(self.ventana, text="y  " , font=self.font_label)
        value_yy.place(x=170, y=80)

    def crear_text(self):
        solucion_text = Text(self.ventana, height=0.5, width=25, state="disabled")
        solucion_text.place(x=400, y=45)

        tipo_text = Text(self.ventana, height=0.5, width=25, state="disabled")
        tipo_text.place(x=400, y=85)

    def crear_entry(self):

        # Esto son los valores de la funcion de  x'
        entry_a1 = Entry(self.ventana, width=3, font=("Arial", 12))
        entry_a1.place(x=65, y=45)
        entry_b1 = Entry(self.ventana, width=3, font=("Arial", 12))
        entry_b1.place(x=135, y=45)

        # Esto son los valores de la funcion de  y'
        entry_a2 = Entry(self.ventana, width=3, font=("Arial", 12))
        entry_a2.place(x=65, y=80)
        entry_b2 = Entry(self.ventana, width=3, font=("Arial", 12))
        entry_b2.place(x=135, y=80)

    def crear_button(self):
        button_aceptar = Button(self.ventana, text="Graficar", command=self.get_data)
        button_aceptar.place(x=50, y=125)

        button_limpiar = Button(self.ventana, text="Limpiar", command= self.clean_entrys)
        button_limpiar.place(x=115, y=125)

    def get_data(self):
        global a1, b1, a2, b2
        try:
            a1 = float(self.entry_a1.get())
            b1 = float(self.entry_b1.get())
            a2 = float(self.entry_a2.get())
            b2 = float(self.entry_b2.get())

            especificarfuncion(a1, b1, a2, b2, self.solucion_text, self.tipo_text)  # Llamar a la función y pasar los valores ingresados
        except ValueError:
            showerror("Error", "Ingresa valores numéricos válidos.")
# resolver lo de guardar y
    def clean_entrys(self):
        self.entry_a1.delete(0, 'end')
        self.entry_a2.delete(0, 'end')
        self.entry_b1.delete(0, 'end')
        self.entry_b2.delete(0, 'end')
    

    def crear_grafica(self):
        print("Futura grafica")

    def iniciar(self):
        self.ventana.mainloop()  # Iniciar el bucle principal de eventos