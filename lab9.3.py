cars = {
    'mers':1000,
    'bmw':1050,
    'mazda': 700,
    'ford': 890,
    'lexus':800,
    'camry':1500,
    'shkoda': 40,
}

name = input('Введите название автомобиля, для проверки его налиция в системе: ')
flag = False
for i in cars:
    if name == i:
        flag = True
        
print('Машина есть в системе' if flag else "Машины нет в системе")

name = input('Введите название автомобиля, которого хотите добавить в систему: ')
price = int(input('Введите цену автомобиля, которого хотите добавить в систему: '))
cars[name] = price

name = input('Введите название автомобиля, для получения его цены: ')
flag = False
car_price = 0
for i in cars:
    if name == i:
        car_price = cars[i]
        flag = True
        
print(f'Цена автомобиля состовляет: {car_price}' if flag else "Машины нет в системе")