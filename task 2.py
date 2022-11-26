x = int(input("Введите чило x: "))
y = int(input("Введите чило y: "))
z = int(input("Введите чило z: "))

if not(x or y or z) == (not(x) and not(y) and not(z)):
    print(True)
else:
    print(False)