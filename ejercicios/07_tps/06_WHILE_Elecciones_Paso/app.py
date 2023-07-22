'''
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por consola (print)

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
        respuesta = "Sí"

        bandera_primercandidato = 0

        candidato_menos_votos = 0
        candidato_mas_votos = 0

        acum_edades = 0
        acum_votosemitidos = 0
        contador_candidatos = 0

        mensaje = None

        while respuesta == "Sí":

            nombre_candidatos = prompt(title="Elección de Presidente", prompt="Ingrese el nombre de su candidato.. ")

            while nombre_candidatos.isdigit():
                nombre_candidatos = prompt(title="Elección de Presidente", prompt="Error. Ingrese el nombre de su candidato(solo letras)")

            edad_candidatos = prompt(title="Elección Presidente", prompt="Ingrese la edad de su candidato")
            edad_candidatos = int(edad_candidatos)

            while edad_candidatos < 25:
                edad_candidatos = prompt(title="Elección Presidente", prompt="Error. Ingrese una edad válida para su candidato")
                edad_candidatos = int(edad_candidatos)
            
            acum_edades = acum_edades + edad_candidatos

            cantidad_votos = prompt(title="Elección de Presidente", prompt="Ingrese la cantidad de votos de su candidato.. ")
            cantidad_votos = int(cantidad_votos)

            while cantidad_votos < 0:
                cantidad_votos = prompt(title="Elección de Presidente", prompt="Error. Ingrese una cantidad válida de votos para su candidato.. ")
                cantidad_votos = int(cantidad_votos)

            acum_votosemitidos = acum_votosemitidos + cantidad_votos

            if bandera_primercandidato == 0 and cantidad_votos > candidato_mas_votos:
                candidato_mas_votos = cantidad_votos
                nombre_candidatomasvotos = nombre_candidatos
                bandera_primercandidato = 1
            elif cantidad_votos < candidato_mas_votos:
                candidato_menos_votos = cantidad_votos
                nombre_candidatomenosvotos = nombre_candidatos
                edad_candidatomenosvotos = edad_candidatos

            respuesta = prompt(title="Elección de Presidente", prompt="Desea continuar? Presione 'Cancel' para salir.. ")
            contador_candidatos = contador_candidatos + 1
        
        promedio_edades = acum_edades / contador_candidatos


        mensaje = "El nombre del candidato con más votos es "+nombre_candidatomasvotos+" con una cantidad de "+str(candidato_mas_votos)
        mensaje += "\n El candidato con menos votos es "+nombre_candidatomenosvotos+". Con una edad de "+str(edad_candidatomenosvotos)+" y "+str(candidato_menos_votos)+" votos."
        mensaje += "\n El promedio de las edades de todos los candidatos es "+str(promedio_edades)
        mensaje += "\n La cantidad total de votos emitidos es "+str(acum_votosemitidos)

        print(mensaje)

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()

""" De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por consola (print) """