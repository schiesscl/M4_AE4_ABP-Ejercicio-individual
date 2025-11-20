from persona import Persona
from tamagotchi import Tamagotchi

def main():
    # Creación de los objetos
    gozarutchi = Tamagotchi(nombre="Gozarutchi", color="Azul")
    persona3 = Persona(nombre="Hans", apellido="Schiess", tamagotchi=gozarutchi)

    # Mostrar información inicial
    print("--- Información ---")
    print(f"Persona: {persona3.nombre} {persona3.apellido}")
    print("Tamagotchi inicial:")
    gozarutchi.mostrar_estado()
    print("---------------------\n")

    while True:
        print("Elige una acción para realizar con tu Tamagotchi:")
        print("1. Jugar")
        print("2. Alimentar")
        print("3. Curar")
        print("4. Mostrar estado actual")
        print("5. Salir")

        opcion = input("Ingresa el número de la opción: ")

        if opcion == "1":
            persona3.jugar_con_tamagotchi()
        elif opcion == "2":
            persona3.darle_comida()
        elif opcion == "3":
            persona3.curarlo()
        elif opcion == "4":
            gozarutchi.mostrar_estado()
        elif opcion == "5":
            print("Vuelve pronto!")
            break
        else:
            print("Opción no válida. Por favor, elige un número del 1 al 5.")
        
        print("-" * 20)

if __name__ == "__main__":
    main()