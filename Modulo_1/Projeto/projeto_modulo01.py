"""
SISTEMA DE GERENCIAMENTO - RESTAURANTE JAPONÊS TANOSHIMI
Av. Lúcio Costa - Barra da Tijuca, RJ

"""
import random

# ==== Cardápio do Restaurante ===
cardapio = {
    1: {"nome": "Sushi Salmão", "descricao": "8 peças de sushi de salmão fresco", "preco": 45.00},
    2: {"nome": "Sashimi Misto", "descricao": "15 fatias de peixes variados", "preco": 65.00},
    3: {"nome": "Temaki Atum", "descricao": "Temaki recheado com atum e cream cheese", "preco": 28.00},
    4: {"nome": "Hot Roll", "descricao": "8 peças empanadas com salmão", "preco": 52.00},
    5: {"nome": "Yakisoba", "descricao": "Macarrão oriental com legumes e frango", "preco": 38.00},
    6: {"nome": "Guioza", "descricao": "6 unidades de pastel japonês frito", "preco": 22.00},
    7: {"nome": "Harumaki", "descricao": "4 rolinhos primavera crocantes", "preco": 18.00},
    8: {"nome": "Refrigerante", "descricao": "Lata 350ml", "preco": 6.00},
    9: {"nome": "Suco Natural", "descricao": "Laranja, limão ou maracujá - 500ml", "preco": 12.00},
    10: {"nome": "Sobremesa Mochi", "descricao": "3 unidades de mochi variados", "preco": 15.00}
}
 
# ==== Mesas do Restaurante ===
mesas_disponiveis = list(range(1, 21)) #Número de mesas possíveis em um restaurante de 100² é de 15 à 20 mesas.

# ==== Garçons disponíveis ===
garcons = [
    {"id": 1, "nome": "Pedro Silva"},
    {"id": 2, "nome": "João de Paula"},
    {"id": 3, "nome": "Roberto Carlos"},
    {"id": 4, "nome": "Julio Cesar"},
    {"id": 5, "nome": "Cesar Augusto"}
]                                       #Segundo pesquisa 1 garçon pode atender até 5 mesas, para melhor atender os clientes colocamos 1g para cada 4m.

# ==== Lista de pedidos ===
pedidos_realizados = [] #Lista para armazenar os pedidos feitos pelos clientes.

# === N° dos pedidos ===
contador_de_pedidos = 1000

# === Funções ===
def boas_vindas():
    print("\n" + "=" * 80)
    print("🍣 Bem-vindo ao Restaurante Japonês Tanoshimi 🍣".center(80))
    print("=" * 80)
    print("\nPor favor, escolha uma mesa disponível:")
    print(mesas_disponiveis)

    while True:
        try:
            mesa = int(input("Digite o número da mesa desejada: "))
            if mesa in mesas_disponiveis:
                return mesa  # ✅ retorna apenas quando for válido
            else:
                print("❌ Mesa não disponível. Escolha um número entre 1 e 20.")
        except ValueError:
            print("⚠️ Entrada inválida! Digite apenas números.")

def definir_garcom(mesa):
    if 1 <= mesa <= 4:
        return garcons[0]["nome"]
    elif 5 <= mesa <= 8:
        return garcons[1]["nome"]
    elif 9 <= mesa <= 12:
        return garcons[2]["nome"]
    elif 13 <= mesa <= 16:
        return garcons[3]["nome"]
    else:
        return garcons[4]["nome"]
    
def mostrar_cardapio():
    print("CARDÁPIO TANOSHIMI".center(80))
    print("="*80)
    for codigo, item in cardapio.items():
        print(f"{codigo}. {item['nome']} - {item['descricao']} - R${item['preco']:.2f}")
    print("="*80)

def selecionar_produtos(mesa, garcom, numero_pedido):
    itens_pedido = []
    total = 0

    while True:
        try:
            escolha = int(input("Digite o número do prato (ou 0 para finalizar): "))
            
            if escolha == 0:
                # 🔹 Mostra o resumo completo antes de decidir
                print("\n" + "=" * 80)
                print(f"RESUMO DO PEDIDO #{numero_pedido}".center(80))
                print(f"Mesa: {mesa} | Garçom: {garcom}".center(80))
                print("=" * 80)

                if len(itens_pedido) == 0:
                    print("Nenhum item foi adicionado ainda.")
                else:
                    for item in itens_pedido:
                        subtotal = item["preco"] * item["quantidade"]
                        print(f"- {item['quantidade']}x {item['nome']} - {item['descricao']} - R${subtotal:.2f}")
                    print("=" * 80)
                    print(f"Total parcial: R${total:.2f}")

                # 🔹 Pergunta se o cliente quer continuar ou pagar
                while True:
                    opcao = input("\nDeseja adicionar mais um item (1) ou ir para pagamento (2)? ")

                    if opcao == "1":
                        print("\nPerfeito! Vamos voltar ao cardápio.\n")
                        mostrar_cardapio()
                        break  # volta para o loop principal
                    elif opcao == "2":
                        print("\nIndo para a área de pagamento...\n")
                        formas_pagamento(total, numero_pedido, mesa, garcom, itens_pedido)
                        return itens_pedido, total
                    else:
                        print("⚠️ Opção inválida! Digite 1 para continuar ou 2 para pagar.")

                continue  # volta ao início do loop principal

            # 🔹 Se for um código válido de prato
            if escolha in cardapio:
                produto_escolhido = cardapio[escolha].copy()
                quantidade = int(input(f"Quantas unidades de {produto_escolhido['nome']} você deseja? "))

                produto_escolhido["quantidade"] = quantidade
                subtotal = produto_escolhido["preco"] * quantidade
                total += subtotal
                itens_pedido.append(produto_escolhido)

                print(f"✅ {quantidade}x {produto_escolhido['nome']} adicionado(s)! Total parcial: R${total:.2f}")

            else:
                print("❌ Código inválido. Tente novamente.")
        
        except ValueError:
            print("⚠️ Digite apenas números válidos.")

def formas_pagamento(total, numero_pedido, mesa, garcom, itens_pedido):
    print("\n" + "=" * 80)
    print("ÁREA DE PAGAMENTO".center(80))
    print("=" * 80)
    print("Escolha a forma de pagamento:")
    print("1. Dinheiro")
    print("2. Cartão de Débito")
    print("3. Cartão de Crédito")
    print("4. Pix")

    forma_pagamento = ""
    while True:
        try:
            opcao = int(input("Digite o número da forma de pagamento desejada: "))

            if opcao == 1:
                forma_pagamento = "Dinheiro"
                print("\nVocê escolheu: 💵 Dinheiro")
                while True:
                    try:
                        valor_pago = float(input(f"Total a pagar: R${total:.2f}\nInforme o valor entregue: R$"))
                        if valor_pago < total:
                            print("❌ Valor insuficiente. Por favor, insira um valor maior ou igual ao total.")
                        else:
                            troco = valor_pago - total
                            print(f"✅ Pagamento recebido. Troco: R${troco:.2f}")
                            break
                    except ValueError:
                        print("⚠️ Digite um valor numérico válido.")
                break

            elif opcao == 2:
                forma_pagamento = "Cartão de Débito"
                print("\nVocê escolheu: 💳 Cartão de Débito")
                print("✅ Pagamento aprovado no débito.")
                break

            elif opcao == 3:
                forma_pagamento = "Cartão de Crédito"
                print("\nVocê escolheu: 💳 Cartão de Crédito")
                print("✅ Pagamento aprovado no crédito.")
                break

            elif opcao == 4:
                forma_pagamento = "Pix"
                print("\nVocê escolheu: 📱 Pix")
                print("🔹 Chave Pix: tanoshimi@restaurante.com")
                print("✅ Pagamento confirmado via Pix.")
                break

            else:
                print("⚠️ Opção inválida. Escolha de 1 a 4.")

        except ValueError:
            print("⚠️ Digite apenas números válidos.")

    # 🔹 Gera nota fiscal logo após o pagamento
    nota_fiscal(numero_pedido, mesa, garcom, itens_pedido, total, forma_pagamento)

def nota_fiscal(numero_pedido, mesa, garcom, itens, total, forma_pagamento):
    print("\n" + "=" * 80)
    print("🍣 RESTAURANTE JAPONÊS TANOSHIMI 🍣".center(80))
    print("Av. Lúcio Costa - Barra da Tijuca, Rio de Janeiro/RJ".center(80))
    print("=" * 80)
    print(f"NOTA FISCAL - PEDIDO #{numero_pedido}".center(80))
    print(f"Mesa: {mesa} | Garçom: {garcom}".center(80))
    print("=" * 80)

    if len(itens) == 0:
        print("Nenhum item no pedido.".center(80))
    else:
        for item in itens:
            subtotal = item["preco"] * item["quantidade"]
            print(f"{item['quantidade']}x {item['nome']:<25} R${subtotal:>8.2f}")

    print("-" * 80)
    print(f"FORMA DE PAGAMENTO: {forma_pagamento}".ljust(60))
    print(f"TOTAL: R${total:.2f}".rjust(80))
    print("=" * 80)
    print("Obrigada pela preferência! Volte sempre! 🍱".center(80))
    print("=" * 80)



# === Código Principal ===
mesa_cliente = boas_vindas()
garcom_responsavel = definir_garcom(mesa_cliente)
contador_de_pedidos += 1

print(f"Mesa {mesa_cliente} selecionada com sucesso.")
print("=" * 80)
print(f"O nome do garçom responsável pelo seu atendimento é: {garcom_responsavel}.")
print("=" * 80)
mostrar_cardapio()

# 🔹 Chamada da função com mesa, garçom e número do pedido
itens_pedido, total_pedido = selecionar_produtos(mesa_cliente, garcom_responsavel, contador_de_pedidos)


