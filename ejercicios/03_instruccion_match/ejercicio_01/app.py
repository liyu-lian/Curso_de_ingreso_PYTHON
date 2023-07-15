import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
Enunciado:
Obtener el valor del mes seleccionado en el combobox_mes y  
al presionar el botón ‘Informar’ mostrar mediante alert los siguientes mensajes 
en función del mes seleccionado:
    Si el mes seleccionado es Enero: ‘que comiences bien el año!!!’
    Si el mes seleccionado es Marzo: ‘a clases!!’
    Si el mes seleccionado es Julio: ‘se vienen las vacaciones!!’
    Si el mes seleccionado es Diciembre: ‘Felices fiestas!!!’

En caso de seleccionar un mes distinto a los mencionados, no hacer nada
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.label_meses = customtkinter.CTkLabel(master=self, text="Meses")
        self.label_meses.grid(row=0, column=0, padx=20, pady=10)
        meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
        self.combobox_mes = customtkinter.CTkComboBox(master=self, values=meses)
        self.combobox_mes.grid(row=1, column=0, padx=20, pady=(10, 10))
        
        self.btn_informar = customtkinter.CTkButton(master=self, text="Informar", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_informar_on_click(self):
        mes_ingresado = self.combobox_mes.get()
        mensaje = None

        match mes_ingresado:
            case "Enero":
                mensaje = "Que comience bien el año!"
            case "Marzo":
                mensaje = "A clases!!"
            case "Julio":
                mensaje = "Se vienen las vacaciones!!!"
            case "Diciembre":
                mensaje = "Felices fiestas!!!!"

        alert(title="Eventos del Año", message=mensaje)
    
if __name__ == "__main__":
    app = App()
    app.mainloop()


"""         if (mes_ingresado == "Enero"):
            mensaje = "Que comience bien el año!!"
        elif (mes_ingresado == "Marzo"):
            mensaje = "A clases!!"
        elif(mes_ingresado == "Julio"):
            mensaje = "Se vienen las vacaciones!!"
        elif(mes_ingresado == "Diciembre"):
            mensaje = "Felices fiestas!!"
        else:
            mensaje = "Seleccione otro mes" """