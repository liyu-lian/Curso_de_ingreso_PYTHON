import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Al presionar el botón 'sumatoria' se analizará el vector lista_datos a efectos de calcular 
la sumatoria el cual deberá ser informado utilizando Dialog Alert.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.btn_calcular = customtkinter.CTkButton(master=self, text="SUMATORIA", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=2, pady=10, columnspan=2, sticky="nsew")

        self.lista_datos = [1,80,5,0,15,-5,1,79]


    def btn_calcular_on_click(self):
        #numeros = self.lista_datos[0]

        acumulador_numeros = 0

        mensaje = None

        for numero in self.lista_datos:
            print(numero)

            acumulador_numeros = acumulador_numeros + numero



        mensaje = "La sumatoria de los numeros en la lista es.. {0}".format(acumulador_numeros)        

        print(mensaje)

if __name__ == "__main__":
    app = App()
    app.mainloop()