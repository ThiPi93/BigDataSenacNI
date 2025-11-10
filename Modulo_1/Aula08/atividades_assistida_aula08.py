# def somar(a, b):
#     resultado = a + b
#     return resultado

# print("Calculadora de Somas")

# for i in range(3):
#     print(f"\n --- Calculando {i+1}° par ---")

#     num1 = int(input("Digite primeiro número: "))
#     num2 = int(input("Digite segundo número: " ))
    
#     resultado_da_soma = somar(num1, num2)

#     print(f"A soma de {num1} + {num2} é = {resultado_da_soma}")

# print("\nProgram Finalizado!")

###############################################################################################

import random

def gerar_dados(qtd, min_valor, max_valor):

    lista_de_dados = [random.randint(min_valor, max_valor) for _ in range(qtd)]

    return lista_de_dados

dados_aleatorios = gerar_dados(5, 1, 100)

print(f"Dados gerados: {dados_aleatorios}")

def somar(a, b):
    return a + b
def subtrair(a, b):
    return a - b
def multiplicar(a, b):
    return a  * b
def dividir(a, b):
    if b == 0:
        print("Erro: Divisão por zero não é permitida.")
        return 0
    else:
        return round(a / b, 2)
    
QTD_DE_DADOS = 5

print("Gerando dados...")
lista1 = gerar_dados(QTD_DE_DADOS, 1, 20)
lista2 = gerar_dados(QTD_DE_DADOS, 0, 10)

print(f"Lista 1: {lista1}")
print(f"Lista 2: {lista2}")
print("-"*40)
print("Iniciando Calculo (elemnto a elemento):")

for num1, num2 in zip(lista1, lista2):

    print(f"\nPar: ({num1}, {num2})")

    print(f"Soma: {num1} + {num2} = {somar(num1, num2)}")
    print(f"Subtração: {num1} - {num2} = {subtrair(num1, num2)}")
    print(f"Multiplicação: {num1} * {num2} = {multiplicar(num1, num2)}")
    print(f"Divisão: {num1} / {num2} = {dividir(num1, num2)}")
