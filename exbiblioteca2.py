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
        print("Deseja gerenciar livros de um cartão já cadastrado? (5 - Sim)")
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

        elif resposta == "5":
            try:
                numero_digitado = int(input("Digite o número do cartão: "))
                exibir_cabecalho()

                if not caminho_livro.exists():
                    print("Nenhum livro cadastrado ainda.")
                    input("Pressione Enter para voltar ao menu...")
                    continue

                with caminho_livro.open("r") as arquivo:
                    blocos = arquivo.read().strip().split("\n\n")

                atualizado = False
                for i, bloco in enumerate(blocos):
                    if f"Numero do cartao: {numero_digitado}" in bloco:
                        print("\n=== Dados atuais ===")
                        print(bloco)
                        livros_linha = [linha for linha in bloco.splitlines() if linha.startswith("Livros:")][0]
                        livros_atuais = [livro.strip() for livro in livros_linha.replace("Livros:", "").split(",")]

                        print("\nLivros atuais:", ", ".join(livros_atuais))
                        print("1 - Adicionar livros")
                        print("2 - Remover livros")
                        escolha = input("Escolha a ação: ").strip()
                        exibir_cabecalho()

                        if escolha == "1":
                            novos = input("Digite os livros que deseja adicionar (separados por vírgula): ")
                            novos_livros = [livro.strip() for livro in novos.split(",")]
                            livros_atuais.extend(novos_livros)

                        elif escolha == "2":
                            remover = input("Digite os livros que deseja remover (separados por vírgula): ")
                            livros_a_remover = [livro.strip() for livro in remover.split(",")]
                            livros_atuais = [livro for livro in livros_atuais if livro not in livros_a_remover]

                        else:
                            print("Opção inválida.")
                            input("Pressione Enter para voltar ao menu...")
                            break

                        novo_bloco = ""
                        for linha in bloco.splitlines():
                            if linha.startswith("Livros:"):
                                novo_bloco += "Livros: " + ", ".join(livros_atuais) + "\n"
                            else:
                                novo_bloco += linha + "\n"

                        blocos[i] = novo_bloco.strip()
                        atualizado = True
                        break

                if atualizado:
                    with caminho_livro.open("w") as arquivo:
                        arquivo.write("\n\n".join(blocos) + "\n\n")
                    print("Atualização feita com sucesso!")
                else:
                    print("Número de cartão não encontrado.")

            except ValueError:
                print("Número inválido.")

            input("Pressione Enter para voltar ao menu...")
            exibir_cabecalho()
            continue

        else:
            print("Opção inválida. Por favor, digite 1, 2, 3, 4 ou 5.")
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
