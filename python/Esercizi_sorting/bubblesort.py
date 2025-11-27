
from stopwatch import Timer


def swap(lista: list[int], j:int, i:int) -> list[int]:
    lista[i], lista[j] = lista[j], lista[i]
    return lista
    

def bubblesort(lista: list[int]) -> list[int]:

    ordered: bool = True

    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] > lista[j]:
                ordered = False
                swap(lista, j, i)
            
        if ordered:
            return lista
    
    return lista


if __name__ == '__main__':

    #list = [3,5,1,4,2,6,4,67,2,8,6,13,35,7,5,7,47,4,7,47,4,643,6,]

    list1 = [1, 2, 3, 4]
    

    with Timer():
        print(bubblesort(list1))