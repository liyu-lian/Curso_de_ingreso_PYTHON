import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    La suma acumulada de los negativos
    La suma acumulada de los positivos
    Cantidad de números positivos ingresados
    Cantidad de números negativos ingresados
    Cantidad de ceros
    Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        #HECHO EN CLASE

        Numero_ingresado = " "

        acum_suma_negativos = 0
        acum_suma_positivos = 0

        contador_positivos = 0
        contador_negativos = 0
        contador_ceros = 0

        while Numero_ingresado != None:  
            Numero_ingresado = prompt(title="Número", prompt="Ingrese números o presione 'Cancel' para salir")

            if Numero_ingresado != None:
                Numero_ingresado = int(Numero_ingresado)
                if Numero_ingresado < 0:
                    contador_negativos = contador_negativos + 1
                    acum_suma_negativos = acum_suma_negativos + Numero_ingresado
                elif Numero_ingresado > 0:
                    contador_positivos = contador_positivos + 1
                    acum_suma_positivos = acum_suma_positivos +  Numero_ingresado
                else:
                    contador_ceros = contador_ceros + 1

        diferencia_posi_y_nega = contador_positivos - contador_negativos
            

        mensaje = " La suma de los números negativos es.. "+str(acum_suma_negativos)
        mensaje += "\n La suma de los números positivos es.. "+str(acum_suma_positivos)
        mensaje += "\n La cantidad de números positivos es "+str(contador_positivos)
        mensaje += "\n La cantidad de números negativos es "+str(contador_negativos)
        mensaje += "\n La cantidad de ceros es "+str(contador_ceros)
        mensaje += "\n La diferencia entre números positivos y números negativos es "+str(diferencia_posi_y_nega)


        alert(title="Números", message=mensaje)

    
if __name__ == "__main__":
    app = App()
    app.mainloop()

"""         while respuesta != None:
            
            numero_ingresado = prompt(title="Números", prompt="Ingrese un número.. ")
            numero_ingresado = int(numero_ingresado)
            
            if numero_ingresado < 0:
                suma_negativos = suma_negativos + numero_ingresado
                contador_negativos = contador_negativos + 1
            elif numero_ingresado > 0:
                suma_positivos = suma_positivos + numero_ingresado
                contador_positivos = contador_positivos + 1
            else:
                contador = contador + 1
            
            respuesta = prompt(title="Número", prompt="Desea seguir incertando números? Presione 'Cancel' para salir") """