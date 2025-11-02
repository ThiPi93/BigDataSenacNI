# ==============================================================================
# ESTRUTURAS DE DECISÃO EM PYTHON: IF/ELSE E MATCH/CASE
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. CÁLCULO DE LÂMPADAS (IF/ELSE para Arredondamento)
# ------------------------------------------------------------------------------
print("--- 1. CÁLCULO DE LÂMPADAS ---")
try:
    potencia_lampada = float(input("Potência de uma lâmpada (W): "))
    largura = float(input("Largura do cômodo (m): "))
    comprimento = float(input("Comprimento do cômodo (m): "))
    
    area = largura * comprimento
    potencia_total_necessaria = area * 3 
    
    num_lampadas_float = potencia_total_necessaria / potencia_lampada
    num_lampadas_inteiro = int(num_lampadas_float)
    
    if num_lampadas_float > num_lampadas_inteiro:
        num_lampadas_final = num_lampadas_inteiro + 1
    else:
        num_lampadas_final = num_lampadas_inteiro
        
    print(f"Resultado:\n  Área: {area:.2f} m²")
    print(f"  Lâmpadas necessárias: {num_lampadas_final}\n")
    
except ValueError:
    print("ERRO: Por favor, digite apenas números válidos.")
except ZeroDivisionError:
    print("ERRO: A potência da lâmpada não pode ser zero.")

# ------------------------------------------------------------------------------
# 2. QUANTIDADE DE CAIXAS DE AZULEJOS (IF/ELSE para Arredondamento)
# ------------------------------------------------------------------------------
print("--- 2. CAIXAS DE AZULEJOS ---")
try:
    AREA_CAIXA = 1.5
    
    comprimento = float(input("Comprimento da cozinha (m): "))
    largura = float(input("Largura da cozinha (m): "))
    altura = float(input("Altura da cozinha (m): "))
    
    area_total_paredes = (2 * comprimento * altura) + (2 * largura * altura)
    num_caixas_float = area_total_paredes / AREA_CAIXA
    
    num_caixas_inteiro = int(num_caixas_float)
    
    # Lógica de Arredondamento (IF/ELSE)
    if num_caixas_float > num_caixas_inteiro:
        num_caixas_final = num_caixas_inteiro + 1
    else:
        num_caixas_final = num_caixas_inteiro
        
    print(f"Resultado:\n  Área total: {area_total_paredes:.2f} m²")
    print(f"  Caixas necessárias: {num_caixas_final}\n")

except ValueError:
    print("ERRO: Por favor, digite apenas números válidos.")

# ------------------------------------------------------------------------------
# 3. RENDIMENTO DO TAXISTA (IF/ELSE para prevenir ZeroDivisionError)
# ------------------------------------------------------------------------------
print("--- 3. RENDIMENTO DO TAXISTA ---")
try:
    PRECO_COMBUSTIVEL = 6.15
    
    km_inicial = float(input("Odômetro inicial (km): "))
    km_final = float(input("Odômetro final (km): "))
    litros_gastos = float(input("Litros de combustível gastos: "))
    valor_recebido = float(input("Valor total recebido (R$): "))

    distancia_percorrida = km_final - km_inicial
    custo_combustivel = litros_gastos * PRECO_COMBUSTIVEL
    lucro_liquido = valor_recebido - custo_combustivel
    
    # PONTO DE DECISÃO: Prevenção de divisão por zero (IF/ELSE)
    if litros_gastos > 0:
        media_consumo = distancia_percorrida / litros_gastos
    else:
        media_consumo = 0.0
        
    print(f"Resultado:\n  Média de Consumo: {media_consumo:.2f} km/L")
    print(f"  Lucro Líquido: R$ {lucro_liquido:.2f}\n")

except ValueError:
    print("ERRO: Por favor, digite apenas números válidos.")

# ------------------------------------------------------------------------------
# 4. CÓDIGO DE ORIGEM (MATCH/CASE - Conveniente para múltiplos valores fixos)
# ------------------------------------------------------------------------------
print("--- 4. CÓDIGO DE ORIGEM (MATCH/CASE) ---")
try:
    codigo = int(input("Digite o código de origem (inteiro, ex: 7, 15 ou 90): "))
    
    # ESTRUTURA MATCH/CASE
    match codigo:
        case 1:
            procedencia = "Sul"
        case 2:
            procedencia = "Norte"
        case 3:
            procedencia = "Leste"
        case 4:
            procedencia = "Oeste"
        case 5 | 6:
            procedencia = "Nordeste"
        # Faixa com Condição (Guard: 'if')
        case n if 7 <= n <= 9:
            procedencia = "Sudeste"
        case 10:
            procedencia = "Centro-Oeste"
        case 11:
            procedencia = "Nordeste"
        # Caso Padrão (Default)
        case _:
            procedencia = "Importado"

    print(f"Resultado:\n  Código {codigo} -> Procedência: {procedencia}\n")
    
except ValueError:
    print("ERRO: Digite um número inteiro válido.")

# ------------------------------------------------------------------------------
# 5. MÉDIA DO ALUNO (IF ANINHADO e IF/ELIF/ELSE)
# ------------------------------------------------------------------------------
print("--- 5. MÉDIA DO ALUNO ---")
try:
    n1 = float(input("Nota N1: "))
    n2 = float(input("Nota N2: "))
    optativa = float(input("Nota Optativa (-1 se não fez): "))

    nota_final_1 = n1
    nota_final_2 = n2

    # PONTO DE DECISÃO 1: Substituição (IF ANINHADO)
    if optativa != -1:
        # Se N1 é a menor nota (ou igual), substitui N1
        if nota_final_1 <= nota_final_2:
            nota_final_1 = optativa
        else: # Se N2 é menor
            nota_final_2 = optativa
            
    media = (nota_final_1 + nota_final_2) / 2.0

    # PONTO DE DECISÃO 2: Situação Final (IF/ELIF/ELSE)
    if media >= 6.0:
        situacao = "APROVADO"
    elif media < 3.0:
        situacao = "REPROVADO"
    else:
        situacao = "EM EXAME (Recuperação)"

    print(f"Resultado:\n  Média Final: {media:.1f}")
    print(f"  Situação: {situacao}\n")

except ValueError:
    print("ERRO: Digite apenas números válidos.")

# ------------------------------------------------------------------------------
# 6. POSITIVO OU NEGATIVO (IF/ELSE Simples)
# ------------------------------------------------------------------------------
print("--- 6. POSITIVO OU NEGATIVO ---")
try:
    valor = float(input("Digite um valor numérico: "))
    
    # PONTO DE DECISÃO
    if valor >= 0:
        resultado = "Positivo (inclui zero)"
    else:
        resultado = "Negativo"
        
    print(f"Resultado:\n  O valor {valor} é: {resultado}\n")

except ValueError:
    print("ERRO: Digite apenas números válidos.")