#  Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)


list1 = [1,3,5,7,9,11,12]
max = int(input("Введите максимальное значение диапазона - "))
min = int(input("введите минимальное значение диапазона - "))

res = []

for i in range(len(list1)):
    if list1[i] > min and list1[i] < max:
        res.append(i)
print(res)
