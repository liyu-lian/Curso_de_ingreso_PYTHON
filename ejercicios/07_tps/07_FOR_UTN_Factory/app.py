'''
Juliana Gimena Grajeda

UTN Software Factory está en la búsqueda de programadores para incorporar a su equipo de 
trabajo. En las próximas semanas se realizará un exhaustivo proceso de selección. Para ello se 
ingresarán los siguientes datos de los 10 postulantes para luego establecer distintas métricas 
necesarias para tomar decisiones a la hora de la selección:

Nombre
Edad (mayor de edad)
Género (F-M-NB)
Tecnología (PYTHON - JS - ASP.NET)
Puesto (Jr - Ssr - Sr)

Informar por pantalla:
a. Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS 
cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr.
b. Nombre del postulante Jr con menor edad.
c. Promedio de edades por género.
d. Tecnologia con mas postulantes (solo hay una).
e. Porcentaje de postulantes de cada genero.

Todos los datos se ingresan por prompt y los resultados se muestran por consola (print)

'''
import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        nombre_ingresado = prompt(title="Inserción de datos", prompt="Ingrese el nombre del postulante")

        while nombre_ingresado.isdigit(): #while not nombre_ingresado.isalpha()
            nombre_ingresado = prompt(title="Inserción de datos", prompt="ERROR. Ingrese el nombre del postulante")

        edad_ingresada = prompt(title="Inserción de datos", prompt=" Ingrese su edad")
            
        while edad_ingresada.isdigit() == False or int(edad_ingresada)<18: #while not edad_ingresada.isdigit()
            edad_ingresada = prompt(title="Inserción de datos", prompt="ERROR. Ingrese una edad válida.. ")

        if edad_ingresada != None:
            edad_ingresada = int(edad_ingresada)


        genero = prompt(title="Inserción de Datos", prompt="Elija entre 'F', 'NB', 'M' ")

        while genero != 'F' and genero != 'm   m' and genero != '':
            genero = prompt(title="Inserción de Datos", prompt="ERROR. Elija entre 'F', 'NB', 'M' ")
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()

""" 
Nombre
Edad (mayor de edad)
Género (F-M-NB)
Tecnología (PYTHON - JS - ASP.NET)
Puesto (Jr - Ssr - Sr)

Informar por pantalla:
a. Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS 
cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr.
b. Nombre del postulante Jr con menor edad.
c. Promedio de edades por género.
d. Tecnologia con mas postulantes (solo hay una).
e. Porcentaje de postulantes de cada genero.

Todos los datos se ingresan por prompt y los resultados se muestran por consola (print) """
