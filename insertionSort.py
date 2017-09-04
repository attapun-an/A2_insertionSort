listOfNumbers = [23, 14, 96, 57, 2, 32]

def insertion_sort(numList):

    for i in range(1, len(numList)):
        currItem = numList[i]
        y = i
        for y in range(y, 0, -1):
            if currItem < numList[i]:
                numList[y+1] = numList[y]
            if currItem > numList[y]:
                numList[y] = currItem
    return numList

reSort = insertion_sort(listOfNumbers)
print(reSort)
