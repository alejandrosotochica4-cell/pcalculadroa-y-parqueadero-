
class Calculadora:
    def __init__(self, numero1, numero2, operacion):
        self.numero1 = numero1
        self.numero2 = numero2
        self.operacion = operacion

    def get_Numero1(self):
        return self.numero1
    
    def get_numero2(self):
        return self.numero2
    
    def get_operacion(self):
        return self.operacion
    
    def set_numero1(self,  nuevo_numero1):
        self.numero1 = nuevo_numero1

    def set_numero2(self, nuevo_numero2):
        self.numero2 = nuevo_numero2

    def set_operacion(self, nueva_operacion):
        self.operacion = nueva_operacion

    def mostrar_info(self):
        print(f"Numero 1: {self.numero1}")
        print(f"Numero 2: {self.numero2}")
        print(f"Operacion: {self.operacion}")

    def calcular(self):

        if self.operacion == "suma":
            return self.numero1 + self.numero2

        elif self.operacion == "resta":
            return self.numero1 - self.numero2

        elif self.operacion == "multiplicacion":
            return self.numero1 * self.numero2

        elif self.operacion == "division":
            if self.numero2 == 0:
                return "Error: division por cero"
            return self.numero1 / self.numero2

        else:
            return "Operacion no valida"

        
