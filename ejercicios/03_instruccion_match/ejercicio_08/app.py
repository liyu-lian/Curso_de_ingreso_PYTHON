import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
Juliana Gimena Grajeda

Enunciado:
Obtener el destino seleccionado en el combobox_destino, luego al presionar el botón 
‘Informar’ indicar mediante alert si en el destino hace frío o calor la mayoría 
de las estaciones del año.
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        destinos = ['Bariloche', 'Mar del plata', 'Cataratas', 'Ushuaia']
        self.combobox_destino = customtkinter.CTkComboBox(master=self, values=destinos)
        self.combobox_destino.grid(row=1, column=0, padx=20, pady=(10, 10))
        
        self.btn_informar = customtkinter.CTkButton(master=self, text="Informar", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_informar_on_click(self):
        destino_ingresado = self.combobox_destino.get()

        mensaje = None

        match destino_ingresado:
            case "Bariloche":
                mensaje = "La mayoría del tiempo aquí hace frío" 
            case "Mar del plata":
                mensaje = "La mayoría del tiempo aquí hace frío" 
            case "Cataratas":
                mensaje = "La mayoría del tiempo aquí hace calor" 
            case "Ushuaia":
                mensaje = "La mayoría del tiempo aquí hace frío"
        alert(title="Destino y su temperatura", message=mensaje)
    
    
if __name__ == "__main__":
    app = App()
    app.mainloop()