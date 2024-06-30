# Задание 1
# Пользователь вводит с клавиатуры три числа. В зависимости от выбора пользователя программа выводит
# на экран сумму трёх чисел или произведение трёх чисел.

num1 = int(input("введите число 1\n"))
num2 = int(input("введите число 2\n"))
num3 = int(input("введите число 3\n"))
all = [num1, num2, num3]

c = int(input("выберите действие: 1 найти сумму трёх чисел, 2 найти  произведение трёх чисел,  \n"))

proizv = num1 * num2 * num3

if c == 1:
 print ('сумма трех чисел :', sum(all))
elif c == 2:
    print ('произведение трёх чисел:', (proizv))

# # Задание 2
# # Пользователь вводит с клавиатуры три числа. В зависимости от выбора пользователя программа выводит
# # на экран максимум из трёх, минимум из трёх или среднеарифметическое трёх чисел.
#
num4 = int(input("введите число 1\n"))
num5 = int(input("введите число 2\n"))
num6 = int(input("введите число 3\n"))
all = [num4, num5, num6]

c = int(input("выберите действие: 1 найти максимум, 2 найти минимум, 3 найти среднее \n"))

if c == 1:
    print ('Максимум из 3х:', max(all))
elif c == 2:
    print ('Минимум из 3х:', min(all))
elif c == 3:
    print('Среднее из 3х:', sum(all) / len(all))
else:
    print("введите число от 1 до 3")

# # Задание 3
# Пользователь вводит с клавиатуры количество метров. В зависимости от выбора пользователя программа
# переводит метры в мили, дюймы или ярды.


from tkinter import *
root = Tk()
var=IntVar()
root.title('Конвертер')
root.geometry('700x350')
a = Label(text = 'Введите количество метров', font = 'arial 16')
a.pack()
def convert(name, index, mode):
  c.delete(0,END)
  if text.get() == "":
    return
  value = float(text.get())
  if   var.get() == 1:
    value = value*0.000621371
  elif var.get() == 2:
    value = value*1.09361
  elif var.get() == 2:
    value = value*3.28084
  elif var.get() == 4:
    value = value*39.3701
  c.insert(0,str(value))
text = StringVar()
text.trace("w", convert)
b = Entry(fg = 'black', bg = 'white', width = 12, font = 'arial 13', textvariable=text)
b.pack()
var = IntVar(root)
var.set(1)
var.trace("w", convert)
r1 = Radiobutton(root, text='миля', font='arial 12', variable=var, value=1)
r2 = Radiobutton(root, text='ярд', font='arial 12', variable=var, value=2)
r3 = Radiobutton(root, text='фут', font='arial 12', variable=var, value=3)
r4 = Radiobutton(root, text='дюйм', font='arial 12', variable=var, value=4)
r1.pack()
r2.pack()
r3.pack()
r4.pack()
c = Entry(fg = 'black', bg = 'white', width = 12, font = 'arial 13')
c.pack()
root.mainloop()