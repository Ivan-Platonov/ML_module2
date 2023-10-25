print('Задача 6. Полёт')

# Что нужно сделать
# Напишите программу для сервиса заказа билетов,
# которая запрашивает у пользователя город вылета и город прилёта. 
# Затем выведите их в одну строку через тире. 
# Обратите внимание на свои переменные: названия должны отражать содержимое.

outcomming_city, incoming_city =  ('',) * 2

while outcomming_city.strip() == '':
  outcomming_city = input('Введите город вылета: ')
while incoming_city.strip() == '':
  incoming_city = input('Введите город придета: ')
print('')
print(outcomming_city, '-', incoming_city)
