# Напишите программу, которая получает на вход строку и подсчитывает, 
# сколько раз в ней встречается каждый символ (независимо от регистра).
# Результат нужно вывести без фигурных скобок
# Пример. 
# ввод:
# Абракадабра
# Вывод
# а-5 б-2 д-1 к-1 р-2
c=str(input())
c=c.lower()
a=dict()
b=list(c)
n=set(b)
n=list(n)
k=0
for i in range(len(n)):
    for l in range(len(b)):
        if b[l]==n[i]:
            k+=1
    a[n[i]]=k
    k=0
a=str(a)
a=a.replace('{','')
a=a.replace('}','')
a=a.replace(',','')
a=a.replace(': ','-')
a=a.replace("'",'')
print(a)