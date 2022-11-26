a = int(input("Введите номер четверти: "))
if a > 4 or a < 1:
    print("такой четверти нет, введите от 1 до 4")
    a = int(input("Введите номер четверти : "))

if a == 1:
    print("x > 0, y > 0")
if a == 2:
    print("x < 0, y > 0")
if a == 3:
    print("x < 0, y < 0")
if a == 4:
    print("x > 0, y < 0")
