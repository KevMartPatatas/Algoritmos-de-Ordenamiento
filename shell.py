def tri_insertion(tableau, gap, debut):
    for i in range(gap + debut, len(tableau), gap):
        en_cours = tableau[i]
        j = i

        while j > 0 and tableau[j - gap] > en_cours:
            tableau[j] = tableau[j - gap]
            j = j - gap

        tableau[j] = en_cours

    return tableau


def tri_shell(tableau):
    for grap in [6, 4, 3, 2, 1]:
        for debut in range(grap):
            vector = tri_insertion(tableau, grap, debut)

    print(vector)


if __name__ == '__main__':
    tri_shell([2, 4, 14, 10, 12, 0, 1, -4, 3, 17, 5])

