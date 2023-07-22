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

        contador_nobinarios = 0
        bandera_menoredad = 0

        acum_edad_NB= 0
        acum_edad_F = 0
        acum_edad_M = 0
        cont_NB = 0
        cont_M = 0
        cont_F = 0

        mensaje = None
        
        for postulantes in range(11):

            nombre_ingresado = prompt(title="Datos Postulantes", prompt="Ingrese el nombre del postulante")

            while nombre_ingresado.isdigit():
                nombre_ingresado = prompt(title="Datos Postulantes", prompt="ERROR. Ingrese un nombre valido para el postulante")
            
            edad_ingresada = prompt(title="Datos Postulantes", prompt="Ingrese la edad del postulante")

            while edad_ingresada.isalpha():

                edad_ingresada = prompt(title="Datos Postulantes", prompt="ERROR. Ingrese una edad valida para el postulante")

            edad_ingresada = int(edad_ingresada)

            while edad_ingresada < 18:
                edad_ingresada = prompt(title="Datos Postulantes", prompt="ERROR. El postulante debe ser mayor de edad ")
                edad_ingresada = int(edad_ingresada)
            
            genero_ingresado = prompt(title="Datos: Postulantes", prompt="Ingrese el género del postulante: 'F', 'M', 'NB'")

            while genero_ingresado !='F' and genero_ingresado !='M' and genero_ingresado !='NB':
                genero_ingresado = prompt(title="Datos: Postulantes", prompt="ERROR. Ingrese un género valido para el postulante: 'F', 'M', 'NB'")

            match genero_ingresado:
                case "NB":
                    acum_edad_NB = acum_edad_NB + edad_ingresada
                    cont_NB = cont_NB + 1
                case "F":
                    acum_edad_F = acum_edad_F + edad_ingresada
                    cont_F = cont_F + 1
                case "M": 
                    acum_edad_M = acum_edad_M + edad_ingresada
                    cont_M = cont_M + 1

            tecnologia_ingresada = prompt(title="Datos: Postulantes", prompt="Ingrese la tecnología del postulante: 'PYTHON', 'JS', 'ASP.NET'")

            while tecnologia_ingresada !='PYTHON' and tecnologia_ingresada !='JS' and tecnologia_ingresada !='ASP.NET':
                tecnologia_ingresada = prompt(title="Datos: Postulantes", prompt="ERROR. Ingrese una tecnología válida para el postulante: 'PYTHON', 'JS', 'ASP.NET'")
            
            puesto_ingresado = prompt(title="Datos: Postulantes", prompt="Ingrese el puesto del postulante: 'Jr', 'Ssr', 'Sr'")

            while puesto_ingresado !='Jr' and puesto_ingresado !='Ssr' and puesto_ingresado !='Sr':
                puesto_ingresado = prompt(title="Datos: Postulantes", prompt="ERROR. Ingrese un puesto válido para el postulante: 'Jr', 'Ssr', 'Sr'")
            
            match puesto_ingresado:
                case "Ssr":
                    match genero_ingresado:
                        case "NB": 
                            match tecnologia_ingresada:
                                case "JS" | "ASP.NET":
                                    if edad_ingresada >25 and edad_ingresada <40:
                                        contador_nobinarios = contador_nobinarios +1
                case "Jr":
                    if bandera_menoredad == 0 or edad_ingresada < Jrmenor_edad:
                        Jrmenor_edad = edad_ingresada
                        nombre_Jrmenoredad = nombre_ingresado
            
        promedio_NB = acum_edad_NB/cont_NB
        promedio_M = acum_edad_M / cont_M
        promedio_F = acum_edad_F / cont_F
        
        mensaje = " A. Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr: "+str(contador_nobinarios)
        mensaje += "\n B. El Nombre del postulante Jr con menor edad es "+nombre_Jrmenoredad
        mensaje += "\n El promedio de edad del género F es: "+str(promedio_F)
        mensaje += "\n El promedio de edad del género M es: "+str(promedio_M)
        mensaje += "\n El promedio de edad del género NB es: "+str(promedio_NB)
        mensaje += ""
        mensaje += ""

        alert(title="Datos: Consultantes", message=mensaje)



if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()

""" 
Informar por pantalla:
a. Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS 
cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr.
b. Nombre del postulante Jr con menor edad.
c. Promedio de edades por género.
d. Tecnologia con mas postulantes (solo hay una).
e. Porcentaje de postulantes de cada genero.

Todos los datos se ingresan por prompt y los resultados se muestran por consola (print) """
