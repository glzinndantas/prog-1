import math

a = int(input("Digite o coeficiente a: " ))
b = int(input("Digite o coeficiente b: " ))
c = int(input("Digite o coeficiente c: " ))

delta = b ** 2 - 4 * a * c 
if delta < 0 :

    print (" não há raizes reais que satisfazem a equação ")

else: 
    x1 = (-b + math.sqrt (delta)) / (2 * a)
    x2 = (-b - math.sqrt (delta)) / (2 * a)

    print ("a raiz x1 = {x1} ")
    print ("a raiz x2 = {x2} ")
