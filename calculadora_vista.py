import tkinter as tk

class VistaCalculadora:

    def __init__(self):

        self.ventana = tk.Tk()
        self.ventana.title("Calculadora MVC")
        self.ventana.geometry("300x250")

        # Numero 1
        tk.Label(self.ventana, text="Numero 1").pack()
        self.entrada1 = tk.Entry(self.ventana)
        self.entrada1.pack()

        # Numero 2
        tk.Label(self.ventana, text="Numero 2").pack()
        self.entrada2 = tk.Entry(self.ventana)
        self.entrada2.pack()

        # Operacion
        tk.Label(self.ventana, text="Operacion (suma, resta, multiplicacion, division)").pack()
        self.entrada_operacion = tk.Entry(self.ventana)
        self.entrada_operacion.pack()

        # Resultado
        self.label_resultado = tk.Label(self.ventana, text="Resultado:")
        self.label_resultado.pack()

        # Boton
        self.boton_calcular = tk.Button(self.ventana, text="Calcular")
        self.boton_calcular.pack()

    def pedir_numero1(self):
        return float(self.entrada1.get())

    def pedir_numero2(self):
        return float(self.entrada2.get())

    def pedir_operacion(self):
        return self.entrada_operacion.get()

    def mostrar_resultado(self, resultado):
        self.label_resultado.config(text=f"Resultado: {resultado}")

    def iniciar(self):
        self.ventana.mainloop()