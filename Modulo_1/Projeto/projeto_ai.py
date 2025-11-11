"""
SISTEMA DE GERENCIAMENTO - RESTAURANTE JAPONÊS TANOSHIMI
Av. Lúcio Costa - Barra da Tijuca, RJ
Desenvolvido aplicando conceitos de: Funções, Estruturas de Dados, 
Decisões e Repetições
"""

import random

# ============================================================
# DADOS INICIAIS DO SISTEMA
# ============================================================

# Cardápio do restaurante (Dicionário de dicionários)
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

# Lista de garçons cadastrados
garcons = [
    {"id": 1, "nome": "Carlos Silva"},
    {"id": 2, "nome": "Ana Paula"},
    {"id": 3, "nome": "Roberto Santos"},
    {"id": 4, "nome": "Juliana Costa"}
]

# Lista de mesas disponíveis (10 mesas no restaurante)
mesas_disponiveis = list(range(1, 11))  # Mesas de 1 a 10

# Lista para armazenar todos os pedidos realizados
pedidos_realizados = []

# Contador global para número de pedidos
contador_pedidos = 1000


# ============================================================
# FUNÇÕES DO SISTEMA
# ============================================================

def exibir_cabecalho(titulo):
    """Exibe um cabeçalho formatado para melhor visualização"""
    print("\n" + "=" * 60)
    print(f"  {titulo.upper()}")
    print("=" * 60)


def exibir_cardapio():
    """Exibe o cardápio completo do restaurante"""
    exibir_cabecalho("Cardápio Tanoshimi")
    print(f"{'ID':<5} {'Prato':<20} {'Descrição':<30} {'Preço':>10}")
    print("-" * 70)
    
    for id_prato, dados in cardapio.items():
        print(f"{id_prato:<5} {dados['nome']:<20} {dados['descricao']:<30} R$ {dados['preco']:>7.2f}")
    print()


def listar_garcons():
    """Exibe a lista de garçons disponíveis"""
    exibir_cabecalho("Garçons Disponíveis")
    for garcom in garcons:
        print(f"ID: {garcom['id']} - Nome: {garcom['nome']}")
    print()


def listar_mesas_disponiveis():
    """Exibe as mesas que estão livres"""
    if len(mesas_disponiveis) > 0:
        print(f"\nMesas disponíveis: {mesas_disponiveis}")
    else:
        print("\n⚠️  Todas as mesas estão ocupadas no momento!")


def obter_garcom_valido():
    """Solicita e valida o ID do garçom responsável"""
    while True:
        try:
            listar_garcons()
            id_garcom = int(input("Digite o ID do garçom responsável: "))
            
            # Verifica se o ID existe na lista de garçons
            for garcom in garcons:
                if garcom['id'] == id_garcom:
                    return garcom['nome']
            
            print("❌ ID de garçom inválido! Tente novamente.")
        except ValueError:
            print("❌ Por favor, digite um número válido!")


def obter_mesa_valida():
    """Solicita e valida o número da mesa"""
    while True:
        try:
            listar_mesas_disponiveis()
            
            if len(mesas_disponiveis) == 0:
                print("Nenhuma mesa disponível. Retornando ao menu...")
                return None
            
            num_mesa = int(input("\nDigite o número da mesa (ou 0 para cancelar): "))
            
            if num_mesa == 0:
                return None
            
            if num_mesa in mesas_disponiveis:
                mesas_disponiveis.remove(num_mesa)  # Remove a mesa da lista de disponíveis
                return num_mesa
            else:
                print("❌ Mesa inválida ou já ocupada! Tente novamente.")
        except ValueError:
            print("❌ Por favor, digite um número válido!")


def criar_pedido():
    """Função principal para criar um novo pedido"""
    global contador_pedidos
    
    exibir_cabecalho("Novo Pedido")
    
    # Passo 1: Obter garçom responsável
    nome_garcom = obter_garcom_valido()
    
    # Passo 2: Obter mesa
    num_mesa = obter_mesa_valida()
    if num_mesa is None:
        return  # Cancelar operação
    
    # Passo 3: Montar o pedido (itens do cardápio)
    exibir_cardapio()
    
    itens_pedido = []
    valor_total = 0.0
    
    print("\n📋 Monte o pedido (digite 0 para finalizar):")
    
    while True:
        try:
            id_item = int(input("\nDigite o ID do prato desejado: "))
            
            if id_item == 0:
                break
            
            if id_item in cardapio:
                quantidade = int(input(f"Quantidade de '{cardapio[id_item]['nome']}': "))
                
                if quantidade <= 0:
                    print("❌ Quantidade deve ser maior que zero!")
                    continue
                
                # Adiciona o item ao pedido
                item = {
                    "id": id_item,
                    "nome": cardapio[id_item]['nome'],
                    "quantidade": quantidade,
                    "preco_unitario": cardapio[id_item]['preco'],
                    "subtotal": cardapio[id_item]['preco'] * quantidade
                }
                
                itens_pedido.append(item)
                valor_total += item['subtotal']
                
                print(f"✅ Adicionado: {quantidade}x {item['nome']} - R$ {item['subtotal']:.2f}")
            else:
                print("❌ ID de prato inválido!")
                
        except ValueError:
            print("❌ Por favor, digite um número válido!")
    
    # Verifica se há itens no pedido
    if len(itens_pedido) == 0:
        print("\n⚠️  Nenhum item adicionado. Pedido cancelado.")
        mesas_disponiveis.append(num_mesa)  # Libera a mesa novamente
        mesas_disponiveis.sort()
        return
    
    # Passo 4: Gerar número do pedido e criar o registro
    numero_pedido = contador_pedidos
    contador_pedidos += 1
    
    pedido_completo = {
        "numero": numero_pedido,
        "mesa": num_mesa,
        "garcom": nome_garcom,
        "itens": itens_pedido,
        "valor_total": valor_total,
        "status": "Aberto"
    }
    
    pedidos_realizados.append(pedido_completo)
    
    # Exibe o resumo do pedido
    exibir_resumo_pedido(pedido_completo)


def exibir_resumo_pedido(pedido):
    """Exibe o resumo detalhado de um pedido"""
    print("\n" + "=" * 60)
    print("          🎫 COMPROVANTE DO PEDIDO")
    print("=" * 60)
    print(f"Número do Pedido: {pedido['numero']}")
    print(f"Mesa: {pedido['mesa']}")
    print(f"Garçom: {pedido['garcom']}")
    print(f"Status: {pedido['status']}")
    print("-" * 60)
    print(f"{'Item':<25} {'Qtd':>5} {'Preço Unit.':>12} {'Subtotal':>12}")
    print("-" * 60)
    
    for item in pedido['itens']:
        print(f"{item['nome']:<25} {item['quantidade']:>5} R$ {item['preco_unitario']:>9.2f} R$ {item['subtotal']:>9.2f}")
    
    print("-" * 60)
    print(f"{'VALOR TOTAL:':<43} R$ {pedido['valor_total']:>9.2f}")
    print("=" * 60)
    print("\n✅ Pedido registrado com sucesso!")
    print(f"🎫 Apresente o número {pedido['numero']} no caixa para pagamento.")
    print()


def realizar_pagamento():
    """Processa o pagamento de um pedido"""
    exibir_cabecalho("Realizar Pagamento")
    
    if len(pedidos_realizados) == 0:
        print("\n⚠️  Não há pedidos registrados no sistema.")
        return
    
    try:
        numero = int(input("\nDigite o número do pedido para pagamento: "))
        
        # Busca o pedido pelo número
        pedido_encontrado = None
        for pedido in pedidos_realizados:
            if pedido['numero'] == numero:
                pedido_encontrado = pedido
                break
        
        if pedido_encontrado is None:
            print(f"❌ Pedido número {numero} não encontrado!")
            return
        
        # Verifica se já foi pago
        if pedido_encontrado['status'] == "Pago":
            print(f"\n⚠️  Este pedido já foi pago anteriormente!")
            return
        
        # Exibe o resumo
        exibir_resumo_pedido(pedido_encontrado)
        
        # Escolha da forma de pagamento
        print("\nFormas de pagamento:")
        print("1 - Dinheiro")
        print("2 - Cartão de Débito")
        print("3 - Cartão de Crédito")
        print("4 - PIX")
        
        forma_pagamento = input("\nEscolha a forma de pagamento (1-4): ")
        
        # Usando match/case (Python 3.10+)
        match forma_pagamento:
            case "1":
                metodo = "Dinheiro"
            case "2":
                metodo = "Cartão de Débito"
            case "3":
                metodo = "Cartão de Crédito"
            case "4":
                metodo = "PIX"
            case _:
                print("❌ Forma de pagamento inválida!")
                return
        
        # Atualiza o status do pedido
        pedido_encontrado['status'] = "Pago"
        pedido_encontrado['forma_pagamento'] = metodo
        
        # Libera a mesa
        mesas_disponiveis.append(pedido_encontrado['mesa'])
        mesas_disponiveis.sort()
        
        print("\n" + "=" * 60)
        print("          ✅ PAGAMENTO REALIZADO COM SUCESSO!")
        print("=" * 60)
        print(f"Valor pago: R$ {pedido_encontrado['valor_total']:.2f}")
        print(f"Método: {metodo}")
        print(f"Mesa {pedido_encontrado['mesa']} liberada.")
        print("\n🙏 Obrigado pela preferência! Volte sempre ao Tanoshimi!")
        print("=" * 60)
        
    except ValueError:
        print("❌ Por favor, digite um número válido!")


def consultar_pedidos():
    """Lista todos os pedidos realizados no sistema"""
    exibir_cabecalho("Consultar Pedidos")
    
    if len(pedidos_realizados) == 0:
        print("\n⚠️  Não há pedidos registrados no sistema.")
        return
    
    print(f"\n{'Nº Pedido':<12} {'Mesa':<8} {'Garçom':<20} {'Valor Total':<15} {'Status':<10}")
    print("-" * 75)
    
    for pedido in pedidos_realizados:
        print(f"{pedido['numero']:<12} {pedido['mesa']:<8} {pedido['garcom']:<20} R$ {pedido['valor_total']:<12.2f} {pedido['status']:<10}")
    
    print()


def relatorio_financeiro():
    """Gera relatório financeiro com totais"""
    exibir_cabecalho("Relatório Financeiro")
    
    if len(pedidos_realizados) == 0:
        print("\n⚠️  Não há pedidos registrados no sistema.")
        return
    
    total_aberto = 0.0
    total_pago = 0.0
    count_aberto = 0
    count_pago = 0
    
    for pedido in pedidos_realizados:
        if pedido['status'] == "Aberto":
            total_aberto += pedido['valor_total']
            count_aberto += 1
        elif pedido['status'] == "Pago":
            total_pago += pedido['valor_total']
            count_pago += 1
    
    total_geral = total_aberto + total_pago
    
    print(f"\n📊 Total de pedidos: {len(pedidos_realizados)}")
    print(f"   • Pedidos abertos: {count_aberto} | Valor: R$ {total_aberto:.2f}")
    print(f"   • Pedidos pagos: {count_pago} | Valor: R$ {total_pago:.2f}")
    print("-" * 60)
    print(f"💰 FATURAMENTO TOTAL: R$ {total_geral:.2f}")
    print()


def adicionar_item_cardapio():
    """Permite adicionar novos pratos ao cardápio"""
    exibir_cabecalho("Adicionar Item ao Cardápio")
    
    # Encontra o próximo ID disponível
    proximo_id = max(cardapio.keys()) + 1 if len(cardapio) > 0 else 1
    
    nome = input("Nome do prato: ")
    descricao = input("Descrição: ")
    
    while True:
        try:
            preco = float(input("Preço (R$): "))
            if preco <= 0:
                print("❌ O preço deve ser maior que zero!")
                continue
            break
        except ValueError:
            print("❌ Digite um valor numérico válido!")
    
    cardapio[proximo_id] = {
        "nome": nome,
        "descricao": descricao,
        "preco": preco
    }
    
    print(f"\n✅ Prato '{nome}' adicionado ao cardápio com ID {proximo_id}!")


def menu_principal():
    """Menu principal do sistema"""
    while True:
        exibir_cabecalho("Sistema Restaurante Tanoshimi")
        print("🍱 1 - Criar Novo Pedido")
        print("💳 2 - Realizar Pagamento")
        print("📋 3 - Consultar Pedidos")
        print("📊 4 - Relatório Financeiro")
        print("🍽️  5 - Exibir Cardápio")
        print("➕ 6 - Adicionar Item ao Cardápio")
        print("🚪 0 - Sair do Sistema")
        print("=" * 60)
        
        opcao = input("\nEscolha uma opção: ")
        
        match opcao:
            case "1":
                criar_pedido()
            case "2":
                realizar_pagamento()
            case "3":
                consultar_pedidos()
            case "4":
                relatorio_financeiro()
            case "5":
                exibir_cardapio()
            case "6":
                adicionar_item_cardapio()
            case "0":
                print("\n👋 Encerrando o sistema... Até logo!")
                break
            case _:
                print("\n❌ Opção inválida! Tente novamente.")
        
        input("\nPressione ENTER para continuar...")


# ============================================================
# EXECUÇÃO DO PROGRAMA
# ============================================================

if __name__ == "__main__":
    print("\n" + "🍣" * 30)
    print("   BEM-VINDO AO SISTEMA DO RESTAURANTE TANOSHIMI")
    print("   Av. Lúcio Costa - Barra da Tijuca, RJ")
    print("🍣" * 30)
    

    menu_principal()