
import tkinter as tk
from datetime import datetime

# ===============================
# CONFIGURACIÓN GENERAL
# ===============================

usuario_actual = None

ventana = tk.Tk()
ventana.title("Sistema de Calculadora")
ventana.geometry("520x620")
ventana.configure(bg="#f2f2f2")
ventana.resizable(False, False)

# ===============================
# ESTILOS
# ===============================

COLOR_PRINCIPAL = "#1f4e79"
COLOR_SECUNDARIO = "#d9e6f2"
COLOR_BOTON = "#2e75b6"
COLOR_TEXTO = "white"

# ===============================
# SECCIÓN REGISTRO USUARIO
# ===============================

titulo_usuario = tk.Label(
    ventana,
    text="REGISTRO DE USUARIO",
    bg=COLOR_PRINCIPAL,
    fg="white",
    font=("Arial", 14, "bold"),
    pady=12
)
titulo_usuario.pack(fill="x")

frame_usuario = tk.Frame(ventana, bg=COLOR_SECUNDARIO, pady=15)
frame_usuario.pack(padx=20, pady=15, fill="x")

tk.Label(frame_usuario, text="ID:", bg=COLOR_SECUNDARIO, font=("Arial", 11)).grid(row=0, column=0, padx=10, pady=8)
entry_id = tk.Entry(frame_usuario, width=25)
entry_id.grid(row=0, column=1, padx=10, pady=8)

tk.Label(frame_usuario, text="Nombre:", bg=COLOR_SECUNDARIO, font=("Arial", 11)).grid(row=1, column=0, padx=10, pady=8)
entry_nombre = tk.Entry(frame_usuario, width=25)
entry_nombre.grid(row=1, column=1, padx=10, pady=8)

label_usuario_registrado = tk.Label(
    ventana,
    text="Usuario no registrado",
    bg="#f2f2f2",
    font=("Arial", 11, "italic")
)
label_usuario_registrado.pack(pady=5)

def registrar_usuario():
    global usuario_actual
    id_usuario = entry_id.get().strip()
    nombre_usuario = entry_nombre.get().strip()

    if id_usuario and nombre_usuario:
        usuario_actual = Usuario(id_usuario, nombre_usuario)
        label_usuario_registrado.config(
            text=f"Usuario activo: {nombre_usuario} (ID: {id_usuario})",
            fg="green"
        )
        entry_id.delete(0, tk.END)
        entry_nombre.delete(0, tk.END)
    else:
        label_usuario_registrado.config(
            text="Complete todos los campos",
            fg="red"
        )

btn_registrar = tk.Button(
    frame_usuario,
    text="Registrar Usuario",
    command=registrar_usuario,
    bg=COLOR_BOTON,
    fg=COLOR_TEXTO,
    width=20
)
btn_registrar.grid(row=2, column=0, columnspan=2, pady=10)

# ===============================
# SECCIÓN CALCULADORA
# ===============================

titulo_calc = tk.Label(
    ventana,
    text="CALCULADORA",
    bg=COLOR_PRINCIPAL,
    fg="white",
    font=("Arial", 14, "bold"),
    pady=12
)
titulo_calc.pack(fill="x", pady=(10, 0))

frame_calc = tk.Frame(ventana, bg=COLOR_SECUNDARIO, pady=20)
frame_calc.pack(padx=20, pady=15, fill="x")

tk.Label(frame_calc, text="Número 1:", bg=COLOR_SECUNDARIO).grid(row=0, column=0, padx=10, pady=8)
entry_num1 = tk.Entry(frame_calc, width=25)
entry_num1.grid(row=0, column=1, padx=10, pady=8)

tk.Label(frame_calc, text="Número 2:", bg=COLOR_SECUNDARIO).grid(row=1, column=0, padx=10, pady=8)
entry_num2 = tk.Entry(frame_calc, width=25)
entry_num2.grid(row=1, column=1, padx=10, pady=8)

tk.Label(frame_calc, text="Resultado:", bg=COLOR_SECUNDARIO).grid(row=2, column=0, padx=10, pady=8)
entry_resultado = tk.Entry(frame_calc, width=25, state="readonly")
entry_resultado.grid(row=2, column=1, padx=10, pady=8)

def realizar_operacion(tipo):
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())

        calc = Calculadora(datetime.now().strftime("%d/%m/%Y %H:%M:%S"), tipo)
        resultado = calc.hacer_operacion(num1, num2, tipo)

        entry_resultado.config(state="normal")
        entry_resultado.delete(0, tk.END)
        entry_resultado.insert(0, str(resultado))
        entry_resultado.config(state="readonly")

        if usuario_actual:
            calc.resultado = resultado
            calc.guardar_info(usuario_actual, num1, num2)

    except ValueError:
        entry_resultado.config(state="normal")
        entry_resultado.delete(0, tk.END)
        entry_resultado.insert(0, "Error: números inválidos")
        entry_resultado.config(state="readonly")

    except ZeroDivisionError:
        entry_resultado.config(state="normal")
        entry_resultado.delete(0, tk.END)
        entry_resultado.insert(0, "Error: división por cero")
        entry_resultado.config(state="readonly")

# BOTONES
frame_botones = tk.Frame(frame_calc, bg=COLOR_SECUNDARIO)
frame_botones.grid(row=3, column=0, columnspan=2, pady=15)

tk.Button(frame_botones, text="Suma +", width=12,
          command=lambda: realizar_operacion("suma"),
          bg=COLOR_BOTON, fg="white").grid(row=0, column=0, padx=5, pady=5)

tk.Button(frame_botones, text="Resta -", width=12,
          command=lambda: realizar_operacion("resta"),
          bg=COLOR_BOTON, fg="white").grid(row=0, column=1, padx=5, pady=5)

tk.Button(frame_botones, text="Multiplicación ×", width=12,
          command=lambda: realizar_operacion("multiplicacion"),
          bg=COLOR_BOTON, fg="white").grid(row=1, column=0, padx=5, pady=5)

tk.Button(frame_botones, text="División ÷", width=12,
          command=lambda: realizar_operacion("division"),
          bg=COLOR_BOTON, fg="white").grid(row=1, column=1, padx=5, pady=5)

def limpiar():
    entry_num1.delete(0, tk.END)
    entry_num2.delete(0, tk.END)
    entry_resultado.config(state="normal")
    entry_resultado.delete(0, tk.END)
    entry_resultado.config(state="readonly")

tk.Button(frame_botones, text="Limpiar",
          command=limpiar,
          bg="red", fg="white",
          width=26).grid(row=2, column=0, columnspan=2, pady=8)

# ===============================
ventana.mainloop()