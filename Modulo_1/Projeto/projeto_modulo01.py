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
    print("🍣 Bem-vindo ao Restaurante Japonês Tanoshimi 🍣")
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
    print("CARDÁPIO TANOSHIMI")
    print("="*80)
    for codigo, item in cardapio.items():
        print(f"{codigo}. {item['nome']} - {item['descricao']} - R${item['preco']:.2f}")
    print("="*80)

def selecionar_produtos():
    itens_pedido = []
    total = 0

    while True:
        try:
            escolha = int(input("Digite o número do prato (ou 0 para finalizar): "))
            
            if escolha == 0:
                # 🔹 Novo trecho: confirmação antes de ir pro pagamento
                while True:
                    opcao = input("\nDeseja adicionar mais um item (1) ou ir para pagamento (2)? ")

                    if opcao == "1":
                        print("\nPerfeito! Vamos voltar ao cardápio.\n")
                        mostrar_cardapio()
                        break  # sai do while interno e volta pro loop principal
                    elif opcao == "2":
                        print("\nIndo para a área de pagamento...\n")
                        return itens_pedido, total  # encerra o pedido
                    else:
                        print("⚠️ Opção inválida! Digite 1 para continuar ou 2 para pagar.")

                continue  # volta pro loop principal (reexibe cardápio se escolheu continuar)

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



# === Código Principal ===
mesa_cliente = boas_vindas()
garcom_responsavel = definir_garcom(mesa_cliente)
print(f"Mesa {mesa_cliente} selecionada com sucesso.")
print("=" * 80)
print(f"O nome do garçom responsável pelo seu atendimento é: {garcom_responsavel}.")
print("=" * 80)
mostrar_cardapio()
itens_pedido, total_pedido = selecionar_produtos()

print("\n" + "=" * 80)
print("RESUMO DO PEDIDO")
print("=" * 80)
for item in itens_pedido:
    subtotal = item["preco"] * item["quantidade"]
    print(f"- {item['quantidade']}x {item['nome']} - {item['descricao']} - R${subtotal:.2f}")
print(f"Total a pagar: R${total_pedido:.2f}")

