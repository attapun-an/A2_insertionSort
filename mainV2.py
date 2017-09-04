listOfNumbers = [23, 14, 96, 57, 2, 32]

def insertion_sort(numList):
    for i in range (1, len(numList)):
        itemToBeInserted = numList[i]
        currItem = i-1
        while numList[currItem] > itemToBeInserted and currItem >= 0:
            numList[currItem+1] = numList[currItem]
            currItem -= 1
        numList[currItem+1] = itemToBeInserted
    return numList

reSort = insertion_sort(listOfNumbers)
print(reSort)
