def bubble_sort(vector):
    permutacion = True
    iteracion = 0

    while permutacion == True:
        permutacion = False
        iteracion += 1

        for actaul in range(0, len(vector) - iteracion):
            if vector[actaul] > vector[actaul + 1]:
                permutacion = True
                # Intercambiamos dos elementos
                vector[actaul], vector[actaul + 1] = vector[actaul + 1], vector[actaul]

    return vector


if __name__ == '__main__':
    print(bubble_sort([4, 3, 6, 74, 31, 46, 6, 19, 56, 14]))
