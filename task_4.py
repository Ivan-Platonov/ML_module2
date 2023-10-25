print('Задача 4. Информация о пользователе')

# Что нужно сделать
# Напишите программу, которая запрашивает некоторые данные у пользователя,
# затем выведите их на экран, как показано ниже.
# Данные должны лежать в разных переменных.
#
# Вариант 1. Запросите имя и фамилию и выведите их на экран построчно.
# Результат должен быть таким (с вашим именем и фамилией, конечно):
# Пример первого варианта:

# Введите имя: Роман
# Введите фамилию: Булгаков
# Вас зовут
# Роман
# Булгаков

# Вариант 2. Запросите имя, фамилию и город проживания,
# затем выведите их на экран в две строки: первая — «Вас зовут» и далее имя и фамилия,
# вторая — «Вы живёте в городе» и далее город.
# Для красоты отделите в консоли ввод и вывод данных, как в примере:
# Пример второго варианта:

# Введите имя: Роман
# Введите фамилию: Булгаков
# Введите город проживания: Москва
# ==========
# Вас зовут: Роман Булгаков
# Вы живете в городе Москва

firstname, lastname, city = ('', ) * 3

while firstname.strip() == '':
  firstname = input('Введите свое имя: ')
while lastname.strip() == '':
  lastname = input('Введите свою фамилию: ')
while city.strip() == '':
  city = input('В каком городе вы живете: ')

print('Вас зовут: ', firstname, lastname)
print('Вы живете в городе: ', city)
