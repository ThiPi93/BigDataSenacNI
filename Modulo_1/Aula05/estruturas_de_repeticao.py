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

# *** Atividades ***

# 1. Cálculo de Média Escolar para Vários Alunos.
for i in range(10):
    try:
        print(f'Número da chamada:{i+1} de 10')
        n1=float(input('Nota Avaliação 01: '))
        n2=float(input('Nota Avaliação 02: '))
        optativa= float(input('Nota optativa, (digite -1 se não fez): '))

        nota_final_1 = n1
        nota_final_2 = n2

        if optativa != -1:
            menor= min(nota_final_1, nota_final_2)
            maior= max(nota_final_1, nota_final_2)
            media= (optativa+maior)/2
        else:
            media= (nota_final_1+nota_final_2)/2
            print(f'Média final:{media:2f}')

        if media >= 6:
            print('Aprovado')
        elif media < 3:
            print('Reprovado')
        else:
            print('Recuperação')
    except ValueError:
        print('Entrada inválida. Por favor, digite um número.')

# # 2. Cadastro de Candidatos.
# from datetime import date
# ano_atual= date.today().year

# for i in range (12):
#     try:
#         print(f'Número do Candidato: {i+1} de 12')
#         nome= str(input('Insira o seu nome completo: '))
#         ano_nascimento= int(input('Insira o ano de nascimento: '))
#         idade= ano_atual-ano_nascimento
#         if idade < 18:
#             print(f'{nome} tem {idade} anos e não pode participar.')
#             continue
            
#         telefone = input("Telefone: ")
#         email = input("E-mail: ")

#         print(f'{nome} tem {idade} pode participar.')
            
#     except ValueError:
#         print('Entrada inválida. Por favor, digite novamente.')

# # 3. Tentativa de Login e Senha.
# contador = 0
# limite = 3

# usuario_correto = 'Thiago'
# senha_correta = '123'

# while contador < limite:
#     try:
#         print(f"Tentativa {contador+1} de {limite}:")
#         u= str(input("Login: "))
#         s= str(input('Senha: '))
#         usuario = u
#         senha = s

#         if usuario == usuario_correto and senha == senha_correta: #modificar esse if mais tarde para que seja coerente com a pergunta.
#             print('Acesso autorizado. Bem-vindo.')
#             break
#         else:
#             contador += 1
#             tentativas_restantes= limite - contador

#             if tentativas_restantes > 0:
#                 print(f'Senha incorreta. Você ainda tem {tentativas_restantes} tentativa(s).')
#             else:
#                 print('Tentativas esgotadas. Acesso bloqueado.')
#     except ValueError:
#         print("Entrada inválida. Por favor, digite novamente.")
