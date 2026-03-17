from calculadora_controlador import ControladorCalculadora

if __name__ == "__main__":
    print(" CALCULADORA - Estructura MVC")

    controlador = ControladorCalculadora()
    controlador.vista.iniciar()