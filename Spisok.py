#Задание 1
#В списке целых, заполненном случайными числами, определить
#минимальный и максимальный элементы, посчитать количество
#отрицательных элементов, посчитать количество положительных элементов,
#посчитать количество нулей. Результаты вывести на экран.


spisok = [1,2,3,4,5,0,0,-1,-2,-3,-4]
min_spisok = min(spisok)
max_spisok = max(spisok)
otric_element = sum(1 for x in spisok if x < 0)
poloj_element = sum(1 for x in spisok if x > 0)
nulevyx_element = sum(1 for x in spisok if x == 0)
print(spisok)
print("минимальный элемент", min_spisok)
print("максимальный элементы ", max_spisok)
print("количество отрицательных элементов", otric_element)
print("количество положительных элементов", poloj_element)
print("количество нулевых элементов", nulevyx_element)

# Задание 2
# Напишите программу, которая удаляет дубликаты из списка.

spisok_1 = [1, 2, 2, 3,3,4, 4, 2,5,6,7,7,8,9,10,10]
spisok_2 = list(set(spisok_1)) # использовали внутреннию функцию set()
print("Начальный список:", spisok_1)
print( "После удаления дублей:", spisok_2)



