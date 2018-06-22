def reverse(n):
    nArr = list(n)
    newArr = ""

    for i in range(len(nArr)-1,-1,-1):
        newArr += nArr[i]

    return newArr
