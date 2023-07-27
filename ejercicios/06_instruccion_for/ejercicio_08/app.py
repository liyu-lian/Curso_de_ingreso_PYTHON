import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Al presionar el botón Mostrar pedir un número. Informar si el número es PRIMO o no.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):

        contador_ceros = 0

        mensaje = None

        numero_ingresado = prompt(title="Inserción de datos", prompt="Ingrese un número.. ")
            
        while numero_ingresado.isalpha():
            numero_ingresado = prompt(title="Inserción de datos", prompt="ERROR. Ingrese un número.. ")

        if numero_ingresado != None:
            numero_ingresado = int(numero_ingresado)

        if numero_ingresado > 0:
            for numero in range(2, numero_ingresado):
                resto = numero_ingresado % numero

                if resto == 0:
                    contador_ceros = contador_ceros + 1

            if contador_ceros == 0:
                mensaje = "El número es primo"
            else:
                mensaje = "El numero ingresado no es primo"
        else:
            mensaje = "El numero ingresado no es primo"
        

        print(mensaje)
    
if __name__ == "__main__":
    app = App()
    app.mainloop()