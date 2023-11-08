def quick_sort(vector):
    if not vector:
        return []
    
    else:
        pivote = vector[-1]
        menor = [x for x in vector if x < pivote]
        mas_grande = [x for x in vector[:-1] if x >= pivote]

        return quick_sort(menor) + [pivote] + quick_sort(mas_grande)
    

if __name__ == '__main__':
    print(quick_sort([3, 5, 2, 6, 19, 1, 0, 7]))

    