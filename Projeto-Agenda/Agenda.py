import csv

agenda = {}

#FUNÇÕES PRINCIPAIS
def mostrar_contatos():
    if not agenda:
        print("\nNenhum contato foi encontrado.")
    for contato, dados in agenda.items():
        print("-----------------------------------------")
        print(f"Nome: {contato}")
        print(f"Telefone: {dados['tel']}")
        print(f"Email: {dados['email']}")
        print(f"Endereço: {dados['endereco']}")

def buscar_contato(contato):
    if contato in agenda:
        print("\nContato encontrado:")
        print(f"Nome: {contato}")
        print(f"Telefone: {agenda[contato]['tel']}")
        print(f"Email: {agenda[contato]['email']}")
        print(f"Endereço: {agenda[contato]['endereco']}")
    else:
        print("\nContato inexistente")

def adicionar_contato(contato, telefone, email, endereco):
    agenda[contato] = {
        "tel": telefone,
        "email": email,
        "endereco": endereco
    }
    print(f"\nContato {contato} adicionado com sucesso!")
    exportar_contatos()

def editar_contato(contato, telefone, email, endereco):
    if contato in agenda:
        agenda[contato] = {
            "tel": telefone,
            "email": email,
            "endereco": endereco
        }
        print(f"\nContato {contato} editado com sucesso!")
        exportar_contatos()
    else:
        print("\nContato inexistente")

def excluir_contato(contato):
    if contato in agenda:
        agenda.pop(contato)
        print(f"\nContato {contato} excluído com sucesso!")
        exportar_contatos()
    else:
        print("\nContato inexistente")

#FUNÇÕES DOS ARQUIVOS
def exportar_contatos():
    try:
        with open('database.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Nome", "Telefone", "Email", "Endereco"])
            for contato, dados in agenda.items():
                writer.writerow([contato, dados['tel'], dados['email'], dados['endereco']])
    except Exception as e:
        print(f"Erro ao exportar contatos: {e}")

def importar_contatos(filename):
    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for linha in reader:
                nome = linha["Nome"].strip()
                telefone = linha["Telefone"].strip()
                email = linha["Email"].strip()
                endereco = linha["Endereco"].strip()
                agenda[nome] = {
                    "tel": telefone,
                    "email": email,
                    "endereco": endereco
                }
    except FileNotFoundError:
        print("Arquivo de contatos não encontrado, criando um novo database.csv")
    except Exception as e:
        print(f"Erro ao importar contatos: {e}")

#VALIDAÇÃO DE EMAIL E TELEFONE
def validar_email(email):
    return "@" in email and "." in email

def validar_telefone(telefone):
    return telefone.isdigit()

#MENU PRINCIPAL
def mostrar_menu():
    while True:
        print("\n-----------------------------------------")
        print("1 - Mostrar todos os contatos")
        print("2 - Adicionar contato")
        print("3 - Excluir contato")
        print("4 - Editar contato")
        print("5 - Buscar contato")
        print("9 - Fechar menu")
        print("-----------------------------------------")
        opcao = input("Digite sua opção: ")

        if opcao == "1":
            mostrar_contatos()
        elif opcao == "2":
            contato = input("Digite o nome do contato: ").strip()
            telefone = input("Digite o telefone do contato: ").strip()
            email = input("Digite o email do contato: ").strip()
            endereco = input("Digite o endereço do contato: ").strip()
            if not validar_telefone(telefone):
                print("Telefone deve conter apenas números")
                continue

            if not validar_email(email):
                print("Email deve conter @ e .")
                continue

            adicionar_contato(contato, telefone, email, endereco)

        elif opcao == "3":
            contato = input("Digite o nome do contato: ").strip()
            excluir_contato(contato)

        elif opcao == "4":
            contato = input("Digite o nome do contato: ").strip()
            telefone = input("Digite o telefone do contato: ").strip()
            email = input("Digite o email do contato: ").strip()
            endereco = input("Digite o endereço do contato: ").strip()
            if not validar_telefone(telefone):
                print("Telefone deve conter apenas números")
                continue

            if not validar_email(email):
                print("Email deve conter @ e .")
                continue

            editar_contato(contato, telefone, email, endereco)

        elif opcao == "5":
            contato = input("Digite o nome do contato: ").strip()
            buscar_contato(contato)

        elif opcao == "9":
            print("Fechando menu...")
            break

        else:
            print("Digite um número válido")

#INÍCIO DO PROGRAMA
importar_contatos("database.csv")
mostrar_menu()
