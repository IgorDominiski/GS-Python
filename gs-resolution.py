# Igor Dominiski RM562055, Murilo Reis RM564053, Murillo Akira RM561806
# Função que exibe o menu principal do sistema e retorna a opção escolhida pelo usuário
def exibir_menu():
    print("\n=== Sistema de Monitoramento de Enchentes ===")
    print("1. Cadastrar Novo Evento")
    print("2. Listar Eventos")
    print("3. Buscar por Região")
    print("4. Sair")
    print("5. Verificar Risco de Enchente por Região")
    opcao = input("Escolha uma opção (1-5): ")
    return opcao


# Função para ler e validar números inteiros do usuário
def ler_numero(mensagem):
    while True:
        valor = input(mensagem)
        if valor.isnumeric():
            return int(valor)
        else:
            print("Digite um número válido.")


# Função para ler e validar números decimais (float) do usuário
def ler_float(mensagem):
    while True:
        valor = input(mensagem)
        partes = valor.split(".")
        if len(partes) == 2 and partes[0].isnumeric() and partes[1].isnumeric():
            return float(valor)
        elif valor.isnumeric():
            return float(valor)
        else:
            print("Digite um número com ponto ou inteiro válido.")


# Função que força o usuário a escolher uma opção válida de uma lista de opções
def forca_opcao(msg, msg_erro, lista_opcoes):
    opcoes = '\n'.join(lista_opcoes)
    opcao = input(f"{msg}\n{opcoes}\n->")
    while opcao not in opcoes:
        print(msg_erro)
        opcao = input(f"{msg}\n{opcoes}\n->")
    return opcao


# Função para cadastrar um novo evento de enchente com seus detalhes
def cadastrar_evento(lista_eventos):
    print("\n--- Cadastrar Evento ---")

    while True:
        regiao = input("Região: ")
        if regiao != "":
            break
        else:
            print("Região não pode ser vazia.")

    intensidade = forca_opcao("Intensidade:", "Intensidade inválida.", ["Baixa", "Moderada", "Alta"])
    vitimas = ler_numero("Número de vítimas: ")
    danos = ler_float("Danos estimados (em milhões): ")

    evento = [regiao, intensidade, vitimas, danos]
    lista_eventos.append(evento)
    print("Evento cadastrado com sucesso!")


# Função para listar todos os eventos de enchente cadastrados
def listar_eventos(lista_eventos):
    if len(lista_eventos) == 0:
        print("Nenhum evento cadastrado.")
    else:
        for i in range(len(lista_eventos)):
            print("\nEvento", i + 1)
            print("Região:", lista_eventos[i][0])
            print("Intensidade:", lista_eventos[i][1])
            print("Vítimas:", lista_eventos[i][2])
            print("Danos estimados: R$", lista_eventos[i][3], "milhões")


# Função para buscar eventos de enchente por região específica
def buscar_eventos(lista_eventos):
    regiao = input("Informe a região para busca: ")
    encontrou = False
    for i in range(len(lista_eventos)):
        if lista_eventos[i][0].lower() == regiao.lower():
            encontrou = True
            print("\nEvento", i + 1)
            print("Intensidade:", lista_eventos[i][1])
            print("Vítimas:", lista_eventos[i][2])
            print("Danos: R$", lista_eventos[i][3], "milhões")
    if not encontrou:
        print("Nenhum evento encontrado nessa região.")


# Função que mostra o risco de enchente para cada região do Brasil
def mostrar_risco_por_regiao():
    print("\n=== Verificador de Risco de Enchente ===")
    print("Digite o nome da região (ex: Sul, Sudeste, Norte, Nordeste, Centro-Oeste)")

    while True:
        regiao = input("Região: ").strip().lower()

        if regiao == "sul":
            print("Risco de enchente: 80%")
            break
        elif regiao == "sudeste":
            print("Risco de enchente: 60%")
            break
        elif regiao == "norte":
            print("Risco de enchente: 30%")
            break
        elif regiao == "nordeste":
            print("Risco de enchente: 40%")
            break
        elif regiao == "centro-oeste":
            print("Risco de enchente: 20%")
            break
        else:
            print("Região inválida. Tente novamente.")


# Lista que armazena todos os eventos de enchente cadastrados
eventos = []

# Loop principal do programa que executa as funções baseado na escolha do usuário
while True:
    escolha = exibir_menu()

    if escolha == "1":
        cadastrar_evento(eventos)
    elif escolha == "2":
        listar_eventos(eventos)
    elif escolha == "3":
        buscar_eventos(eventos)
    elif escolha == "4":
        print("Saindo do programa.")
        break
    elif escolha == "5":
        mostrar_risco_por_regiao()
    else:
        print("Escolha inválida.")
