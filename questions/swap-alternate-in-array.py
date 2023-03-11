def swap_alternate(array):
    for i in range(0, len(array), 2):
        if i+1 >= len(array):
            break
        temp = array[i]
        array[i] = array[i+1]
        array[i+1] = temp
    return array

if __name__ == '__main__':
    array = [1,2,3,4,5,6,7]
    swapped = swap_alternate(array)
    print(swapped)