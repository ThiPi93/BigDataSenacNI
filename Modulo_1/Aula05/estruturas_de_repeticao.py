#Usando for (Quando sabemos a contagem: 5 vezes nesse caso)

# for i in range(5):# range começa do zero(0), range será(0, 1, 2, 3, 4,)
#     try:
#         print(f'Número{i+1} de 5:')# é pq o range começa do zero.
#         num= float(input('Digite um número: '))
        
#         dobro= num*2
#         triplo= num*3
#         quadruplo= num*4
#         print(f"Resultado: Dobro={dobro}, Triplo={triplo}, Quádruplo={quadruplo}\n")

#     except ValueError:
#         print("Entrada inválida. Tente novamente.")

# #Usando while (Repetição baseada em Condição)
# print("--- Usando WHILE (Repetição Condicional) ---")

# contador= 0# Inicializamos o contador.
# limite= 5# Definimos o limite.

# while contador < limite: #A condição de parada: Enquanto o contador for menor que 5.
#     try:
#         print(f"{contador+1} de {limite}:")
#         num= float(input('Digite um número: '))

#         dobro= num*2
#         triplo= num*3
#         quadruplo= num*4
#         print(f"Resultado: Dobro={dobro}, Triplo={triplo}, Quádruplo={quadruplo}\n")

#         contador= contador+1# Importantíssimo! Incrementa o contador para evitar loop infinito. Informa que quer um novo ciclo.

#     except ValueError:
#         print("Entrada inválida. Tente novamente.")

# #Usando do-while (Executar primeiro, checar depois)
# print("--- Simulação DO-WHILE (Executa 1° vez, depois checa) ---")

# contador= 0
# limite= 5

# while True: #Loop infinito garantido para executar pelo menos uma vez.
#     if contador>= limite:
#         break# Ponto de DECISÃO: Se o limite for atinfido, usamos 'break' para sair.
#     try:
#         print(f"{contador+1} de {limite}:")
#         num= float(input('Digite um número: '))

#         dobro = num * 2
#         triplo = num * 3
#         quadruplo = num * 4
 
#         print(f" Resultado: Dobro={dobro}, Triplo={triplo}, Quádruplo={quadruplo}\n")

#         contador= contador+1# Incremento.

#     except ValueError:
#         print("Entrada inválida. Tente novamente.")
