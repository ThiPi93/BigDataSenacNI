# ================================================
# 1. Cálculo de Média Escolar para Vários Alunos
# ================================================
print("=== Cálculo de Média Escolar ===")
for i in range(1, 11):  # 10 alunos
    print(f"\nAluno {i}:")
    try:
        nota1 = float(input("Digite a primeira nota: "))
        nota2 = float(input("Digite a segunda nota: "))
        media = (nota1 + nota2) / 2

        # Verificação de status
        if media >= 6:
            status = "Aprovado"
        elif media >= 3:
            status = "Recuperação"
        else:
            status = "Reprovado"

        print(f"Média: {media:.2f} - Status: {status}")
    except ValueError:
        print("Entrada inválida! Digite apenas números para as notas.")

# ===========================
# 2. Cadastro de Candidatos
# ===========================
print("\n=== Cadastro de Candidatos ===")
ano_atual = 2025  # Pode usar datetime.now().year se preferir (aí precisa fazer import datetime)


# from datetime import datetime
# ano_atual = datetime.now().year


for i in range(1, 13):  # 12 candidatos
    print(f"\nCandidato {i}:")
    try:
        ano_nasc = int(input("Digite o ano de nascimento: "))
        idade = ano_atual - ano_nasc

        if idade < 18:
            print("Não pode participar (menor de 18 anos).")
            continue  # pula para o próximo candidato
        else:
            telefone = input("Digite o telefone: ")
            email = input("Digite o e-mail: ")
            print(f"Cadastro concluído para candidato {i}.")
    except ValueError:
        print("Ano inválido! Digite apenas números para o ano de nascimento.")

# ===============================
# 3. Tentativa de Login e Senha
# ===============================
print("\n=== Sistema de Login ===")
usuario_correto = "admin"
senha_correta = "123456"
tentativas = 3

while tentativas > 0:
    try:
        usuario = input("Usuário: ")
        senha = input("Senha: ")

        if usuario == usuario_correto and senha == senha_correta:
            print("Login realizado com sucesso!")
            break
        else:
            tentativas -= 1
            print(f"Usuário ou senha incorretos. Tentativas restantes: {tentativas}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

if tentativas == 0:
    print("Bloqueado! Número máximo de tentativas atingido.")