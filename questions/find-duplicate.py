# https://www.codingninjas.com/codestudio/problems/duplicate-in-array_893397?source=youtube&campaign=love_babbar_codestudio1&utm_source=youtube&utm_medium=affiliate&utm_campaign=love_babbar_codestudio1


def findDuplicate(array):
    for i in range(len(array)):
        timesFound = 0
        element = array[i]
        for j in range(len(array)):
            if array[j] == element:
                timesFound += 1

        if timesFound > 1:
            return element
    return None


array = [1,2,3,4,5,6,7,7,8,9]
answer = findDuplicate(array);
print(f'duplicate element is {answer}') if answer != None else print('None is duplicate')
