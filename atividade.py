'''maior = menor =0
for x in range (10):
    valor = int(input("Entre com x: "))
    soma= 0
    soma = soma +valor
    if x ==0:
        maior=valor
        menor=valor
    elif x > maior:
        maior=valor
    elif x <menor:
        menor = valor
print(f"O valor maior é:{maior}")
print(f"O valor menor é:{menor}")
print(soma)
media = soma/10
print(media)'''

'''soma = 0
quantidade = 20
for i in range(quantidade):
    valor = float(input(f"Digite o {i+1}° valor: "))
    soma += valor

media = soma / quantidade

print(f"Soma dos valores: {soma}")
print(f"Média dos valores : {media}")'''


'''for i in range(0,21,2):
    print(i)

for i in range(1, 21, 2):
        print(i)'''

'''soma = 0
for i in range(0,21,2):
    soma += i


print("Soma dos valores pares:",soma)'''


'''soma = 0
quantidade = 10
for i in range(quantidade):
    valor = float(input(f"Digite o {i+1}° valor: "))
    if valor % 2 == 0:
        soma += valor
print(f"soma dos valores é={soma}")'''



'''quantidade = 10
for i in range(quantidade):
    idade = int(input(f"Insira a {i+1}°:  "))

    if 5 <= idade <= 7:
        print(f"Pessoa {i + 1}: Infantil A")
    elif 8 <= idade <=11 :
        print(f"Pessoa {i + 1}: Infantil B")
    elif 12 <= idade <=13 :
        print(f"Pessoa {i + 1}: Juvenil")
    else:
        print(f"Pessoa {i + 1}: Outra categoria")'''



'''soma = 0
numero = None

while numero != 0:
    numero = int(input("Digite um número inteiro (digite 0 para sair): "))
    soma += numero

print("A soma de todos os números informados é:", soma)'''




'''valor = None
while True:
    numero = int(input("Digite um número inteiro (ou 0 para encerrar): "))

    if numero == 0:
        break  #

    if valor is None or numero > valor:
        valor = numero

if valor is not None:
    print(f"O maior valor digitado foi: {valor}")
else:
    print("Nenhum valor foi digitado.")'''



'''soma = 0
contador = 0

while True:
    numero = int(input("Digite um número inteiro (0 para sair): "))

    if numero == 0:
        break

    soma += numero
    contador += 1

if contador == 0:
    print("Nenhum número foi digitado.")
else:
    media = soma / contador
    print(f"Soma dos valores digitados: {soma}")
    print(f"Média dos valores digitados: {media}")'''





'''soma = 0
numero = None

while True:
    numero = int(input("Digite um número inteiro (0 para sair): "))

    if numero == 0:
        break

    if numero % 2 == 0:
        soma += numero

print(f"A soma dos valores pares é: {soma}")'''

'''idades = []

while True:
    idade = int(input("Digite a idade (ou um número negativo para parar): "))

    if idade < 0:
        break

    idades.append(idade)

if not idades:
    print("Nenhuma idade foi inserida.")
else:
    maior_idade = max(idades)
    menor_idade = min(idades)
    soma_idades = sum(idades)
    media_idades = soma_idades / len(idades)

    print("Maior idade:", maior_idade)
    print("Menor idade:", menor_idade)
    print("Soma das idades:", soma_idades)
    print("Média das idades:", media_idades)'''



'''numero = int(input("Digite o número para o qual deseja calcular a tabuada: "))
contador = 1

while contador <= 10:
    resultado = numero * contador
    print(f"{numero} x {contador} = {resultado}")
    contador += 1'''

def Soma(x,y):
    print(x+y)

def Sub(x,y):
    print(x-y)

def Mult(x, y):
    print(x * y)

def dividir(x, y):
            print(x / y)
valor1 = int(input("Entre com valor 1 : "))
valor2 = int(input("Entre com valor 2 : "))

Soma(valor1,valor2)
Sub(valor1,valor2)
Mult(valor1,valor2)
dividir(valor1,valor2)




