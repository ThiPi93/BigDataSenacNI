# #Média Escolar para 5 Estudantes 
# Use um for loop para iterar 5 vezes. Dentro do loop, realize a leitura das notas e a decisão 
# (if/elif/else) da média. Crie uma lista vazia (resultados = []). A cada repetição, adicione uma 
# string (ex: "Aluno 1 - Aprovado") a esta lista usando .append(). 

# print("=== Cálculo de Média Escolar ===")
# resultado = []
# for i in range(5):  # 5 alunos
#     print(f"\nAluno {i + 1}:")
#     try:
#         nota1 = float(input("Digite a primeira nota: "))
#         nota2 = float(input("Digite a segunda nota: "))
#         media = (nota1 + nota2) / 2
#         # Verificação de status
#         if media >= 6:
#             status = "Aprovado"
#         elif media >= 3:
#             status = "Recuperação"
#         else:
#             status = "Reprovado"
        resultado.append(f'\nAluno {i + 1}: {status}')
#         print(f"Média: {media:.2f} - Status: {status}")
        
#     except ValueError:
#         print("Entrada inválida! Digite apenas números para as notas.")
# print(resultado)

# *** Questão 2 ****
#Cadastro Seletivo de Candidatos Use um for loop para iterar 5 vezes. 
# Dentro do loop, use um if/else para checar se o candidato é menor de 18 anos (rejeição).
#  Crie uma lista principal: candidatos_validos = []. 
# Se o candidato for válido, crie um Dicionário (ex: candidato = {'nome': '...', 'email': '...'}). 
# Adicione este Dicionário à lista: candidatos_validos.append(candidato).

# print("\n=== Cadastro de Candidatos ===")
# ano_atual = 2025  # Pode usar datetime.now().year se preferir (aí precisa fazer import datetime)
# candidatos_validos = []

# # from datetime import datetime
# # ano_atual = datetime.now().year


# for i in range(5):  # 12 candidatos
#     print(f"\nCandidato {i+1}:")
#     try:
#         ano_nasc = int(input("Digite o ano de nascimento: "))
#         idade = ano_atual - ano_nasc

#         if idade < 18:
#             print("Não pode participar (menor de 18 anos).")
#             continue  # pula para o próximo candidato
            
#         else:
#             nome = input("Digite seu nome: ")
#             telefone = input("Digite o telefone: ")
#             email = input("Digite o e-mail: ")
#             candidato = {'Candidato':i + 1,'Nome':nome,'Telefone': telefone,'E-mail': email}
#             print(f"Cadastro concluído para candidato {i+1}.")

#             candidatos_validos.append(candidato)
#     except ValueError:
#         print("Ano inválido! Digite apenas números para o ano de nascimento.")
# print(candidatos_validos)
