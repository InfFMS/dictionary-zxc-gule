# Представьте, что вы шпионы)
# Придумайте шифр, в котором буквы заменяются на какие-то символы
# и реализуйте шифроватор и дешифроватор
shifr={'т':'(', 'а':':', 'н':'|', 'к':';', 'и':')', 'е':'^', 'о':'#', 'ъ':'*', ' ':'/'}
deshifr={v: k for k, v in shifr.items()}
def shifrat(shifr):
    while True:
        res=[]
        a=input()
        for i in a:
            if i in shifr:
                res.append(shifr[i])
        print(''.join(res))
        if a=='exit':
            break
def deshifrat(deshifr):
    while True:
        res=[]
        a=input()
        for i in a:
            if i in deshifr:
                res.append(deshifr[i])
        print(''.join(res))
        if a=='exit':
            break
while True:
    com=input('shifrat or deshifrat?')
    if com=='shifrat':
        shifrat(shifr)
    elif com=='deshifrat':
        deshifrat(deshifr)