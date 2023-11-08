def Insertion_sort(vector):
    for i in range(1, len(vector)):
        actual = vector[i]
        j = i

        #  Desplazamiento de los elementos de la matriz
        while j > 0 and vector[j - 1] > actual:
            vector[j] = vector[j - 1]
            j = j - 1

        #  Insertar el elemento en su lugar
        vector[j] = actual

    print(vector)


if __name__ == '__main__':
    Insertion_sort([4, 3, 6, 74, 31, 46, 6, 19, 56, 14])
