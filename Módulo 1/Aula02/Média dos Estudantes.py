n1=float(input('Priemria Nota: '))
n2=float(input('Segunda Nota: '))
n3=float(input('Terceira Nota: '))
n4=float(input('Quarta Nota: '))

media=(n1+n2+n3+n4)/4
corte=7

if media > corte:
    print('Aprovado')
elif media >= 5 and media <= 7:
    print('Recuperação')
elif meida < 5:
    print('Reprovado')
else:
    print('Informe um valor adequado')