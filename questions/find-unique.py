# https://www.codingninjas.com/codestudio/problems/find-unique_625159?source=youtube&campaign=love_babbar_codestudio1&utm_source=youtube&utm_medium=affiliate&utm_campaign=love_babbar_codestudio1

# All elements occur twice but one element occurs only once return that element and it's index

# BRUTEFORCE Approach
def findUnique1(array):
    repeated = []
    for i in range(len(array)):
        element = array[i]
        if element in repeated:
            continue

        timesFound = 0
        for j in range(len(array)):
            if array[j] == element:
                timesFound += 1

        if timesFound == 1:
            return [i, element]
        else:
            repeated.append(element)

    return [-1, -1]


# OPTIMISED
def findUnique2(array):
    ans = 0
    for i in range(len(array)):
        ans = ans ^ array[i]
    
    if ans != 0:
        return [ans, array.index(ans)]
    else:
        return [-1, -1]


if __name__ == '__main__':
    array = [4,3,9,5,7,3,2,9,7,99,5,2,4]
    [index, element] = findUnique2(array)
    if index != -1:
        print(f'{element} is unique element found at index {index}')
    else:
        print('All elements are duplicate')