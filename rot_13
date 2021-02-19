def rot13(message):

    big = list(chr(x) for x in list(range(65,  91)))
    low = list(chr(x) for x in list(range(97, 123)))
    s = ''
    for i in message:
        if i.islower():
            a = (low.index(i)+13)%26
            s += low[a]
        elif i.isupper():
            a = (big.index(i)+13)%26
            s += big[a]
        else:
            s += i
    return s
