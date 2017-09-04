def bubble_sort(numList):
    for i in range(0, len(numList)-1):
        swap = False
        while swap == True:

        if numList[i] > numList[i+1]:
            temp = numList[i]
            numList[i] = numList[i+1]
            numList[i+1] = temp
            swap = True

    return numList

listOfNumbers = [23, 14, 96, 57, 2, 32]
meh = bubble_sort(listOfNumbers)
print(meh)
