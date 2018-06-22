def is_pangram(sentence):

    sentence = sentence.lower()

    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    counter = 0

    sentenceList = list(sentence)
    print(sentenceList)
    for i in alphabet:
        if i not in sentenceList:
            print(i)
            counter += 1

    if counter > 0:
        return False
    else:
        return True
