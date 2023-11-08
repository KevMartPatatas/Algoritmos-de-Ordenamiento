def cocktail_sort(vector):
    permutacion, direccion, actual = True, 1, 0
    comienzo, fin = 0, len(vector) - 2

    while permutacion == True:
        permutacion = False

        while (actual < fin and direccion == 1) or (actual > comienzo and direccion == -1):
            # Prueba sin intercambio
            if vector[actual] > vector[actual + 1]:
                permutacion = True
                # Intercambiamos dos elementos
                vector[actual], vector[actual + 1] = vector[actual + 1], vector[actual]

            actual = actual + direccion

        # Cambiar la direccion de desplazamiento
        if direccion == 1:
            fin = fin - 1
        else:
            comienzo = comienzo + 1

        direccion = -direccion

    return vector


if __name__ == '__main__':
    print(cocktail_sort([2, 4, 14, 10, 12, 0, 1, -4, 3, 17, 5]))
