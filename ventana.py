import tkinter as Ventana

Usuario_actual = None
Carro_actual = None

obj_ventana = Ventana.Tk()
obj_ventana.geometry("500x520")
obj_ventana.config(bg="white")
obj_ventana.resizable(False, False)
obj_ventana.title("Parqueadero")

# =======================
# TITULO
# =======================

Ventana.Label(obj_ventana,
              text="SISTEMA PARQUEADERO",
              bg="blue",
              fg="white",
              font=("Arial", 12, "bold"),
              pady=8).pack(fill="x")

# =======================
# FRAME PRINCIPAL
# =======================

frame = Ventana.Frame(obj_ventana, bg="lightblue")
frame.pack(pady=10)

# ===== USUARIO =====

Ventana.Label(frame, text="ID", bg="lightblue").grid(row=0, column=0)
entry_id = Ventana.Entry(frame)
entry_id.grid(row=0, column=1)

Ventana.Label(frame, text="Nombre", bg="lightblue").grid(row=1, column=0)
entry_nombre = Ventana.Entry(frame)
entry_nombre.grid(row=1, column=1)

Ventana.Label(frame, text="Tipo Usuario", bg="lightblue").grid(row=2, column=0)
entry_tipo = Ventana.Entry(frame)
entry_tipo.grid(row=2, column=1)

def registrar_usuario():
    global Usuario_actual

    if entry_id.get() and entry_nombre.get() and entry_tipo.get():
        Usuario_actual = Usuario(entry_id.get(), entry_nombre.get(), entry_tipo.get())
        label_registro.config(text="USUARIO REGISTRADO", fg="green")
    else:
        label_registro.config(text="FALTAN DATOS DEL USUARIO", fg="red")

Ventana.Button(frame, text="Registrar Usuario",
               command=registrar_usuario,
               bg="black", fg="white").grid(row=3, column=0, columnspan=2, pady=5)

# ===== CARRO =====

Ventana.Label(frame, text="Placa", bg="lightblue").grid(row=4, column=0)
entry_placa = Ventana.Entry(frame)
entry_placa.grid(row=4, column=1)

Ventana.Label(frame, text="Tipo Carro", bg="lightblue").grid(row=5, column=0)
entry_tipo_carro = Ventana.Entry(frame)
entry_tipo_carro.grid(row=5, column=1)

Ventana.Label(frame, text="Color", bg="lightblue").grid(row=6, column=0)
entry_color = Ventana.Entry(frame)
entry_color.grid(row=6, column=1)

def registrar_carro():
    global Carro_actual

    if entry_placa.get() and entry_tipo_carro.get() and entry_color.get():
        Carro_actual = Carro(entry_placa.get(),
                             entry_tipo_carro.get(),
                             entry_color.get())
        label_registro.config(text="CARRO REGISTRADO", fg="green")
    else:
        label_registro.config(text="FALTAN DATOS DEL CARRO", fg="red")

Ventana.Button(frame, text="Registrar Carro",
               command=registrar_carro,
               bg="black", fg="white").grid(row=7, column=0, columnspan=2, pady=5)

# ===== PARQUEADERO =====

Ventana.Label(frame, text="Puesto", bg="lightblue").grid(row=8, column=0)
entry_puesto = Ventana.Entry(frame)
entry_puesto.grid(row=8, column=1)

Ventana.Label(frame, text="Fecha", bg="lightblue").grid(row=9, column=0)
entry_fecha = Ventana.Entry(frame)
entry_fecha.grid(row=9, column=1)

Ventana.Label(frame, text="Hora Entrada", bg="lightblue").grid(row=10, column=0)
entry_hora_e = Ventana.Entry(frame)
entry_hora_e.grid(row=10, column=1)

Ventana.Label(frame, text="Hora Salida", bg="lightblue").grid(row=11, column=0)
entry_hora_s = Ventana.Entry(frame)
entry_hora_s.grid(row=11, column=1)

Ventana.Label(frame, text="Estado", bg="lightblue").grid(row=12, column=0)
entry_estado = Ventana.Entry(frame)
entry_estado.grid(row=12, column=1)

def registrar_parqueo():

    if not Usuario_actual:
        label_registro.config(text="REGISTRE PRIMERO EL USUARIO", fg="red")
        return

    if not Carro_actual:
        label_registro.config(text="REGISTRE PRIMERO EL CARRO", fg="red")
        return

    if not entry_puesto.get() or not entry_fecha.get() or not entry_hora_e.get() or not entry_hora_s.get() or not entry_estado.get():
        label_registro.config(text="FALTAN DATOS DEL PARQUEADERO", fg="red")
        return

    obj_parq = Parqueadero(
        entry_puesto.get(),
        entry_fecha.get(),
        entry_hora_e.get(),
        entry_hora_s.get(),
        entry_estado.get()
    )

    obj_parq.acumular_info(Usuario_actual, Carro_actual)
    obj_parq.mostrar_tabla()

    label_registro.config(text="PARQUEO REGISTRADO CORRECTAMENTE", fg="green")

Ventana.Button(frame, text="Registrar Parqueo",
               command=registrar_parqueo,
               bg="green", fg="white").grid(row=13, column=0, columnspan=2, pady=10)

# ===== MENSAJE =====

label_registro = Ventana.Label(frame, text="", bg="lightblue", font=("Arial", 10, "bold"))
label_registro.grid(row=14, column=0, columnspan=2)

obj_ventana.mainloop()