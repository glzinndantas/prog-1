1.

def calcular_salario(salario_por_hora, horas_trabalhadas):
    salario_total = salario_por_hora * horas_trabalhadas
    return salario_total 

2.

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

resultado1 = (2 * num1) * (num2 / 2)
resultado2 = (3 * num1) + num3
resultado3 = num3 ** 3

print("1) O produto do dobro do primeiro com metade do segundo é:", resultado1)
print("2) A soma do triplo do primeiro com o terceiro é:", resultado2)
print("3) O terceiro elevado ao cubo é:", resultado3)


3.

calcular_operacoes = lambda num1, num2, num3: (
    (2 * num1) * (num2 / 2),
    (3 * num1) + num3,
    num3 ** 3
)

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

resultado1, resultado2, resultado3 = calcular_operacoes(num1, num2, num3)

print("1) O produto do dobro do primeiro com metade do segundo é:", resultado1)
print("2) A soma do triplo do primeiro com o terceiro é:", resultado2)
print("3) O terceiro elevado ao cubo é:",resultado3)


4.

ano = int(input("Digite um ano: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"{ano} é um ano bissexto.")
else:
    print(f"{ano} não é um ano bissexto.")


