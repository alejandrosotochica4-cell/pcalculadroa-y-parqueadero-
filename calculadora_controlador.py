from calculadora_modelo import Calculadora
from calculadora_vista import VistaCalculadora

class ControladorCalculadora:

    def __init__(self):
        self.vista = VistaCalculadora()
        self.vista.boton_calcular.config(command=self.iniciar)

    def iniciar(self):

        num1_valor = self.vista.pedir_numero1()
        num2_valor = self.vista.pedir_numero2()
        operacion = self.vista.pedir_operacion()

        calculadora = Calculadora(num1_valor, num2_valor, operacion)

        resultado = calculadora.calcular()

        self.vista.mostrar_resultado(resultado)