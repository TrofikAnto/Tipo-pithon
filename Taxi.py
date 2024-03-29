def taxi(distance):
    return(round((base + add * distance/150), 2))
base = 45
add = 17
distance = int(input("Введите расстояние в метрах: "))
print('Стоимость будет: ', taxi(distance))