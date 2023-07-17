import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario quiera, 
hasta que presione el botón Cancelar (en el prompt) o el usuario ingrese cero. 
Calcular la suma acumulada de los positivos y multiplicar los negativos. 
Luego informar los resultados en las cajas de texto txt_suma_acumulada y txt_producto

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
        
        self.txt_suma_acumulada = customtkinter.CTkEntry(master=self, placeholder_text="Suma acumulada")
        self.txt_suma_acumulada.grid(row=0, padx=20, pady=20)

        self.txt_producto = customtkinter.CTkEntry(master=self, placeholder_text="Producto")
        self.txt_producto.grid(row=1, padx=20, pady=20)

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        acumulador_numeros = 0
        multiplicacion_negativos = 1
        respuesta = "Si"

        while respuesta != None:
            numero_ingresado = prompt(title="Números", prompt="Ingrese un número.. ")
            numero_ingresado = int(numero_ingresado)

            if numero_ingresado > 0:
                acumulador_numeros = acumulador_numeros + numero_ingresado
            elif numero_ingresado<0:
                multiplicacion_negativos = multiplicacion_negativos * numero_ingresado

            respuesta = prompt(title = "Respuesta", prompt="Desea seguir ingresando números? Presione 'Cancel' para cerrar ")
        
        self.txt_suma_acumulada.delete(0, 1000)
        self.txt_suma_acumulada.insert(0, acumulador_numeros)
        self.txt_producto.delete(0, 1000)
        self.txt_producto.insert(0, multiplicacion_negativos)

    
if __name__ == "__main__":
    app = App()
    app.mainloop()
