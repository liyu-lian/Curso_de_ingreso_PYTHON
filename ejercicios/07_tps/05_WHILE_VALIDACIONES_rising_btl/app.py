import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Rising BTL. Empresa dedicada a la toma de datos para realizar estadísticas y censos nos pide realizar una carga de datos validada e ingresada 
por ventanas emergentes solamente (para evitar hacking y cargas maliciosas) y luego asignarla a cuadros de textos. 

Los datos requeridos son los siguientes:
    Apellido
    Edad, entre 18 y 90 años inclusive.
    Estado civil, ["Soltero/a", "Casado/a", "Divorciado/a", "Viudo/a"]
    Número de legajo, numérico de 4 cifras, sin ceros a la izquierda.
'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.label0 = customtkinter.CTkLabel(master=self, text="Apellido")
        self.label0.grid(row=0, column=0, padx=20, pady=10)
        self.txt_apellido = customtkinter.CTkEntry(master=self)
        self.txt_apellido.grid(row=0, column=1)

        self.label1 = customtkinter.CTkLabel(master=self, text="Edad")
        self.label1.grid(row=1, column=0, padx=20, pady=10)
        self.txt_edad = customtkinter.CTkEntry(master=self)
        self.txt_edad.grid(row=1, column=1)

        self.label2 = customtkinter.CTkLabel(master=self, text="Estado")
        self.label2.grid(row=2, column=0, padx=20, pady=10)
        self.combobox_tipo = customtkinter.CTkComboBox(
            master=self, values=["Soltero/a", "Casado/a", "Divorciado/a", "Viudo/a"])
        self.combobox_tipo.grid(row=2, column=1, padx=20, pady=10)

        self.label3 = customtkinter.CTkLabel(master=self, text="Legajo")
        self.label3.grid(row=3, column=0, padx=20, pady=10)
        self.txt_legajo = customtkinter.CTkEntry(master=self)
        self.txt_legajo.grid(row=3, column=1)

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        respuesta = True
        
        while respuesta != False:
            apellido = prompt(title="Inserción de datos", prompt="Ingrese su apellido")

            while apellido.isdigit():
                apellido = prompt(title="Inserción de datos", prompt="ERROR. Ingrese un apellido válido.. ")

            edad_ingresada = prompt(title="Inserción de datos", prompt="Ingrese su edad")

            while edad_ingresada.isalpha():
                edad_ingresada = prompt(title="Inserción de datos", prompt="ERROR. Ingrese una edad válida.. ")

            if edad_ingresada != None:
                edad_ingresada = int(edad_ingresada)
            
            while edad_ingresada < 18 or edad_ingresada > 90:
                edad_ingresada = prompt(title="Inserción de datos", prompt="ERROR. Debe ser mayor de 18 años pero no mayor de 90 años.. ")
                edad_ingresada = int(edad_ingresada)

            legajo = prompt(title="Inserción de datos", prompt="Ingrese su número de legajo (4 cifras).. ")

            while legajo == None or legajo.isdigit() == False or int(legajo) < 1001 or int(legajo) > 9999: #while not legajo.isdigit()
                legajo = prompt(title="Inserción de datos", prompt="ERROR. Ingrese su número de legajo(4 cifras).. ")

            estado_civil = prompt(title="Inserción de Datos", prompt="Elija entre 'Soltero/a', 'Casado/a', 'Divorciado/a' o 'Viudo/a' ")

            while estado_civil != 'Casado/a' and estado_civil != 'Soltero/a' and estado_civil != 'Divorciado/a' and estado_civil != 'Viudo/a':
                estado_civil = prompt(title="Inserción de Datos", prompt="ERROR. Elija entre 'Soltero/a', 'Casado/a', 'Divorciado/a' o 'Viudo/a' ")

            respuesta = question(title="Inserción de datos", message="Desea continuar?")

        self.txt_apellido.delete(0, 1000)
        self.txt_apellido.insert(0, apellido)
        self.txt_edad.delete(0, 1000)
        self.txt_edad.insert(0, edad_ingresada)

        self.txt_legajo.delete(0, 1000)
        self.txt_legajo.insert(0, legajo)

        self.combobox_tipo.set(estado_civil)

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()

"""    
    Apellido
    Edad, entre 18 y 90 años inclusive.
    Estado civil, ["Soltero/a", "Casado/a", "Divorciado/a", "Viudo/a"]
    Número de legajo, numérico de 4 cifras, sin ceros a la izquierda. """
