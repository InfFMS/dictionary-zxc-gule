# Напишите программу, которая получает на вход строку чисел, разделенных пробелами, и формирует словарь,
#  в котором ключами служат числа, а значениями – слово "четное" или "нечетное".
c=str(input())
a=dict()
list2=c.split()
for i in range(len(list2)):
    if (int(list2[i]))%2==0:
        a[list2[i]]='четное'
    else:
        a[list2[i]]='нечетное'
print(a)