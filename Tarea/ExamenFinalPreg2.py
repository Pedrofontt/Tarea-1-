"""4. Haga una clase jugadorLoteria que tenga nombre, cedula, usuario, clave y los números que jugará en el próximo sorteo.
Haga al menos 7 instancias de jugadores de lotería que solicite nombre, cedula, usuario, clave y los números que jugará
en el próximo sorteo y presentarlos en pantalla, tal y como se muestra en el ejemplo de salida. Durante el llenado de
datos si presiona la tecla Esc saldrá del programa inmediatamente."""

import random
import sys
def NumerosSorteo():
    return list(range(100))

class jugadorLoteria:
    def __init__(self, nombre, cedula, usuario, clave, numeros):
        self.nombre = nombre
        self.cedula = cedula
        self.usuario = usuario
        self.clave = clave
        self.numeros = numeros

def obtenerDatos():
    print("Ingrese los datos del jugador:")
    nombre = input("Nombre: ")
    cedula = input("Cédula: ")
    usuario = input("Usuario: ")
    clave = input("Clave: ")
    numeros = random.sample(NumerosSorteo(), 5)
    return jugadorLoteria(nombre, cedula, usuario, clave, numeros)

def main():
    jugadores = []
    while len(jugadores) < 7:
        print(f"Ingrese los datos del jugador {len(jugadores) + 1}: (Presione Esc (ctrl+c) para salir)")
        try:
            jugador = obtenerDatos()
            jugadores.append(jugador)
        except KeyboardInterrupt:  
            print("\nSaliendo del programa...")
            sys.exit()
    for i, jugador in enumerate(jugadores,1):
        print(f"Jugador {i}: {jugador.nombre}, Cédula: {jugador.cedula}, Usuario: {jugador.usuario}, Número que jugara en el proximo sorteo: {jugador.numeros}")

if __name__ == "__main__":
    main()