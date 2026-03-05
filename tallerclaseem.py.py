import tkinter as tk 
from tkinter import ttk 

ventana = tk.Tk()
ventana.title("Formulario")
ventana.geometry("500x650")

nombre_var = tk.StringVar()
genero_var = tk.StringVar()
lenguaje_var = tk.StringVar()
lenguaje_var.set("Seleccione")
python = tk.IntVar()
Java = tk.IntVar()

label_n = tk.Label(ventana, text="nombre")
label_n.pack()

Entry_n= tk.Entry(ventana,textvariable=nombre_var)

Entry_n.pack()

label_g = tk.Label(ventana, text="Genero:")
label_g.pack 

radio_m = tk.Radiobutton(ventana, text="Masculino", variable=genero_var, value="Masculino")
radio_m.pack()

radio_f = tk.Radiobutton (ventana, text="Femenino", variable=genero_var, value="Femenino")
radio_f.pack()

label_i = tk.Label(ventana, text="interes")
label_i.pack()

check_p = tk.Checkbutton( ventana, text=" phyton", variable= python ).pack()
check_j = tk.Checkbutton( ventana, text="Java", variable= Java).pack()

label_i = tk.Label(ventana, text= "lenguaje favorito").pack()
opcion_m = tk.OptionMenu ( ventana, lenguaje_var, "python", "Java", "C++").pack ()

label_pais = tk.Label ( ventana, text="Seleccione Pais").pack()
lista = tk.Listbox( ventana, height=3)
lista.insert(1," Colombia")
lista.insert(2,"Venezuela")
lista.insert(3, "Peru")

lista.pack()
Separador=ttk.Separator(ventana, orient= "horizontal")
Separador.pack(fill="x", pady=10 )

label_r = tk.Label(ventana, text="Resultados").pack()

frame_R = tk.Frame(ventana)
frame_R.pack()

text = tk.Text( frame_R, width=50, height=10)
Scroll = ttk.Scrollbar( frame_R, command=text.yview)
text.config(yscrollcommand = Scroll.set)
text.pack(side= "left")
Scroll.pack(side="right", fill="y")

def mostrar():
    text.insert( "end", "Nombre: " + nombre_var.get() + "\n" )
    text.insert( "end", "Genero: " + genero_var.get() + "\n" )
    text.insert("end", "Ineteres:")
    if python.get()==1:
        text.insert("end", "python")
        if Java.get()==1:
            text.insert("end", "Java")
    text.insert("end", "Lenguaje favorito:" + lenguaje_var.get() + "\n")

    Seleccion = lista.curselection()
    if Seleccion: 
        text.insert("end", "Pais seleccionado: " + lista.get(Seleccion[0]) + "\n")
        text.insert("end")

btn_mostrar = tk.Button(ventana, text="Mostar Resultados", command=mostrar)
btn_mostrar.pack()

ventana.mainloop()