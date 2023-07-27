import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Al presionar el botón 'MÁXIMO' se analizará el vector lista_datos a efectos de determinar cuál es el número 
más grande allí contenido el cual deberá ser informado utilizando Dialog Alert.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.btn_calcular = customtkinter.CTkButton(master=self, text="MÁXIMO", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=2, pady=10, columnspan=2, sticky="nsew")

        self.lista_datos = [1,80,5,0,15,-5,1,79]


    def btn_calcular_on_click(self):
        mensaje = None

        maximo = self.lista_datos[0]

        for numeros in self.lista_datos:
            if numeros > maximo:
                maximo = numeros

        mensaje = "El número {0} es el mayor de toda la lista".format(maximo)

        print(mensaje)
        

        
    
if __name__ == "__main__":
    app = App()
    app.mainloop()

"""     bandera = 0

        for numeros in self.lista_datos:

            if bandera  == 0 or numeros > numero_may:
                numero_may = numeros

        mensaje = "El numero más grande es "+str(numero_may)

        print(mensaje) """