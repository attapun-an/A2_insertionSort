def bubble_sort(numList):
    swap = True
    while swap:
        swap = False
        for i in range(len(numList)-1):
            if numList[i] > numList[i+1]:
                temp = numList[i]
                numList[i] = numList[i+1]
                numList[i+1] = temp
                swap = True

    return numList

listOfNumbers = [23, 14, 96, 57, 2, 32]
meh = bubble_sort(listOfNumbers)
print(meh)
