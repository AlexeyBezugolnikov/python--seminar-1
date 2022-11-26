x = int(input("Введите чило x: "))
y = int(input("Введите чило y: "))
if x == 0 or y == 0:
    print("Введите число не равное '0' ")
    x = int(input("Введите чило x: "))
    y = int(input("Введите чило y: "))
if x > 0 and y > 0:
    print("Первая четверть")
if x < 0 and y > 0:
    print("Вторая четверть")
if x < 0 and y < 0:
    print("Третья четверть")
if x > 0 and y < 0:
    print("Четвертая четверть")
