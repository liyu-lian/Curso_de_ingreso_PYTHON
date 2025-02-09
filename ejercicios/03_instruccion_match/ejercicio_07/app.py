import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
Juliana Gimena Grajeda


Enunciado:
Obtener el destino seleccionado en el combobox_destino, luego al presionar el 
botón ‘Informar’ indicar el punto cardinal de nuestro país donde se encuentra: 
Norte, Sur, Este u Oeste
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
                mensaje = "Se encuentra en el Oeste del País"
            case "Mar del plata":
                mensaje = "Se encuentra en el Este del País"
            case "Cataratas":
                mensaje = "Se encuentra en el Norte del País"
            case "Ushuaia":
                mensaje = "Se encuentra en el Sur del País"
        alert(title="Destino", message=mensaje)
    
if __name__ == "__main__":
    app = App()
    app.mainloop()