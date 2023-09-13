1.

def e_primo(num):
    if num <= 1:
        return False  
    
    for i in range(2, num):
        if num % i == 0:

            print(f"{num} não é primo. É divisível por {i}.")
            return False
    

    return True


numero = int(input("Informe um número: ")) 
if e_primo(numero):
    print(f"{numero} é primo.")
else:
    print(f"{numero} não é primo.")

2.
val_div = float(input("Digite o valor da dívida: "))
parc = 1
juros = 0
print( "Valor dos Juros|Valor Total|Quantidade de Parcelas|Valor da Parcela|"
    
)
while True: 
    juros = (5 / 3) * parc + 5
    if parc == 1:
        juros = 0

    val_ju = val_div * (juros / 100)
    val_total = val_div + val_ju
    valor_parc = val_total / parc
    print(
         f"|R$ {val_ju:.2f}\t\t"
        f"|R$ {val_total:.2f}\t"
        f"|\t\t\t{parc}\t\t\t"
        f"|\t\t\tR$ {valor_parc:.2f}"
    )
    if parc == 1:
        parc -= 1
    parc += 3
    if parc > 12:
        break

3.
n = 1
c1 = 0
c2 = 0
c3 = 0
c4 = 0
while n > 0:
    n = int(input("Digite um número: "))
    if n >= 0 and n <= 25:
        c1 = c1 + 1
    elif n >= 26 and n <= 50:
        c2 = c2 + 1
    elif n >= 51 and n <= 75:
        c3 = c3 + 1
    elif n >= 76 and n <= 100:
        c4 = c4 + 1
print("A quantidade de números entre 0 e 25 é: ", c1) 
print(", entre votos 26-50 é: ", c2) 
print(", entre votos 51-75 é: ", c3) 
print(", e entre votos 76-100 é: ", c4)


