# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень). 4
# Напишите решения через list и через dict.

print('Чтобы завершить программу введите ноль')
user_input = int(input('Введите число от 1 до 12: '))

months = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь',
          'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']

seasons = ['зима', 'весна', 'лето', 'осень']
while 0 < user_input <= 12:
    if user_input == 1 or user_input == 2 or user_input == 12:
        print(seasons[0])
    elif user_input == 3 or user_input == 4 or user_input == 5:
        print(seasons[1])
    elif user_input == 6 or user_input == 7 or user_input == 8:
        print(seasons[2])
    else:
        print(seasons[3])
    user_input = int(input('Введите число от 1 до 12: '))