def quicksort(list):
    if len(list) <= 1:
        return list

    pivot = list[len(list) // 2]
    lt = []
    gt = []
    equal = []

    for a in list:
        if a < pivot:
            lt.append(a)
        elif a > pivot:
            gt.append(a)
        else:
            equal.append(a)

    return quicksort(lt) + equal + quicksort(gt)

if __name__ == "__main__":
    param = [54,26,93,17,77,31,44,55,20]
    print(quicksort(param))
