# with open(r'C:\Users\Eduard\Desktop\Учеба\ДЗ\Python\18.06.2024/DD.txt', 'r',
#           encoding='utf-8') as f:
#     data = f.read()
# print(data)

# with open(r'C:\Users\Eduard\Desktop\Учеба\ДЗ\Python\18.06.2024/DD.txt', 'r', encoding='utf-8') as ile:
#     print('\nСергей Леонов, 11:18, 12:23', file=file)

# def read_file(s):
#    with open(r'C:\Users\Eduard\Desktop\Учеба\ДЗ\Python\18.06.2024/DD.txt', 'r',
#           encoding='utf-8') as f:
#       txt = f.read()
#    return txt
#
# print(read_file)
# import sys
# def process_data(data):
#     processed_data = data * 2
#     return processed_data
# for line in sys.stdin:
#     data = float(line.strip())
# print(processed_data)
# import os
# new_dir = 'NewProjects'
# parent_dir =  r'C:\Users\Eduard\Desktop\Учеба'
# path = os.path.join(parent_dir, new_dir)
# os.mkdir(path)
# print(f'Директория {new_dir} создана: {os.listdir()}')

# with open(r'C:\Users\Eduard\Desktop\Proga\first.txt', 'r', encoding='utf-8') as file1, \
# open(r'C:\Users\Eduard\Desktop\Proga\second.txt', 'r', encoding='utf-8') as file2:
#     for line_x, line_y in zip(file1, file2):
#         print(f'Сотрудник {line_x.strip()}, должность - {line_y.strip()}')

# income, outcome = 0, 0
# with open(r'C:\Users\Eduard\Desktop\Proga\income.txt', 'r', encoding='utf-8') as file1, \
# open(r'C:\Users\Eduard\Desktop\Proga\outcome.txt', 'r', encoding='utf-8') as file2:
#     for line in file1:
#         num = line.strip()[3:]
#         income += int(num)
#
#     for line in file2:
#         num = line.strip()[4:]
#         outcome += int(num)
# print(f'Прибыль за прошлый месяц: {income - outcome} RUB')

# import datetime
# import itertools
# from typing import NamedTuple
#
#
# class Card(NamedTuple):
#     name: str = None
#     phys_damage: int = 0
#     hp: int = 0
#     mage_damage: int = 0
#     armor: int = 0
#     add_hp: int = 0
#
#     def __repr__(self):
#         """repr у нас будет показывать только аргументы, которые отличаются от умолчательных"""
#         defaults = type(self)._field_defaults
#         params = ', '.join(
#             f'{k}={v!r}'
#             for k, v in self._asdict().items()
#             if k in defaults and v != defaults[k]
#         )
#         return f'{type(self).__name__}({params})'
#
#     def __str__(self):
#         return f'<{self.name}#{id(self)}>'
#
#     @property
#     def total_hp(self):
#         return self.hp + self.add_hp
#
#     @property
#     def group(self):
#         return max(
#             (self.mage_damage, 'Intelegence'),
#             (self.add_hp, 'Strength'),
#             (self.armor, 'Agility'),
#         )[1]
#
#
# class Deck():
#     def __init__(self, deck_name="Колода", date=None, cards=None):
#         self.deck_name = deck_name
#         self.date = date or datetime.now()
#         self.cards = cards or []
#
#     def __iter__(self):
#         return iter(self.cards)
#
#     def by_group(self):
#         return itertools.groupby(self, lambda card: card.group)
#
#
# my_deck = Deck("Моя колода", "24.05.2022", [
#     Card("черви", phys_damage=32, hp=600, mage_damage=100),
#     Card("бубны", phys_damage=40, hp=600, mage_damage=60),
#     Card("пик", phys_damage=80, hp=600, add_hp=150),
#     Card("треф", phys_damage=60, hp=600, armor=10),
# ])
#
# for group, cards in my_deck.by_group():
#     print(f'# {group}:')
#     for card in cards:
#         print(f'\t{card!r}')
#


# Написать программу «успеваемость». Пользователь
# вводит 10 оценок студента. Оценки от 1 до 12. Реализовать
# меню для пользователя:
# ■ Вывод оценок (вывод содержимого списка);
# ■ Пересдача экзамена (пользователь вводит номер элемента списка и новую оценку);
# ■ Выходит ли стипендия (стипендия выходит, если
# средний бал не ниже 10.7);
# ■ Вывод отсортированного списка оценок: по возрастанию или убыванию.


program = []
for i in range(1, 11):
    b = 0
    while b < 1 or b > 12:
        try:
         b = int(input('Введите'f'{ i} оценку: '))
        except:
         b = 0
    program.append(b)
#
grade = 0
while grade == 0:
    print('\n1. Вывод списка оценок', '2. Пересдача экзамена', '3. Выходит ли стипендия',
          '4. Сортировка оченок по возрастанию', '5. Сортировка оченок по убыванию', '6. Выход', '\n', sep='\n')
    try:
        grade = int(input())
        if grade == 1:
            for i, val in enumerate(program):
                print(i + 1, ' - ', val)
        elif grade == 2:
            try:
                index = int(input('Введите номер экзамена: '))
                val = int(input('Введите оценку: '))
                if val > 0 and val < 13:
                    program[index - 1] = val
                    print('Оценка изменена')
            except:
                print('Ошибка!')
                grade = 0
        elif grade == 3:
            if sum(program) / len(program) >= 10.7:
                print('Стипендия выходит :)')
            else:
                print('Стипендия не выходит :(')
        elif grade == 4:
            print(sorted(program))
        elif grade == 5:
            print(sorted(program, reverse=True))
        if grade != 6:
            grade = 0
    except:
        grade = 0










# score = []
# for i in range(1, 11):
#     b = 0
#     while b < 1 or b > 12:
#         try:
#             b = int(input(f'{i} оценка: '))
#         except:
#             b = 0
#     score.append(b)
#
# option = 0
# while option == 0:
#     print('\n1. Вывод списка оценок', '2. Пересдача экзамена', '3. Выходит ли стипендия',
#           '4. Сортировка оченок по возрастанию', '5. Сортировка оченок по убыванию', '6. Выход', '\n', sep='\n')
#     try:
#         option = int(input())
#         if option == 1:
#             for i, val in enumerate(score):
#                 print(i + 1, ' - ', val)
#         elif option == 2:
#             try:
#                 index = int(input('Введите номер экзамена: '))
#                 val = int(input('Введите оценку: '))
#                 if val > 0 and val < 13:
#                     score[index - 1] = val
#                     print('Оценка изменена')
#             except:
#                 print('Ошибка!')
#                 option = 0
#         elif option == 3:
#             if sum(score) / len(score) >= 10.7:
#                 print('Стипендия выходит :)')
#             else:
#                 print('Стипендия не выходит :(')
#         elif option == 4:
#             print(sorted(score))
#         elif option == 5:
#             print(sorted(score, reverse=True))
#         if option != 6:
#             option = 0
#     except:
#         option = 0

