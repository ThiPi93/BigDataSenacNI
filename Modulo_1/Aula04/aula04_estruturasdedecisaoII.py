# diadasemana=int(input('Qual dia da semana você quer saber?'))

# if semana == 1:
# print("Domingo")
# elif semana == 2:
# print("Segunda-feira")
# elif semana == 3:
# print("Terça-feira")
# elif semana == 4:
# print("Quarta-feira")
# elif semana == 5:
# print("Quinta-feira")
# elif semana == 6:
# print("Sexta-feira")
# elif semana == 7:
# print("Sábado")
# else: # O 'else' funciona como o 'default'
# print("Dia inválido")
# try:
#     diadasemana=int(input('Qual dia da semana você quer saber?'))

#     match diadasemana:
#         case 1:
#             print('Domingo')
#         case 2:
#             print('Segunda-feira')
#         case 3:
#             print('Terça-feira')
#         case 4:
#             print('Quarta-feira')
#         case 5:
#             print('Quinta-feira')
#         case 6:
#             print('Sexta-feira')
#         case 7:
#             print('Sábado')
#         case _:
#             print('Erro')
# except ValueError:
#     print('Informação invalida')

# #6 Positivo ou Negativo:
# try:
#     numero= int(input('Informe o numero: '))

#     if numero >= 0:
#         print("Positivo")
#     elif numero < 0:
#         print("Negativo")
#     else:
#         print('Erro')
# except ValueError:
#     print('Erro informe valor adequado')

# #2 - Quantidade de Caixas de Azulejos.
# p1=float(input('Parede em metros² 1: '))
# p2=float(input('Parede em metros² 2: '))
# p3=float(input('Parede em metros² 3: '))
# p4=float(input('Parede em metros² 4: '))

# ps=(p1+p2+p3+p4) #Paredes em m²
# cx= 8 #Peças de azulejos por cx
# pecas= 1.5 #Tamanho das peças
# resultado=ps/(cx*pecas)
# print(f'Quantidades de cxs necessárias: {resultado}')

# #3 - Rendimento do Taxista:
# incio=int(input('Informe o número de km no início do dia: '))
# final=int(input('Informe o número de km no final do dia: '))
# valortotal=float(input('Informe o valor total R$ recebido dos passageiros: '))

# valor= 6.15 #preço do combustível litro.
# consumo= final-incio #média de km por dia.
# kml= 11.5 #média km que um carro faz por litro.
# combustivel= consumo/kml #litros de combustível gastos.
# ll= valortotal-(combustivel*valor)
# print(f'Lucro líquido: {ll}')
# ## !!!tirar dúvida com o Douglas: Não entendi 'a média de consumo em km/L'!!!.

# #5 - Média do Aluno com Optativa.
# nota1=float(input('Nota da primeira avaliação: '))
# nota2=float(input('Nota da segunda avaliação: '))
# optativa=float(input('Nota da avaliação optativa (caso não tenha feito forneça o valor -1): '))

# if optativa != -1: #Verifica se a optativa foi feita. O valor -1 é usado como sinalizador de “não fez”. Se for diferente de -1, entramos no bloco de substituição.
#     menor= min(nota1, nota2) #min() retorna o menor valor entre nota1 e nota2. Ex.: se nota1 = 5.0 e nota2 = 2.5, então menor = 2.5.
#     maior= max(nota1, nota2) #max() retorna o maior valor entre nota1 e nota2. Continuando o exemplo: maior = 5.0.
#     media= (optativa+maior)/2
# else:
#     media= (nota1+nota2)/2
#     print(f'Média final: {media:.2f}') #Exibe a média com duas casas decimais. O :.2f formata o número (float) com duas casas — por exemplo 5.5 vira 5.50.
#     #!!! Por que a 'Média final:' não apareceu no resultado!!!

# try:

#     if media >= 6:
#         print('Aprovado')
#     elif meidia < 3:
#         print('Reprovado')
#     else:
#         print('Recuperação')
# except ValueError:
#     print('Entrada inválida. Por favor, digite um número inteiro.')

# 
# #1 - Cálculo de Lâmpadas.

# potencia_lampada= float(input("Potência de cada lâmpada (em watts): "))
# largura= float(input("Largura do cômodo (em metros): "))
# comprimento= float(input("Comprimento do cômodo (em metros): "))

# area= largura * comprimento # área em m²
# potencia_necessaria= area * 3 # 3 watts por m²
# numero_de_bocais= area/3 # Número de bocais por m²
# qtd_lampadas= potencia_necessaria / potencia_lampada

# print(f"Número de lâmpadas necessárias: {qtd_lampadas} unidade(s)")
# #!!! Número de bocais é irrelevante pro cálculo !!!