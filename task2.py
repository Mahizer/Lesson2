# 2. Для списка реализовать обмен значений соседних элементов,
# т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().


my_list = []
print('Чтобы выйти из программы введите ноль')
i = 0
z = 0
while True:
    user_input = int(input('Введите значение элемента: '))
    if user_input == 0:
        break
    my_list.append(user_input)

print(my_list)
while i != len(my_list):
    if len(my_list) >= 2 and len(my_list) % 2 == 0:
        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
        i += 2
    elif len(my_list) % 2 == 1:
        z = my_list[-1]
        del my_list[-1]
if z != 0:
    my_list.append(z)

print(my_list)





