"""
#Boletim

Aluno1= 5
Aluno2= 7
soma= Aluno1+Aluno2
media= soma/2

print(media)
"""
"""
#Calculadora
numero01=int(input('numero01:' ))
numero02=int(input('numero02:' ))
print (numero01+numero02)
print(numero01*numero02)
print(numero01-numero02)
print(numero01/numero02)
print(numero01%numero02)
"""
'''
numero1=float(input('Diga seu primeiro numero.' ))
numero2=float(input('Diga seu segundo numero.' ))
soma=numero1+numero2
subtracao=numero1-numero2
multi=numero1*numero2
div=numero1/numero2
resto=numero1%numero2
print(f'Soma:',numero1+numero2)
'''

#Ordeneção de três números.

a=int(input("56"))
b=int(input("75"))
c=int(input("258"))
if a <= b and a <= c:
    if b <= c:
        print(a, b, c)
    else:
         print(a, c, b)
elif b <= a and b  <= c:
    if a <= c:
        print(b, a, c)
    else:
        print( b, c, a)
else:
    if a <= b:
        print(c, a, b)
    else:
        print(c, b, a)



a<b and a<c #primeiro
b<c         #segundo
c           #terceiro



#Cáuculo da média e status do estudante.

n1=float(input("7"))
n2=float(input("5.5"))
n3=float(input("6.7"))
n4=float(input("7.3"))

media= (n1+n2+n3+n4)/4
print("Média", media)

if media >= 7:
    print("Status: Aprovado")
elif media >= 5:
    print("Status: Recuperação")
else:
    print("Status: Reprovado")