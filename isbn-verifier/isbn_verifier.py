import re

def verify(isbn):

    newBn = stripToList(isbn)

    if newBn == 'NotValid':
        return False

    if len(newBn) != 10:
        print(len(isbn))
        return False

    if (newBn[0] * 10 + newBn[1] * 9 + newBn[2] * 8 + newBn[3] * 7 + newBn[4] * 6 + newBn[5] * 5 + newBn[6] * 4 + newBn[7] * 3 + newBn[8] * 2 + newBn[9] * 1) % 11 == 0:
        return True
    else:
        return False

def stripToList(n):

    validity = 'Valid'

    if n == '' or not re.match('[0-9X]',n[-1]):
        validity = 'NotValid'

    if validity != 'NotValid' and re.search('[A-Z]',n[:-1]) != None:
        validity = 'NotValid'

    print(validity)

    newList = list(n)

    returnList =[]

    if validity != 'NotValid':
        for i in newList:
            if i != '-' and i != 'X':
                    returnList.append(int(i))
            if i == 'X':
                returnList.append(10)

    if validity != 'NotValid':
        return returnList
    else:
        returnList = 'NotValid'
        return returnList
