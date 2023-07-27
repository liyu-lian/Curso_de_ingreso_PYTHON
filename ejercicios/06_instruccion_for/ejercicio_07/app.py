import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Al presionar el botón Mostrar pedir un número. mostrar los números divisores desde el 1 al número ingresado, 
y mostrar la cantidad de números divisores encontrados.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):

        contador_divisores = 0

        numero_ingresado = prompt(title="Inserción de datos", prompt="Ingrese un número.. ")
            
        while numero_ingresado.isalpha():
            numero_ingresado = prompt(title="Inserción de datos", prompt="ERROR. Ingrese un número.. ")

        if numero_ingresado != None:
            numero_ingresado = int(numero_ingresado)

        for mensaje in range (1, numero_ingresado+1):

            if numero_ingresado % mensaje == 0:

                print(mensaje)

                contador_divisores = contador_divisores + 1

        print("En total hay {0} divisores para este número".format(contador_divisores))
        
    
if __name__ == "__main__":
    app = App()
    app.mainloop()