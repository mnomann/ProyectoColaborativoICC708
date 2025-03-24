def get_notas():
    while True:
        try:
            notas = input("Ingrese las calificaciones separadas por espacios: ")
            notas_list = [float(notas) for grade in notas.split()]
            return notas_list
        except ValueError:
            print("Entrada invalida. ingresa solo numeros separados por espacios.")

if __name__ == "__main__":
    print(get_notas())
