#1. Controle de Pesca.
dias_de_pesca = 5
for i in range(5):
    try:
        peso_total = float(input("Peso dos peixes pescados (em KG): "))
        peso_limite = 100
        calcular_multa = (peso_total-peso_limite)*4

        if peso_total <= peso_limite:
            print("Valor da multa: 0.0")
            print("Peso dentro do limite. Nenhuma multa a pagar.")
            break
        elif peso_total > peso_limite:
            multa = print(f"Valor da multa a ser pago em R$: {calcular_multa}")
    except TypeError:
        print("Erro! Digite um valor aceitável")