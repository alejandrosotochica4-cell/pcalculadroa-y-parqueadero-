import tkinter as ventana
from datetime import datetime

# ===== VENTANA =====

obj_ventana = ventana.Tk()
obj_ventana.geometry("480x600")
obj_ventana.config(bg="lightgreen")
obj_ventana.resizable(False, False)
obj_ventana.title("Parqueadero y Registro")

Usuario_actual = None

# =========================
# SECCIÓN 1 - USUARIO
# =========================

titulo_label = ventana.Label(obj_ventana,
                             text="REGISTRAR USUARIO",
                             bg="green",
                             fg="white",
                             font=("Arial", 12, "bold"),
                             pady=8)
titulo_label.pack(fill="x")

seccion1 = ventana.Frame(obj_ventana, bg="green")
seccion1.pack(pady=8)

ventana.Label(seccion1, text="Cédula:", bg="lightgreen").grid(row=0, column=0, pady=4)
entry_id = ventana.Entry(seccion1, width=22)
entry_id.grid(row=0, column=1)

ventana.Label(seccion1, text="Nombre:", bg="lightgreen").grid(row=1, column=0, pady=4)
entry_nombre = ventana.Entry(seccion1, width=22)
entry_nombre.grid(row=1, column=1)

ventana.Label(seccion1, text="Tipo Usuario:", bg="lightgreen").grid(row=2, column=0, pady=4)
entry_tipo = ventana.Entry(seccion1, width=22)
entry_tipo.grid(row=2, column=1)

label_usuario_registrado = ventana.Label(obj_ventana,
                                         text="Usuario: No registrado",
                                         bg="green",
                                         fg="white")
label_usuario_registrado.pack(fill="x", pady=5)

def registro_usuario():
    global Usuario_actual

    id_usuario = entry_id.get()
    nombre_usuario = entry_nombre.get()
    tipo_usuario = entry_tipo.get()

    if id_usuario and nombre_usuario and tipo_usuario:
        Usuario_actual = (id_usuario, nombre_usuario, tipo_usuario)
        label_usuario_registrado.config(
            text=f"Usuario: {nombre_usuario} (ID: {id_usuario})",
            fg="white"
        )
        entry_id.delete(0, ventana.END)
        entry_nombre.delete(0, ventana.END)
        entry_tipo.delete(0, ventana.END)
    else:
        label_usuario_registrado.config(
            text="Complete todos los datos del usuario",
            fg="red"
        )

ventana.Button(seccion1,
               text="Registrar Usuario",
               command=registro_usuario,
               bg="black",
               fg="white").grid(row=3, column=0, columnspan=2, pady=8)

# =========================
# SECCIÓN 2 - PARQUEADERO
# =========================

titulo_label2 = ventana.Label(obj_ventana,
                              text="REGISTRO PARQUEADERO",
                              bg="green",
                              fg="white",
                              font=("Arial", 12, "bold"),
                              pady=8)
titulo_label2.pack(fill="x")

seccion2 = ventana.Frame(obj_ventana, bg="green")
seccion2.pack(pady=8)

# Campos correctamente organizados (SIN repetir filas)

campos = [
    "Placa:",
    "Tipo Carro:",
    "Color:",
    "Puesto:",
    "Fecha:",
    "Hora Entrada:",
    "Hora Salida:",
    "Estado:"
]

entries = []

for i, texto in enumerate(campos):
    ventana.Label(seccion2, text=texto, bg="lightgreen").grid(row=i, column=0, pady=3)
    entry = ventana.Entry(seccion2, width=22)
    entry.grid(row=i, column=1)
    entries.append(entry)

label_parqueo = ventana.Label(obj_ventana,
                               text="Parqueo: No registrado",
                               bg="green",
                               fg="white")
label_parqueo.pack(fill="x", pady=5)

def registrar_parqueo():

    if not Usuario_actual:
        label_parqueo.config(text="Primero registre el usuario", fg="red")
        return

    for entry in entries:
        if not entry.get():
            label_parqueo.config(text="Complete todos los datos del parqueo", fg="red")
            return

    placa = entries[0].get()
    puesto = entries[3].get()
    fecha = entries[4].get()

    label_parqueo.config(
        text=f"Parqueo registrado | Placa: {placa} | Puesto: {puesto} | Fecha: {fecha}",
        fg="white"
    )

    # Limpiar campos después de registrar
    for entry in entries:
        entry.delete(0, ventana.END)

ventana.Button(seccion2,
               text="Registrar Parqueo",
               command=registrar_parqueo,
               bg="blue",
               fg="white").grid(row=9, column=0, columnspan=2, pady=10)

# ===== EJECUCIÓN =====

obj_ventana.mainloop()