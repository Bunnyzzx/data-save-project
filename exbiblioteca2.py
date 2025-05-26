# Importação de bibliotecas
import os
from pathlib import Path

def exibir_cabecalho():
    os.system("cls" if os.name == "nt" else "clear")
    print("             ")
    print(r"    ____        __           _____         ")       
    print(r"   / __ \____ _/ /_____ _   / ___/____ __   _____") 
    print(r"  / / / / __ `/ __/ __ `/   \__ \/ __ `/ \ / / _ \ ")
    print(r" / /_/ / /_/ / /_/ /_/ /   ___/ / /_/ /\ \/ /  __/")
    print(r"/_____/\__,_/\__/\__,_/   /____/\__,_/  \___/\___/ ")
    print("    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⣶⣶⣶⣶⣶⣶⣶⣦⣀⠀⠀⠀⠀⢀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("    ⠀⠀⠀⠀⠀⠀⠀⢠⢤⣠⣶⣿⣿⡿⠿⠛⠛⠛⠛⠉⠛⠛⠛⠛⠿⣷⡦⠞⣩⣶⣸⡆⠀⠀⠀⠀⠀⠀⠀")
    print("    ⠀⠀⠀⠀⠀⠀⣠⣾⡤⣌⠙⠻⣅⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠔⠋⢀⣾⣿⣿⠃⣇⠀⠀⠀⠀⠀⠀⠀")
    print("    ⠀⠀⠀⠀⣠⣾⣿⡟⢇⢻⣧⠄⠀⠈⢓⡢⠴⠒⠒⠒⠒⡲⠚⠁⠀⠐⣪⣿⣿⡿⡄⣿⣷⡄⠀⠀⠀⠀⠀")
    print("    ⠀⠀⠀⣠⣿⣿⠟⠁⠸⡼⣿⡂⠀⠀⠈⠁⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠉⠹⣿⣧⢳⡏⠹⣷⡄⠀⠀⠀⠀")
    print("    ⠀⠀⣰⣿⡿⠃⠀⠀⠀⢧⠑⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⠇⡸⠀⠀⠘⢿⣦⣄⠀⠀")
    print("    ⠀⢰⣿⣿⠃⠀⠀⠀⠀⡼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡠⠀⠀⠀⠀⠀⠀⠰⡇⠀⠀⠀⠈⣿⣿⣆⠀")
    print("    ⠀⣿⣿⡇⠀⠀⠀⠀⢰⠇⠀⢺⡇⣄⠀⠀⠀⠀⣤⣶⣀⣿⠃⠀⠀⠀⠀⠀⠀⠀⣇⠀⠀⠀⠀⠸⣿⣿⡀")
    print("    ⢸⣿⣿⠀⠀⠀⠀⠀⢽⠀⢀⡈⠉⢁⣀⣀⠀⠀⠀⠉⣉⠁⠀⠀⠀⣀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⣿⣿⡇")
    print("    ⢸⣿⡟⠀⠀⠀⠠⠀⠈⢧⡀⠀⠀⠀⠹⠁⠀⠀⠀⠀⠀⠀⠠⢀⠀⠀⠀⠀⠀⢼⠁⠀⠀⠀⠀⠀⢹⣿⡇")
    print("    ⢸⣿⣿⠀⠀⠀⠀⠀⠠⠀⠙⢦⣀⠠⠊⠉⠂⠄⠀⠀⠀⠈⠀⠀⠀⣀⣤⣤⡾⠘⡆⠀⠀⠀⠀⣾⣿⡇")
    print("    ⠘⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⢠⠜⠳⣤⡀⠀⠀⣀⣤⡤⣶⣾⣿⣿⣿⠟⠁⠀⠀⡸⢦⣄⠀⠀⣿⣿⠇")
    print("    ⠀⢿⣿⣧⠀⠀⠀⠀⠀⣠⣤⠞⠀⠀⠀⠙⠁⠙⠉⠀⠀⠸⣛⡿⠉⠀⠀⠀⢀⡜⠀⠀⠈⠙⠢⣼⣿⡿⠀")
    print("    ⠀⠈⣿⣿⣆⠀⠀⢰⠋⠡⡇⠀⡀⣀⣤⢢⣤⣤⣀⠀⠀⣾⠟⠀⠀⠀⠀⢀⠎⠀⠀⠀⠀  ⣰⣿⣿⠁⠀")
    print("    ⠀⠀⠈⢿⣿⣧⣀⡇⠀⡖⠁⢠⣿⣿⢣⠛⣿⣿⣿⣷⠞⠁⠀⠀⠈⠫⡉⠁⠀⠀⠀⠀⢀⣼⣿⠿⠃⠀⠀")
    print("    ⠀⠀⠀⠈⠻⣿⣿⣇⡀⡇⠀⢸⣿⡟⣾⣿⣿⣿⣿⠋⠀⠀⠀⢀⡠⠊⠁⠀⠀⠀⢀⣠⣿⠏⠀⠀⠀⠀⠀")
    print("    ⠀⠀⠀⠀⠀⠈⠻⣿⣿⣦⣀⢸⣿⢻⠛⣿⣿⡿⠁⠀⠀⣀⠔⠉⠀⠀⠀⠀⣀⣴⡿⠟⠁⠀⠀⠀⠀⠀⠀")
    print("    ⠀⠀⠀⠀⠀⠀⠀⠈⠙⠿⣿⣿⣿⣼⣿⣿⣟⠀⠀⡠⠊⠀⣀⣀⣠⣴⣶⠿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠿⣿⣿⣿⣿⣶⣶⣷⣶⣶⡿⠿⠛⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠛⠛⠛⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("dev: @caioxhtps")  
    print("             ")

# Caminhos dos arquivos
caminho_do_arquivo1 = Path("cadastro.txt")
caminho_livro = Path("livro_cliente.txt")

while True:
    exibir_cabecalho()

    while True:
        print("Deseja realizar um novo cadastro? (1 - Sim / 2 - Não)")
        print("Deseja ver os dados dos usuários cadastrados? (3 - Sim / 4 - Não)")
        resposta = input().strip()
        exibir_cabecalho()

        if resposta == "1":
            if not caminho_do_arquivo1.exists():
                with caminho_do_arquivo1.open("w") as arquivo1:
                    arquivo1.write("Cadastro de clientes\n\n")
            break

        elif resposta == "2":
            print("Encerrando o programa...")
            exit()

        elif resposta == "3":
            print("\n=== Usuários Cadastrados ===\n")
            if caminho_do_arquivo1.exists():
                with caminho_do_arquivo1.open() as arquivo1:
                    conteudo = arquivo1.read().strip()
                    print(conteudo if conteudo else "Nenhum dado encontrado.")
            else:
                print("Arquivo de cadastro não encontrado.")
            input("\nPressione Enter para voltar ao menu...")
            exibir_cabecalho()

        elif resposta == "4":
            exibir_cabecalho()
            continue

        else:
            print("Opção inválida. Por favor, digite 1, 2, 3 ou 4.")
            exibir_cabecalho()

    try:
        with caminho_do_arquivo1.open() as arquivo1:
            conteudo = arquivo1.read()
            numero_cartao = conteudo.count("Numero do cartao:") + 1
    except FileNotFoundError:
        numero_cartao = 1

    nome = input("Digite seu nome: ")
    exibir_cabecalho()

    cpf = input("Digite seu CPF: ")
    exibir_cabecalho()

    telefone = input("Digite seu telefone: ")
    exibir_cabecalho()

    with caminho_do_arquivo1.open("a") as arquivo1:
        arquivo1.write(f"Nome: {nome}\n")
        arquivo1.write(f"CPF: {cpf}\n")
        arquivo1.write(f"Telefone: {telefone}\n")
        arquivo1.write(f"Numero do cartao: {numero_cartao}\n\n")

    print(f"\nCadastro realizado com sucesso!")
    print("")
    print(f"Nome: {nome}")
    print(f"\nSeu número de cartão é: {numero_cartao}")


    input("Pressione Enter para continuar...")
    exibir_cabecalho()

    nome_titular = ""
    while True:
        try:
            numero_digitado = int(input("Digite o número do cartão: "))
            exibir_cabecalho()

            if numero_digitado < 1:
                raise ValueError("O número do cartão deve ser maior que zero.")

            with caminho_do_arquivo1.open() as arquivo1:
                linhas = arquivo1.readlines()

            for i in range(len(linhas)):
                if linhas[i].strip() == f"Numero do cartao: {numero_digitado}":
                    nome_titular = linhas[i - 3].replace("Nome: ", "").strip()
                    print(f"\nCartão válido. Titular: {nome_titular}")
                    break
            else:
                print("Cartão inválido. Tente novamente.")
                continue

            break

        except ValueError as e:
            print("Erro:", e)
            exibir_cabecalho()

    livros = input("\nDigite o nome dos livros separados por vírgula: ")
    exibir_cabecalho()

    with caminho_livro.open("a") as arquivo:
        arquivo.write(f"Numero do cartao: {numero_digitado}\n")
        arquivo.write(f"Nome do titular: {nome_titular}\n")
        arquivo.write(f"Livros: {livros}\n\n")

    print("Livros cadastrados com sucesso!")
    input("Pressione Enter para continuar...")
    exibir_cabecalho()

    while True:
        repetir = input("Deseja cadastrar outro usuário? (1 - Sim / 2 - Não): ").strip()
        exibir_cabecalho()

        if repetir == "1":
            break
        elif repetir == "2":
            print()
            print("Encerrando o programa...")
            exit()
        else:
            print("Opção inválida. Digite 1 para sim ou 2 para não.")
            exibir_cabecalho()
