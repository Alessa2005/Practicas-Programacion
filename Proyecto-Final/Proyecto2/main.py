from src.Consola import Consola
from ejecucion import ejecutar_cancer, ejecutar_bases
RESET = "\033[0m"
GREEN = "\033[32m"
BLUE = "\033[34m"
BRIGHT = "\033[1m"
RED = "\033[31m"

def main():
    cl = Consola()
    print(BLUE + BRIGHT + "\n--MENÚ PRINCIPAL CLASIFICADOR--\n" + RESET)
    opciones_menu = [
        "Ejecutar los análisis del mejor árbol de desición para cancer.csv",
        "Ejecutar el programa para dos bases de datos genéricas A y B",
        "Terminar programa"
    ]
    while True:
        try:
            opcion = cl.mostrar_opciones("Seleccione una opción:", opciones_menu)
            if opcion == "regresar":
                print(GREEN + "Gracias por usar el programa. ¡Hasta luego!" + RESET)
                break
            elif opcion == "Ejecutar los análisis del mejor árbol de desición para cancer.csv":
                ejecutar_cancer()
            elif opcion == "Ejecutar el programa para dos bases de datos genéricas A y B":
                ejecutar_bases()
            elif opcion == "Terminar programa":
                print("\n\033[32mGracias por usar el programa. ¡Hasta luego!\033[0m")
                break
            if cl.terminar():
                print(GREEN + "Gracias por usar el programa. Hasta luego!" + RESET)
                break
        except Exception as e:
            print(RED + f"\nError: {e}\n" + RESET)

if __name__ == "__main__":
    main()