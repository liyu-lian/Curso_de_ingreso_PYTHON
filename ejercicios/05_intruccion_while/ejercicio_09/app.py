import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario quiera 
hasta que presione el botón Cancelar (en el prompt). 
Luego determinar el máximo y el mínimo 
e informarlos en los cuadros de textos txt_maximo y txt_minimo respectivamente

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
        
        self.txt_minimo = customtkinter.CTkEntry(master=self, placeholder_text="Mínimo")
        self.txt_minimo.grid(row=0, padx=20, pady=20)

        self.txt_maximo = customtkinter.CTkEntry(master=self, placeholder_text="Máximo")
        self.txt_maximo.grid(row=1, padx=20, pady=20)

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        respuesta = True

        bandera_primer_num = 0
        bandera_primernum = 0
        
        while respuesta != False:

            numero_ingresado = prompt(title="Inserción de datos", prompt="Ingrese un número.. ")
            
            while numero_ingresado.isalpha():
                numero_ingresado = prompt(title="Inserción de datos", prompt="ERROR. Ingrese un número.. ")

            if numero_ingresado.isdigit():
                numero_ingresado = int(numero_ingresado)

                if bandera_primer_num == 0 or numero_ingresado > numero_max:
                    numero_max = numero_ingresado 
                    bandera_primer_num = 1
                
                if bandera_primernum == 0 or numero_ingresado < numero_min:
                    numero_min = numero_ingresado
                    bandera_primernum = 1

            respuesta = question(title="Ingreso de Números", message="Desea continuar?")
            
        self.txt_maximo.delete(0, 1000)
        self.txt_maximo.insert(0, numero_max)
        self.txt_minimo.delete(0, 1000)
        self.txt_minimo.insert(0, numero_min)
    
if __name__ == "__main__":
    app = App()
    app.mainloop()
