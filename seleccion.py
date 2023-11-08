def selection_sort(vector):
    nb = len(vector)

    for actual in range(0, nb):
        mas_pequeno = actual

        for j in range(actual + 1, nb):
            if vector[j] < vector[mas_pequeno]:
                mas_pequeno = j

        if min is not actual:
            temp = vector[actual]
            vector[actual] = vector[mas_pequeno]
            vector[mas_pequeno] = temp

    return vector


if __name__ == '__main__':
    print(selection_sort([2, 10, 5, 8, 1, 4, 7]))
