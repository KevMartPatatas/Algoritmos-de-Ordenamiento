def gnome_sort(vector):
    i_b, i_i, taille = 1, 2, len(vector)

    while i_b < taille:
        if vector[i_b - 1] <= vector[i_b]:
            i_b, i_i = i_i, i_i + 1
        else:
            vector[i_b - 1], vector[i_b] = vector[i_b], vector[i_b - 1]
            i_b -= 1
            if i_b == 0:
                i_b, i_i = i_i, i_i + 1

    return vector


if __name__ == '__main__':
    print(gnome_sort([4, 43, 5, 6, 24, 22, 34, 1, -19]))
