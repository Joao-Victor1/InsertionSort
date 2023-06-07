#InsertionSort
def insertion_sort(array):
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
        
        #Comparar key com cada elemento na esquerda até que um elemento menor que key seja encontrado
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1

        #Posicionar o menor valor:
        array[j + 1] = key

data = [6,3,5,1,7,2,8,4]
insertion_sort(data)
print('\nArray em ordem crescente:')
print(data)


