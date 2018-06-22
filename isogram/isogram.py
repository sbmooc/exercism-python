def is_isogram(string):
    string = strip(string)
    doubled = 0

    for i in string:
        if string.count(i) > 1:
            doubled += 1

    if doubled > 0:
        return False
    else:
        return True

def strip(n):
    string = n.lower()
    string = string.replace(" ","")
    string = string.replace("-","")
    return string
