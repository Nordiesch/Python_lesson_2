# Задание 1
print(type(15 * 3))  # int
print(type(15 / 3))  # float
print(type(15 // 2))  # int
print(type(15 ** 2))  # int


"""
# Задание 2 и 3. Очень много кода. Хотел бы посмотреть более короткий вариант. 
# Можно ли использовать тут метод format для элементов списка с числами. Если да, то как?

list_user = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(id(list_user)) # Проверка на создание нового списка
for el in list_user:
    if el[-1].isdigit():
        if len(el) == 1:
            list_user[list_user.index(el)] = '0' + list_user[list_user.index(el)]
        elif len(el) == 2 and ord(el[0]) < 48:
            list_user[list_user.index(el)] = list_user[list_user.index(el)][0] + '0' + list_user[list_user.index(el)][-1]
ind = 0
while ind < len(list_user):
    if list_user[ind][-1].isdigit():
        list_user.insert(ind + 1, '"')
    ind += 1
ind = 0
list_user = list_user[::-1]
while ind < len(list_user):
    if list_user[ind][-1].isdigit():
        list_user.insert(ind + 1, '"')
    ind += 1
list_user = list_user[::-1]
print(id(list_user)) # Проверка на создание нового списка. id одинаковый 
list_user_str = " ".join(list_user)
print(list_user_str)
"""

"""
# Задание 4
list_personal = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй',
                 'директор аэлита']
# print(id(list_personal)) Проверка на изменение списка
ind = 0
for list_personal[ind] in list_personal:
    name = (list_personal[ind][list_personal[ind].rfind(" ") + 1:]).capitalize()
    print("Привет, " + name + "!")
    ind = ind + 1
# print(id(list_personal)) Проверка на изменение списка. Вывод: не изменился
"""

"""
# Задание 5.а
price_list = [57.8, 46.51, 97, 165, 63.21, 73, 4545.45, 98.2, 20, 100]
all_price_str = []
for el in price_list:
    r = int(el)
    kk = int(el * 100) - int(el) * 100
    price = f"{r} руб {kk:02d} коп"
    all_price_str.append(price)
all_price_str = ",".join(all_price_str)
print(all_price_str)

# Задание 5.b
# print(id(price_list)) Проверка на созданине нового списка после выполнения функции sorted.
print(sorted(price_list))
# print(id(price_list)) Проверка на созданине нового списка после выполнения функции sorted. Список не создался

# Задание 5.с
new_price_list = sorted(price_list)[::-1]
print(new_price_list)

# Задание 5.d
print((sorted(price_list))[(len(price_list) - 1) - 4:])
"""