def mobile_display(n, p):
    p = max(p,30)
    n = max(n,20)
    p = n*p
    p = p//100
    lista1 = []
    w1 = int((p/2)-1)
    w2 = int((n-10)/2)
    x = '*' * n
    lista1.append(x)
    for i in range(p-3):
        x2 = '*'+' '*(n-2)+'*'
        lista1.append(x2)
    lista1.append('* Menu'+' '*(n-16)+'Contacts *')
    lista1.append(x)
    if n%2 == 0:
        lista1[w1]='*'+' '*w2+'CodeWars'+' '*w2 +'*'
    else:
        lista1[w1]='*'+' '*w2+'CodeWars '+' '*w2 +'*'
    return '\n'.join(lista1)
