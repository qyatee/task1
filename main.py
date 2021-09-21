n = int(input("Задайте длинну массива\n"))
x = []
S = 0
for i in range(n):
    x.append(int(input("Введите элемент массива с индексом " + str(i) + ": ")))
for i in range(n):
    a = x[i]
    for j in range(i+1, n):
        b = x[j]
        for k in range(j+1, n):
            c = x[k]
            if a+b > c and a+c > b and b+c > a:
                p = (a+b+c)/2
                Spr = (p*(p-a)*(p-b)*(p-c))**0.5
                if Spr >= S:
                    S = Spr
if S:
    print("Площадь наибольшего треугольника равна", S)
else:
    print("Невозможно построить треугольник")
