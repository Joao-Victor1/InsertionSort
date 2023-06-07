//InsertionSort
function insertionSort(array){
    for(let i = 1; i < array.length; i++){
        //Armazenar elemento do array desordenado
        let key = array[i];
        let j = i - 1
        while((j > -1) && (key < array[j])){
            array[j+1] = array[j];
            j--;
        }
        array[j+1] = key;
    }

    return array;
}

let array = [6,5,1,8,7,2,3,4];
insertionSort(array);
console.log(array);