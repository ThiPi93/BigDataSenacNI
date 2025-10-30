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

#3 - Rendimento do Taxista:
incio=int(input('Informe o número de km no início do dia: '))
final=int(input('Informe o número de km no final do dia: '))
combustivel=int(input('Informe o número de liros de combustível gasto no dia: '))
