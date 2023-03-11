# https://www.codingninjas.com/codestudio/problems/find-unique_625159?source=youtube&campaign=love_babbar_codestudio1&utm_source=youtube&utm_medium=affiliate&utm_campaign=love_babbar_codestudio1

# All elements occur twice but one element occurs only once return that element and it's index

def findUnique(array):
    repeated = []
    for i in range(len(array)):
        if array[i] in repeated:
            continue
        timesFound = 0
        for j in range(len(array)):
            if array[i] == array[j]:
                timesFound += 1
        if timesFound == 1:
            return [i, array[i]]
        else:
            repeated.append(array[i])
    return [-1, -1]


if __name__ == '__main__':
    array = [4,3,9,5,7,3,2,9,7,99,5,2,4]
    [index, element] = findUnique(array)
    if index != -1:
        print(f'{element} is unique element found at index {index}')
    else:
        print('All elements are duplicate')