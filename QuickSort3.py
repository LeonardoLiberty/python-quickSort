def QuickSort(array):
    if len(array) > 1:
        p = array[0]
        L, E, G = [], [], []

        while len(array) > 0:
            if array[0] < p:
                L.append(array.pop(0))
            elif array[0] > p:
                G.append(array.pop(0))
            else:
                E.append(array.pop(0))



        QuickSort(L)
        QuickSort(G)
        quick(array, L,E,G)

    else:
         return array


def quick(res, L,E,G):

    if len(L) > 0:
        res.extend(L)
    if len(E) > 0:
        res.extend(E)
    if len(G) > 0:
        res.extend(G)

    return res

if __name__ == '__main__':
    array = [1, 5, 6, 4, 2, 3, 1, 1,10,18]
    print('原：', array)
    QuickSort(array)
    print('现：', array)