'''
+Открыть фалй citys и загрузить в переменную (список)
+Сделать список в нижнем регистре
+сделать список с повтерениями (пустой)
Запрос города (str). Перевод в нижний регистр
сделать цикл
  - проверка в списке повторений
  - проерка в списке городов. При совпадении взять индекс и удалить город из списка
  - добавить в список повторений
  - Взть последнюю букву из введенного города в перемменную и слелать проход на поиск городов ничинающихся на эту букву в citys.
  - Сообщить "Отлично, такой город сущестовует /n Мне город на {последня буква в верхнем регистре}"
  - Произвести поиск по списку citys и найти слова начинающиеся на нужную букву.
  - Занести слово в список повторений и удалить из списка citys
  - Вывести сообщение "Я называю город {город}. Тебе на {последня буква в верхнем регистре}"

'''
citys_repeat = []
import os
with open('citys_list') as f:
    city_file = f.readlines()
citys_upper = list(map(lambda x:x.strip(), city_file))
citys = [element.lower() for element in citys_upper] ; citys_upper
last_liter = ''
def check_city(input):
    global citys
    global citys_repeat
    global last_liter
    input = str(input)
    input_lower = input.lower()
    if input_lower in citys:
        if input_lower[0] == last_liter or last_liter == None or last_liter == '':
           print(f"Город {input_lower} есть в России")
           citys_repeat.append(input_lower)
           citys.remove(input_lower)
           if input_lower[-1] == 'ь' or input_lower[-1] == 'ъ' or input_lower[-1] == 'й' or input_lower[-1] == 'ц':
               city_last_litter = input_lower[-2]
               print(f"Мне город на: {city_last_litter}")
           else:
               city_last_litter = input_lower[-1]
               print(f"Мне город на: {city_last_litter}")
           new_city = [idx for idx in citys if idx[0].lower() == city_last_litter.lower()]
           new_city = new_city[0]
           citys_repeat.append(new_city)
           citys.remove(new_city)
           if new_city[-1] == 'ь' or new_city[-1] == 'ъ' or new_city[-1] == 'й' or new_city[-1] == 'ц':
               last_liter = new_city[-2]
           else:
               last_liter = new_city[-1]
           print(f"CHECK_CITY Мой ответ: {new_city}, тебе на: {last_liter}")
        elif input_lower[0] != last_liter:
           print(f"Город {input_lower} не начинается на {last_liter} Попробуй еще раз!")
    else:
        print(f"Города {input_lower} нет в России. Попробуй еще раз!")

while True:
    city_input = input('Введите город: \n')
    city_input = city_input.lower()
    print(f"PRINT IN WHILE {city_input}")
    print(last_liter)
    if city_input in citys:
        check_city(city_input)
    elif city_input in citys_repeat:
        print(f"Город {city_input} уже был! Попробуй еще раз")
    else:
        print(f"Город {city_input} не существует! Попробуй еще раз!")

