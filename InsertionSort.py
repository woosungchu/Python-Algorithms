def insertionSort(alist):
    for i in range(1,len(alist)):
        currentValue = alist[i]
        position = i

        while alist[position - 1] > currentValue and position > 0 :
            alist[position] = alist[position - 1]
            position = position -1

        alist[position] = currentValue
    return alist

if __name__ == "__main__":
    alist = [54,26,93,17,77,31,44,55,20]
    print(insertionSort(alist))
