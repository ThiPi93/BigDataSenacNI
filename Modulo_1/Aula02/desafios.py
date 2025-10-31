#### Desafio 1: Ordenação de Três Números ####

# Recebidos 3 números inteiros, crie um programa que os mostre ordenados em ordem crescente.
# Dica: Este desafio exige que você use estruturas if aninhadas ou uma série de testes
# usando operadores de comparação para determinar qual número é o menor, o do
# meio e o maior.

a=int(input('Informe seu primeiro número: '))
b=int(input('Informe seu segundo número: '))
c=int(input('Informe seu terceiro número: '))

primeiro=None
segundo=None
terceiro=None

if a<b and a<c:  # abc ou acb
    primeiro=a   
    if b<c:      # abc
        segundo=b
        terceiro=c
    else:        # acb
        segundo=c
        terceiro=b
elif b<a and b<c:  # bac ou bca
    primeiro=b
    if a<c:        # bac
        segundo=a
        terceiro=c
    else:          # bca
        segundo=c
        terceiro=a
elif c<a and c<b: # cab ou cba
    primeiro=c
    if a<b:   # cab
        segundo=a
        terceiro=b
    else:     # cba
        segundo=b
        terceiro=a
else:
    print('Erro na informação dos números.')

print(f'Ordem:{primeiro},{segundo},{terceiro}')

#### Desafio 2: Cálculo de Média e Status do Estudante ####

# Dadas as 4 notas de um estudante, calcule sua média e, com base nela, emita a mensagem de status correspondente:
# 1. Aprovado: Média estritamente maior que 7.
# 2. Recuperação: Média entre 5 (inclusive) e 7 (inclusive).
# 3. Reprovação: Média estritamente abaixo de 5.

n1=float(input('Primeira Nota:'))
n2=float(input('Segunda Nota:'))
n3=float(input('Terceira Nota:'))
n4=float(input('Quarta Nota:'))

media=(n1+n2+n3+n4)/4
corte=7

if media > corte:
    print('Aprovado')
elif 5 <= media <= 7:
    print('Recuperação')
elif media < 5:
    print ('Reprovado')
else:
    print('Informe um valor adequado para as notas')

