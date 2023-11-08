import math


def comb_sort(vector):
    permutacion = True
    gap = len(vector)

    while permutacion == True or gap > 1:
        permutacion = False
        gap = math.floor(gap / 1.3)

        if gap < 1 : gap = 1

        for actual in range(0, len(vector) - gap):
            if vector[actual] > vector[actual + gap]:
                permutacion = True

                # Intercambiamos dos elementos
                vector[actual], vector[actual + gap] = vector[actual + gap], vector[actual]

    return vector


if __name__ == '__main__':
    print(comb_sort([4, 3, 6, 74, 31, 46, 6, 19, 56, 14]))
    
