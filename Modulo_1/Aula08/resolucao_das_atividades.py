# Calculadora IMC.
def calcular_imc(peso, altura):
    if altura <= 0:
        print("Altura inválida. Não é possível calcular.")
    return 0.0

    imc = peso / (altura * altura)
    return imc 

def obeter_classificacao(imc):
