import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el
usuario quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    a. La suma acumulada de los negativos
    b. La suma acumulada de los positivos
    c. Cantidad de números positivos ingresados
    d. Cantidad de números negativos ingresados
    e. Cantidad de ceros
    f. El minimo de los negativos
    g. El maximo de los positivos
    h. El promedio de los negativos

Informar los resultados mediante alert()

'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.btn_cargar = customtkinter.CTkButton(
            master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_cargar.grid(row=2, padx=20, pady=20,
        columnspan=2, sticky="nsew")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar Estadísticas", command=self.btn_mostrar_estadisticas_on_click)
        self.btn_mostrar.grid(row=3, padx=20, pady=20,
        columnspan=2, sticky="nsew")

        self.lista = []

    def btn_comenzar_ingreso_on_click(self):
        respuesta = True

        while respuesta == True:

            numeros = input("Ingrese un número")

            while numeros.isalpha():
                numeros = input("ERROR. Ingrese un número.. ")

            self.lista.append(numeros)
            respuesta = question(title="Pregunta", message="Desea seguir ingresando números?")

    def btn_mostrar_estadisticas_on_click(self):

        acumulador_numeros_positivos  =0
        acumulador_numeros_negativos = 0
        contador_0 = 0
        contador_negativos = 0
        contador_positivos = 0

        bandera_1 = 0
        bandera_2 = 0

        for numero in self.lista:
            numero = int(numero)

            if bandera_1 == 0:
                minimo_neg = numero
                bandera_1 = 1
            else:
                if numero < minimo_neg:
                    minimo_neg = numero

            if bandera_2 == 0:
                maximo_pos = numero
                bandera_2 = 1
            else:
                if numero < maximo_pos:
                    maximo_pos = numero

            if numero > 0:
                acumulador_numeros_positivos = acumulador_numeros_positivos + numero

                contador_positivos = contador_positivos + 1
            elif numero < 0:
                acumulador_numeros_negativos = acumulador_numeros_negativos + numero

                contador_negativos = contador_negativos + 1
            else:
                contador_0 = contador_0 + 1

                
        promedio = acumulador_numeros_negativos / contador_negativos

        mensaje = "a. La suma acumulada de los negativos es {0}".format(acumulador_numeros_negativos)
        mensaje +="\n b. La suma acumulada de los positivos es {0}".format(acumulador_numeros_positivos)
        mensaje +="\n c. Cantidad de números positivos ingresados {0}".format(contador_positivos)
        mensaje +="\n d. Cantidad de números negativos ingresados {0}".format(contador_negativos)
        mensaje +="\n e. Cantidad de ceros {0}".format(contador_0)
        mensaje +="\n f. El minimo de los negativos {0}".format(minimo_neg)
        mensaje +="\n g. El maximo de los positivos {0}".format(maximo_pos)
        mensaje +="\n h. El promedio de los negativos {0}".format(promedio)

        print(mensaje)


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()

""" a. La suma acumulada de los negativos
    b. La suma acumulada de los positivos
    c. Cantidad de números positivos ingresados
    d. Cantidad de números negativos ingresados
    e. Cantidad de ceros
    f. El minimo de los negativos 
    g. El maximo de los positivos
    h. El promedio de los negativos """