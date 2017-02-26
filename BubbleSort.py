
def bubbleSort(myList):
    """
    bubble sort algorithms
    """
    needSwap = True

    while needSwap :
        needSwap = False

        for element in range(len(myList) - 1):
            if myList[element] > myList[element+1]:
                needSwap = True

                #swap
                temp = myList[element]
                myList[element]= myList[element + 1]
                myList[element+1]=temp
    return myList

if __name__ == "__main__" :
    myList = [3,2,7,1,9,4,6]
    sortedList = bubbleSort(myList)
    print(sortedList)
