a = int(input(" Введите день недели: "))
if 0 < a < 6:
    print("Будни")
elif 5 < a < 8:
    print("Выходной")
else:
    print("Нет такого дня недели!")

