import os
import time
import keyboard  # Necesitarás instalar la biblioteca con `pip install keyboard`

def limpiar_pantalla():
    """Limpia la pantalla según el sistema operativo."""
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    pista = 50  # Longitud de la pista
    posicion_carrito = 0  # Posición inicial del carrito

    print("¡Bienvenido al juego del carrito! 🚗")
    print("Presiona 'd' para avanzar, 'q' para salir.\n")
    time.sleep(2)

    while True:
        limpiar_pantalla()
        pista_actual = ['-'] * pista
        pista_actual[posicion_carrito] = '🚗'

        # Imprime la pista y el carrito
        print("".join(pista_actual))
        print("\nPresiona 'd' para avanzar, 'q' para salir.")

        if keyboard.is_pressed('q'):
            print("\n¡Gracias por jugar! 🚗")
            break

        if keyboard.is_pressed('d'):
            posicion_carrito += 1
            if posicion_carrito >= pista:
                print("\n¡Felicidades, llegaste al final de la pista! 🎉🚗")
                break

        time.sleep(0.1)  # Evita que el avance sea demasiado rápido

if __name__ == "__main__":
    main()
