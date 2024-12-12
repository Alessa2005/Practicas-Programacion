from .TablaDatos import TablaDatos

class Consola:
    """
    Clase que representa un menú interactivo en la consola.
    """

    def entradaDatos(self, texto):
        """
        Solicita datos al usuario para 
        ejecutar el programa.

        Args:
            texto (str): Mensaje que se mostrará al 
            usuario para indicar la entrada necesaria.

        Returns:
            TablaDatos: Objeto con los datos necesarios 
            para el programa.

        Raises:
            ValueError: Si el texto proporcionado 
            es una cadena vacía o None.
        """
        if texto == "" or texto is None:
            raise ValueError("Texto invalido")
        archivo = input(texto)
        return TablaDatos(archivo)

    def menu_opciones(self, opciones, seleccionado):
        """
        Obtiene la opción seleccionada por el 
        usuario a partir de un menú de opciones.

        Args:
            opciones (list[str]): Lista de opciones 
            disponibles para seleccionar.
            seleccionado (str): Entrada del usuario
            indicando la opción elegida.

        Returns:
            str: Opción seleccionada por el usuario o 
            "regresar" si selecciona 0.

        Raises:
            TypeError: Si la entrada del usuario 
            no es un número entero.
            ValueError: Si la entrada del usuario 
            no corresponde a una opción válida.
        """
        try:
            selec = int(seleccionado)
            if selec == 0:
                return "regresar"
            if 1 <= selec <= len(opciones):
                return opciones[selec - 1]
            else:
                print("\033[31mOpción no válida. Intenta nuevamente.\033[0m\n")
        except TypeError:
            raise TypeError("Entrada inválida. Por favor, ingresa un número.\n")
        except ValueError:
            raise  ValueError("Entrada inválida. Por favor, ingresa un número.\n")

    def mostrar_opciones(self, titulo, opciones):
        """
        Muestra un menú de opciones en la consola 
        y solicita al usuario que seleccione una.

        Args:
            titulo (str): Título descriptivo del menú de opciones.
            opciones (list[str]): Lista de opciones disponibles 
            para seleccionar.

        Returns:
            str: Opción seleccionada por el usuario.
        """
        while True:
            try:
                print(f"\n{titulo}")
                for i, opcion in enumerate(opciones):
                    print(f"[{i}] - {opcion}")
                eleccion = int(input("Ingrese el número seleccionado: "))
                if 0 <= eleccion < len(opciones):
                    return opciones[eleccion]
                else:
                    print("\033[31mError: Selección fuera de rango. Intenta nuevamente.\033[0m")
            except ValueError:
                print("\033[31mError: Entrada inválida. Por favor, ingresa un número.\033[0m")

    def terminar(self):
        """
        Termina el programa ejecutado en consola.

        Returns:
            Boolean: True si el usuario escoje salir
        """
        try:
            elegido = self.mostrar_opciones("¿Desea terminar el programa?", ["Terminar programa", "No"])
            if elegido == "Terminar programa":
                return True
            return False
        except Exception as e:
            print(f"\033[31mError inesperado: {e}\033[0m")
            return False


