#resolução feita pelo professor
a= int(input('Informe seu primeiro número: '))
b= int(input('Informe seu segundo número: '))
c= int(input('Informe seu terceiro número: '))

primeiro=None
segungo=None
terceiro=None

if a<b and a<c:
    primeiro=a
    if b<c:
        segundo=b
        terceiro=c
    else:
        segundo=b
        terceiro=c
elif b<a and b<c:
     primeiro=b
    if a<c:
        segundo=a
        terceiro=c
    else:
        segundo=c
        terceiro=a
elif c<a and c<b:
     primeiro=c
    if a<b:
        segundo=a
        terceiro=b
    else:
        segundo=b
        terceiro=a
else:
    print('Erro na informação dos númeors')
    
print(f'Ordem{primeiro},{segundo},{terceiro}')