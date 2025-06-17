import os

def opc_menu(usuario_logado, permitidos):
    print("\033[0m[1] Cadastrar novo usuário")
    if(usuario_logado == None):
        print("[2] Entrar no Chupeta Car")
    print("[3] Aba de Chupetas")
    print("[4] Aba de passageiros")
    if(usuario_logado == True):
        permitidos.append('5')
        print("[5] Logout")
    print("[6] Segredo (NÃO ENTRE)")
    print("[0] Sair\n")

def cadastrar_user(usuarios):
    nome = ""
    while nome.strip() == "":
        nome = input("\nDigite seu nome de usuário: ")
        if nome.strip() == "":
            print("\n\033[1;31mO nome não pode estar em branco!\033[0m")

    email_valido = False
    while not email_valido:
        email = input("\nDigite seu endereço de email: ")
        if ' ' in email or email.count('@') != 1 or not email.endswith(".com"):
            print("\n\033[1;31mEmail inválido!\033[0m\n")
            while True:
                print("[1] Tentar novamente")
                print("[0] Voltar para o menu principal\n")
                opcao = input("Selecione uma opção: ")
                if opcao == '1':
                    break
                elif opcao == '0':
                    os.system("cls" if os.name == "nt" else "clear")
                    email = None
                    break
                else:
                    print("\n\033[1;31mOpção inválida!\033[0m\n")
            if email is None:
                return False
            else:
                continue

        email_ja_existe = any(usuario['email'] == email for usuario in usuarios)

        if email_ja_existe:
            print("\033[1;32m\n\033[1;33mEste email já está cadastrado!\033[0m\n\033[0m")
            while True:
                print("[1] Tentar outro email")
                print("[0] Voltar para o menu principal\n")
                opcao = input("Selecione uma opção: ")
                if opcao == '1':
                    break
                elif opcao == '0':
                    os.system("cls" if os.name == "nt" else "clear")
                    email = None
                    break
                else:
                    print("\n\033[1;31mOpção inválida!\033[0m\n")
            if email is None:
                return False
            else:
                continue
        else:
            break

    senha = ""
    while not senha:
        senha = input("Digite sua senha: ")
        if not senha:
            print("\n\033[1;31mA senha não pode ser vazia!\033[0m\n")

    usuarios.append({
        "nome": nome,
        "email": email,
        "senha": senha
    })
 # ! ========================= R12 - Salvar usuários em Arquivo =========================

    with open("usuarios.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{nome},{email},{senha}\n")

    return True

import os

def login_user(login_email, login_senha, usuarios):
    if not login_email or not login_senha:
        print("\n\033[1;31mEmail e senha são obrigatórios!\033[0m\n")
        input("Pressione enter para voltar")
        os.system("cls" if os.name == "nt" else "clear")
        return None
    
    for usuario in usuarios:
        if usuario['email'] == login_email and usuario['senha'] == login_senha:
            print("\n\033[1;32mLogin realizado com sucesso!\033[0m")
            print(f"\n\033[1;32mBem-vindo,\033[0m \033[1m{usuario['nome']}\033[0m")
            input("\nPressione enter para voltar ao menu principal ")
            os.system("cls" if os.name == "nt" else "clear")
            return usuario

    print("\n\033[1;31mEmail ou senha incorretos!\033[0m\n")
    input("Pressione enter para voltar ao menu principal ")
    os.system("cls" if os.name == "nt" else "clear")
    return None

def tela_aba_chup():
    print("""\n
                ╔═════════════════════════════════════════╗
                ║         🚗  ABA DE CHUPETAS  🚗         ║
                ╚═════════════════════════════════════════╝
                    \n""")
    print("[1] Cadastrar nova carona")
    print("[2] Editar caronas cadastradas")
    print("[3] Remover caronas")
    print("[4] Relatório de caronas")
    print("[0] Voltar\n")

def tela_cad_car():
    print("""\n
        ╔══════════════════════════════════════════════════╗
        ║            🛵 CADASTRAR UMA NOVA CARONA          ║
        ╚══════════════════════════════════════════════════╝
        \n""")


    print('Preencha os campos corretamente (confirme "\033[1msair\033[0m" para voltar)\n')

def cad_origem():
    while True:
        origem = input("Digite a origem: ").strip()
        if origem.lower() == 'sair':
            return None, True
        elif not origem:
            print("\n\033[1;31mA origem não pode ser vazia!\033[0m\n")
        else:
            return origem.title(), False

def cad_destino(origem):
    while True:
        destino = input("Digite o destino: ")
        if(destino.strip().lower() == 'sair'):
            return None, True
        elif not destino.strip():
            print("\n\033[1;31mO destino não pode ser vazio!\033[0m\n")
            continue
        elif(destino.strip().title() == origem):
            print("\n\033[1;31mO destino não pode ser igual a origem!\033[0m\n")
            continue
        else:
            return destino.strip().title(), False

def cad_data():
    while True:
        data = input("Digite a data da carona (dd/mm/aaaa): ")
        if(data.lower() == 'sair'):
            return None, True
        elif not data.strip():
            print("\n\033[1;31mA data não pode ser vazia!\033[0m\n")
        elif (
            len(data) == 10 and
            data[2] == '/' and
            data[5] == '/' and
            data[:2].isdigit() and
            data[3:5].isdigit() and
            data[6:].isdigit()
        ):
            dia = int(data[:2])
            mes = int(data[3:5])
            ano = int(data[6:])

            if ano < 2025:
                print("\n\033[1;31mData inválida!\033[0m\n")
            elif ano == 2025:
                if mes < 5 or mes > 12:
                    print("\n\033[1;31mData inválida!\033[0m\n")
                elif mes == 5 and dia < 12:
                    print("\n\033[1;31mData inválida!\033[0m\n")
                else:
                    return data, False
            elif ano > 2026:
                print("\n\033[1;31mA data não pode ultrapassar o limite de 1 ano!\033[0m\n")
            elif ano == 2026:
                if mes > 5:
                    print("\n\033[1;31mA data não pode ultrapassar o limite de 1 ano!\033[0m\n")
                elif mes == 5 and dia > 12:
                    print("\n\033[1;31mA data não pode ultrapassar o limite de 1 ano!\033[0m\n")
                else:
                    return data, False
            else:
                return data, False
        else:
            print("\n\033[1;31mFormato inválido! Use exatamente dd/mm/aaaa\033[0m\n")

def cad_horario():
    while True:
        horario = input("Digite o horário da carona (ex: 14:00): ")
        if horario.lower() == 'sair':
            return None, True
        elif not horario.strip():
            print("\n\033[1;31mO horário não pode ser vazio!\033[0m\n")
        elif (
            len(horario) == 5 and
            horario[2] == ':' and
            horario[:2].isdigit() and
            horario[3:].isdigit()
        ):
            horas = int(horario[:2])
            minutos = int(horario[3:])

            if 0 <= horas <= 23 and 0 <= minutos <= 59:
                return horario, False
            else:
                print("\n\033[1;31mHorário inválido! Use valores entre 00:00 e 23:59\033[0m\n")
        else:
            print("\n\033[1;31mUse o formato hh:mm\033[0m\n")

def cad_vagas():
    while True:
        vagas = input("Digite a quantidade de vagas: ")
        if vagas.lower() == 'sair':
            return None, True
        elif not vagas.strip():
            print("\n\033[1;31mO número de vagas não pode ser vazio!\033[0m\n")
        elif vagas.isdigit():
            vagas_int = int(vagas)
            if vagas_int > 0:
                return vagas_int, False
            else:
                print("\n\033[1;31mVocê deve disponibilizar pelo menos uma vaga!\033[0m\n")
        else:
            print("\n\033[1;31mDigite apenas números inteiros positivos!\033[0m\n")

def cad_valor():
    while True:
        valor = input("Digite o valor por vaga (ex: 10.00): ")
        if valor.lower() == 'sair':
            return None, True
        elif not valor.strip():
            print("\n\033[1;31mO valor não pode ser vazio!\033[0m\n")
        else:
            tem_ponto = False
            valor_tru = True

            for caractere in valor:
                if caractere in ('.', ','):
                    if tem_ponto:
                        valor_tru = False
                        break
                    tem_ponto = True
                elif not caractere.isdigit():
                    valor_tru = False
                    break

            if valor_tru:
                val_float = float(valor.replace(',', '.'))
                return val_float, False
            else:
                print("\n\033[1;31mApenas números são aceitos! (utilize ponto ou vírgula para centavos)\033[0m\n")

def tela_editar_car():
    print("""\n
        ╔════════════════════════════════════════╗
        ║         ✏️ EDITAR CARONAS POSTADAS      ║
        ╚════════════════════════════════════════╝
        \n""")

def ediatr_carona(caronas, usuario_logado):
    minhas_caroninhas = []

    for carona in caronas:
        if carona['motorista_email'] == usuario_logado['email']:
            minhas_caroninhas.append(carona)

    if len(minhas_caroninhas) == 0:
        print("\n\033[1;33mVocê não possui caronas cadastradas.\033[0m\n")
        input("Pressione enter para continuar ")
        os.system("cls" if os.name == "nt" else "clear")
        return

    for i in range(len(minhas_caroninhas)):
        carona = minhas_caroninhas[i]
        print(f"\n[{i + 1}] {carona['origem']} --> {carona['destino']} | Data: {carona['data']} às {carona['horario']}")
        print(f"\n    Vagas: {carona['vagas']} | Valor: R${carona['valor']}")

    print("\n[0] Voltar\n")
    editar_carona = input("Digite o número da carona que deseja editar: ")

    if editar_carona == '0':
        os.system("cls" if os.name == "nt" else "clear")
        return

    if editar_carona == '':
        print("\n\033[1;31mVocê não digitou nada, chupeta!\033[0m\n")
        input("Pressione enter para continuar ")
        os.system("cls" if os.name == "nt" else "clear")
        return

    if not editar_carona.isdigit() or int(editar_carona) < 1 or int(editar_carona) > len(minhas_caroninhas):
        print("\n\033[1;31mOpção inválida!\033[0m\n")
        input("Pressione enter para continuar ")
        os.system("cls" if os.name == "nt" else "clear")
        return

    edicao = int(editar_carona) - 1
    carona_selecionada = minhas_caroninhas[edicao]

    print("\n\033[1mEdição de carona selecionada:\033[0m\n")
    print(f"{carona_selecionada['origem']} --> {carona_selecionada['destino']} | Data: {carona_selecionada['data']} às {carona_selecionada['horario']}\n")

    carona_selecionada['origem'] = input("Nova origem (deixe em branco para manter): ") or carona_selecionada['origem']
    carona_selecionada['destino'] = input("Novo destino (deixe em branco para manter): ") or carona_selecionada['destino']
    carona_selecionada['data'] = input("Nova data (deixe em branco para manter): ") or carona_selecionada['data']
    carona_selecionada['horario'] = input("Novo horário (deixe em branco para manter): ") or carona_selecionada['horario']
    carona_selecionada['vagas'] = input("Novo quantidade de vagas (deixe em branco para manter): ") or carona_selecionada['vagas']
    carona_selecionada['valor'] = input("Novo valor por vaga (deixe em branco para manter): ") or carona_selecionada['valor']

    print("\n\033[1;32mCarona atualizada com sucesso!\033[0m\n")
    input("Pressione enter para continuar ")
    os.system("cls" if os.name == "nt" else "clear")

def tela_remover_car():
    print("""\n
        ╔══════════════════════════════════════╗
        ║           🗑️ REMOVER CARONAS          ║
        ╚══════════════════════════════════════╝
        \n""")
    
def caronitas(caronitas):
     for i in range(len(caronitas)):
        carona = caronitas[i]
        print(f"\n[{i + 1}] {carona['origem']} --> {carona['destino']} | Data: {carona['data']} às {carona['horario']}")
        print(f"    Vagas: {carona['vagas']} | Valor: R${carona['valor']}")

def filtrar_caronitas(caronas, usuario_logado):

    caronitas = []

    for carona in caronas:
        if carona['motorista_email'] == usuario_logado['email']:
            caronitas.append(carona)

    if len(caronitas) == 0:
        print("\n\033[1;33mVocê não possui caronas cadastradas.\033[0m\n")
        input("Pressione enter para continuar ")
        os.system("cls" if os.name == "nt" else "clear")
        return None
    else:
        return caronitas

def remover_caronitas(caronas, caronitas):
    print("\n[0] Voltar")
    escolha = input("\nDigite o número da carona que deseja remover: ")
    if(escolha == '0'):
        os.system("cls" if os.name == "nt" else "clear")
        return caronas, False
    elif(escolha == ''):
        print("\n\033[1;31mOpção inválida!\033[0m\n")
        input("Pressione enter para tentar novamente ")
        os.system("cls" if os.name == "nt" else "clear")
        return caronas, False
    escolha = int(escolha)
    if(escolha >= 1 and escolha <= len(caronitas)):
        print("\n[0] Sim  /  [1] Não\n")
        confirmar = input("Tem certeza que deseja remover essa carona? ")
        if(confirmar == "0"):
            caronia_p_remover = caronitas[escolha - 1]
            nova_lista_caronas = []
            for car in caronas:
                if(car != caronia_p_remover):
                    nova_lista_caronas.append(car)
            caronas = nova_lista_caronas
            print("\033[1;32m" + "\nCarona removida com sucesso." + "\033[0m")
            input("\nPressione Enter para continuar ")
            os.system("cls" if os.name == "nt" else "clear")
        else:
            print("\nRemoção cancelada\n")
            input("Pressione Enter para continuar ")
            os.system("cls" if os.name == "nt" else "clear")
    else:
        print("\n\033[1;31mNúmero inválido\033[0m\n")
        input("Pressione Enter para continuar ")
        os.system("cls" if os.name == "nt" else "clear")
    return caronas, True

def gerar_chupetorio(caronas, usuario_logado):
    encontrado = False
    moneys = 0.0
    chupetorio = []

    for carona in caronas:
        if carona['motorista_email'] == usuario_logado['email']:
            encontrado = True
            origem_14 = carona['origem']
            destino_14 = carona['destino']
            data_14 = carona['data']
            valor_14 = float(carona['valor'])
            vagas_sobrano = int(carona['vagas'])

            if 'reservas' in carona:
                vagocupadas = len(carona['reservas']) // 2
            else:
                vagocupadas = 0

            total_vag = valor_14 * vagocupadas
            moneys += total_vag

            atalho_hehehe = (
                (f"Origem: {origem_14}\n") +
                (f"Destino: {destino_14}\n") +
                (f"Data: {data_14}\n") +
                (f"Valor por vaga: R${valor_14:.2f}\n") +
                (f"Vagas restantes: {vagas_sobrano}\n") +
                (f"Total recebido: R${total_vag:.2f}\n") +
                ("-=" * 16)
            )
            print(atalho_hehehe)
            chupetorio.append(atalho_hehehe)

    if not encontrado:
        print("Não há caronas cadastradas.")
    else:
        total_tal = (f"\nTOTAL GERAL RECEBIDO: R${moneys:.2f}\n")
        print(total_tal)
        chupetorio.append(total_tal)

 # ! ========================= R15 - Salvar relatório =========================

        salvo = input("\nDeseja salvar o relatório em .txt? (s/n): ").strip().lower()
        if salvo == 's':
            print("Pididi")
            with open("chupetorio.txt", 'w', encoding="utf-8") as relatorio:
                relatorio.write("RELATÓRIO DE CHUPETAS CADASTRADAS\n\n")
                relatorio.writelines(chupetorio)
            print("Relatório salvo com sucesso como 'chupetorio.txt'.\n")

    input("Pressione enter para continuar ")

def tela_aba_pass():
    print("""\n
        ╔════════════════════════════════════════════╗
        ║        🧍  ABA DE PASSAGEIROS  🧍          ║
        ╚════════════════════════════════════════════╝
        \n""")
    print("[1] Ver caronas disponíveis")
    print("[2] Buscar caronas")
    print("[3] Ver caronas reservadas")
    print("[4] Cancelar reservas")
    print("[5] Avaliar Chupetas disponíveis")
    print("[0] Voltar\n")

def car_disp(caronas, caronas_disponiveis, reservas):
    caronas_disponiveis.clear()

    os.system("cls" if os.name == "nt" else "clear")

    for i in range(len(caronas)):
        carona_atual = caronas[i]
        if(carona_atual["motorista_email"] and int(carona_atual["vagas"]) > 0):
            caronas_disponiveis.append(carona_atual)

    if(not caronas_disponiveis):
        print("\033[1;31m" + "\n\033[1;33mNão há caronas disponíveis no momento.\033[0m\n" + "\033[0m")
        input("Pressione enter para continuar ")
        os.system("cls" if os.name == "nt" else "clear")
        return

    print("\nCaronas disponíveis:")
    for i in range(len(caronas_disponiveis)):
        carona = caronas_disponiveis[i]
        print(f"\n[{i + 1}] {carona['origem']} --> {carona['destino']} | Data: {carona['data']} às {carona['horario']}")
        print(f"\n    Vagas: {carona['vagas']} | Valor: R${carona['valor']}")
    print("\n[0] Voltar\n")

    escolha = input("Digite o número da carona para visualizá-la ")

    if(escolha == '0'):
        os.system("cls" if os.name == "nt" else "clear")
        return

    if(not escolha.isdigit() or int(escolha) < 1 or int(escolha) > len(caronas_disponiveis)):
        print("\n\033[1;31mOpção inválida!\033[0m\n")
        input("Pressione enter para continuar ")
        os.system("cls" if os.name == "nt" else "clear")
        return

    selecionado = int(escolha) - 1
    carona = caronas_disponiveis[selecionado]

    if(int(carona['vagas']) > 0):
        print("\n\033[1mDetalhes da Carona Selecionada:\033[0m\n")
        print(f"Origem: {carona['origem']}")
        print(f"Destino: {carona['destino']}")
        print(f"Data: {carona['data']}")
        print(f"Horário: {carona['horario']}")
        print(f"Vagas: {carona['vagas']}")
        print(f"Valor por vaga: R${carona['valor']}")
        print(f"Motorista: {carona['motorista_nome']}")

 # ! ========================= R8 - Mostrar passageiros =========================
        encontrou_passageiro = False
        for r in reservas:
            if r['carona'] == carona:
                print("Passageiro:", r["passageiro_nome"])
                encontrou_passageiro = True
        if not encontrou_passageiro:
            print("Sem passageiros por enquanto")

# ! ========================= R5 - Reservar vaga em carona =========================

def res_vaga(carona, usuario_logado, reservas):
    reservar = input("\nGostaria de reservar vaga? (s/n) ")
    if(reservar.lower() == 's'):
        if('reservas' not in carona):
            carona['reservas'] = []
        if(usuario_logado['email'] in carona['reservas']):
            print("\n\033[1;33mVocê já reservou essa carona.\033[0m\n")
        elif(carona['motorista_email'] == usuario_logado['email']):
            print("\033[1;31m" + "\n\033[1;33mVocê não pode reservar sua própria carona\033[0m\n" + "\033[0m")
            input("Pressione enter para voltar ")
            os.system("cls" if os.name == "nt" else "clear")
            return
        else:
            reservas.append({
                "passageiro_nome": usuario_logado['nome'],
                "passageiro_email": usuario_logado['email'],
                "carona": carona
            })

            carona['vagas'] = int(carona['vagas']) - 1
            carona['reservas'].append(usuario_logado['nome'])
            carona['reservas'].append(usuario_logado['email'])
            print("\n\033[1;32mReserva efetuada com sucesso!\033[0m")
    elif(reservar.lower() == 'n'):
        input("\nPressione enter para voltar ")
        os.system("cls" if os.name == "nt" else "clear")
        return
    else:
        print("\n\033[1;33mEssa carona não possui vagas disponíveis.\033[0m\n")
        input("\nPressione enter para voltar ")
        os.system("cls" if os.name == "nt" else "clear")

# ! ========================= R5 - Reservar vaga em carona =========================

def faz_res(carona, usuario_logado, reservas):
    reservar = input("\nGostaria de reservar vaga? (s/n) ")
    if(reservar.lower() == 's'):
        if('reservas' not in carona):
            carona['reservas'] = []
        if(usuario_logado['email'] in carona['reservas']):
            print("\n\033[1;33mVocê já reservou essa carona.\033[0m\n")
        elif(carona['motorista_email'] == usuario_logado['email']):
            print("\033[1;31m" + "\n\033[1;33mVocê não pode reservar sua própria carona\033[0m\n" + "\033[0m")
            input("Pressione enter para voltar ")
            os.system("cls" if os.name == "nt" else "clear")
            return
        else:
            reservas.append({
                "passageiro_nome": usuario_logado['nome'],
                "passageiro_email": usuario_logado['email'],
                "carona": carona
            })

            carona['vagas'] = int(carona['vagas']) - 1
            carona['reservas'].append(usuario_logado['nome'])
            carona['reservas'].append(usuario_logado['email'])
            print("\n\033[1;32mReserva efetuada com sucesso!\033[0m")
    elif(reservar.lower() == 'n'):
        input("\nPressione enter para voltar ")
        os.system("cls" if os.name == "nt" else "clear")
        return
    else:
        print("\n\033[1;33mEssa carona não possui vagas disponíveis.\033[0m\n")
        input("\nPressione enter para voltar ")
        os.system("cls" if os.name == "nt" else "clear")

def tela_buscar_car():
    print("""\n
        ╔══════════════════════════════════════════╗
        ║       🔍 BUSCAR CARONAS DISPONÍVEIS      ║
        ╚══════════════════════════════════════════╝
        \n""")

    print("[0] Voltar\n")

def bus_res_car(buscar_origem, caronas_disponiveis, usuario_logado, reservas):
    origem_encontrada = False

    for carona in caronas_disponiveis:
        if(carona['origem'] == buscar_origem):
            origem_encontrada = True
            break

    if(not origem_encontrada):
        print(f"\033[1;31m\nNão existem caronas que partam de {buscar_origem}\033[0m")
        input("\nPressione enter para voltar ")
        os.system("cls" if os.name == "nt" else "clear")
        return

    buscar_destino = input("\nPara: ").strip().title()
    if(buscar_destino == '0'):
        os.system("cls" if os.name == "nt" else "clear")
        return

    caronas_encontradas = []
    for i in range(len(caronas_disponiveis)):
        carona = caronas_disponiveis[i]
        if(carona['origem'] == buscar_origem and carona['destino'] == buscar_destino):
            caronas_encontradas.append((i, carona))

    if(len(caronas_encontradas)) == 0:
        print(f"\033[1;31m\nNão existem caronas de {buscar_origem} para {buscar_destino}\033[0m\n")
        input("Pressione enter para voltar ")
        os.system("cls" if os.name == "nt" else "clear")
        return

    print("\nCaronas encontradas:\n")
    for caroninhas in caronas_encontradas:
        numero = caroninhas[0]
        carona = caroninhas[1]
        print(f"[{numero + 1}] {carona['origem']} --> {carona['destino']} | Data: {carona['data']} às {carona['horario']}")
        print(f"\n    Vagas: {carona['vagas']} | Valor: R${carona['valor']}\n")

        escolha = input("Digite o número da carona para visualizá-la ")

    if(escolha == '0'):
        os.system("cls" if os.name == "nt" else "clear")
        return

    if(not escolha.isdigit() or int(escolha) < 1 or int(escolha) > len(caronas_disponiveis)):
        print("\n\033[1;31mOpção inválida!\033[0m\n")
        input("Pressione enter para continuar ")
        os.system("cls" if os.name == "nt" else "clear")
        return

    selecionado = int(escolha) - 1
    carona = caronas_disponiveis[selecionado]

    if(int(carona['vagas']) > 0):
        
        print("\n\033[1mDetalhes da Carona Selecionada:\033[0m\n")
        print(f"Origem: {carona['origem']}")
        print(f"Destino: {carona['destino']}")
        print(f"Data: {carona['data']}")
        print(f"Horário: {carona['horario']}")
        print(f"Vagas: {carona['vagas']}")
        print(f"Valor por vaga: R${carona['valor']}")
        print(f"Motorista: {carona['motorista_nome']}")

        for r in reservas:
            if(r['carona'] == carona):
                print("Passageiros:", r["passageiro_nome"]) 
            else:
                print("\nSem passageiros por enquanto")

        reservar = input("\nGostaria de reservar vaga? (s/n) ")
        if(reservar.lower() == 's'):
            if('reservas' not in carona):
                carona['reservas'] = []
            if(usuario_logado['email'] in carona['reservas']):
                print("\n\033[1;33mVocê já reservou essa carona.\033[0m")
            elif(carona['motorista_email'] == usuario_logado['email']):
                print("\033[1;31m" + "\n\033[1;33mVocê não pode reservar sua própria carona.\033[0m" + "\033[0m")
                input("\nPressione enter para voltar ")
                os.system("cls" if os.name == "nt" else "clear")
                return
            else:
                reservas.append({
                    "passageiro_nome": usuario_logado['nome'],
                    "passageiro_email": usuario_logado['email'],
                    "carona": carona
                })

                carona['vagas'] = int(carona['vagas']) - 1
                carona['reservas'].append(usuario_logado['email'])
                print("\n\033[1;32mReserva efetuada com sucesso!\033[0m")
        elif(reservar.lower() == 'n'):
            input("\nPressione enter para voltar ")
            os.system("cls" if os.name == "nt" else "clear")
            return
    else:
        print("\n\033[1;33mEssa carona não possui vagas disponíveis.\033[0m\n")

    input("\nPressione enter para voltar ")
    os.system("cls" if os.name == "nt" else "clear")

def ver_car_res(reservas, usuario_logado):
    my_reservinhas = []

    for reserva in reservas:
        if(reserva['passageiro_email'] == usuario_logado['email']):
            my_reservinhas.append(reserva)

    if(len(my_reservinhas) == 0):
        print("\033[1;31m" + "\n\033[1;33mVocê não possui nenhuma carona reservada.\033[0m\n" + "\033[0m")
        input("Pressione enter para continuar ")
        os.system("cls" if os.name == "nt" else "clear")
        return

    print("""\n
        ╔═══════════════════════════════════════════╗
        ║         📅 VER CARONAS RESERVADAS         ║
        ╚═══════════════════════════════════════════╝
        \n""")

    for i in range(len(my_reservinhas)):
        carona = my_reservinhas[i]['carona']
        print(f"\n\033[4m[{i + 1}] {carona['origem']} --> {carona['destino']} | Data: {carona['data']} às {carona['horario']}\033[0m")
        print(f"    Motorista: {carona['motorista_nome']} | Vagas restantes: {carona['vagas']} | Valor: R${carona['valor']}")

    input("\nPressione enter para continuar ")
    os.system("cls" if os.name == "nt" else "clear")

def canc_res(usuario_logado, caronas):
    global reservas

    my_reservinhas = []

    for reserva in reservas:
        if(reserva['passageiro_email'] == usuario_logado['email']):
            my_reservinhas.append(reserva)

    if(len(my_reservinhas) == 0):
        print("\033[1;31m" + "\n\033[1;33mVocê não possui nenhuma reserva para cancelar.\033[0m\n" + "\033[0m")
        input("Pressione enter para continuar ")
        os.system("cls" if os.name == "nt" else "clear")
        return

    while True:
        print("""\n
            ╔════════════════════════════════════════╗
            ║          ❌ CANCELAR RESERVAS          ║
            ╚════════════════════════════════════════╝
            \n""")

        for i in range(len(my_reservinhas)):
            carona = my_reservinhas[i]['carona']
            print(f"\n[{i + 1}] {carona['origem']} --> {carona['destino']} | Data: {carona['data']} às {carona['horario']}")
            print(f"    Motorista: {carona['motorista_nome']} | Vagas restantes: {carona['vagas']} | Valor: R${carona['valor']}")
        print("\n[0] Voltar\n")

        cancelamento = input("Selecione a reserva que deseja cancelar: ")

        if(cancelamento == '0'):
            os.system("cls" if os.name == "nt" else "clear")
            break

        if(not cancelamento.isdigit() or int(cancelamento) < 1 or int(cancelamento) > len(my_reservinhas)):
            print("\n\033[1;31mOpção inválida!\033[0m\n")
            input("Pressione enter para continuar ")
            os.system("cls" if os.name == "nt" else "clear")
            continue

        cancela = int(cancelamento) - 1
        reserva_cancelada = my_reservinhas.pop(cancela)
        reservas.remove(reserva_cancelada)
        carona_cancelada = reserva_cancelada['carona']

        for carona in caronas:
            if (carona['origem'] == carona_cancelada['origem'] and
                carona['destino'] == carona_cancelada['destino'] and
                carona['data'] == carona_cancelada['data'] and
                carona['horario'] == carona_cancelada['horario'] and
                carona['motorista_email'] == carona_cancelada['motorista_email']):

                carona['vagas'] = int(carona['vagas']) + 1
                if('reservas' in carona):
                    carona['reservas'] = [email for email in carona['reservas'] if email != usuario_logado['email']]
                break

        print("\n\033[1;32mReserva cancelada com sucesso!\033[0m\n")
        input("Pressione enter para continuar ")
        os.system("cls" if os.name == "nt" else "clear")

def tela_ava():
    print("""\n
        ╔════════════════════════════════════════════╗
        ║          🌟 AVALIAR MOTORISTAS 🌟          ║
        ╚════════════════════════════════════════════╝
            \n""")

def ava_chup(caronas, usuario_logado):
    global avaliacoes

    if not caronas:
        print("\033[1;31m" + "Nenhum motorista disponível no momento" + "\033[0m")
        input("\nPressione enter para voltar ")
        os.system("cls" if os.name == "nt" else "clear")
        return

    motoristas = []
    print("Motoristas disponíveis para avaliação:\n")
    for carona in caronas:
        nome_motorista = carona['motorista_nome']
        if nome_motorista not in motoristas:
            motoristas.append(nome_motorista)

    for i in range(len(motoristas)):
        nome = motoristas[i]
        total = 0
        quantidade = 0

        for usu_ava in avaliacoes:
            if nome in avaliacoes[usu_ava]:
                total += avaliacoes[usu_ava][nome]
                quantidade += 1

        if quantidade > 0:
            media = total / quantidade
            estrelas = '⭐' * int(media)
            quebra = media - int(media)
            if quebra >= 0.75:
                estrelas += '⭐'
            elif quebra >= 0.25:
                estrelas += '◐'
            while len(estrelas) < 5:
                estrelas += '☆'
            print(f"[{i + 1}] {nome} {estrelas} ({media:.1f})\n")
        else:
            print(f"[{i + 1}] {nome} ☆☆☆☆☆ (sem nota)\n")

    print("[0] Voltar\n")

    escolha = input("Selecione um motorista para visualizar os detalhes: ").strip()

    if escolha == '0':
        os.system("cls" if os.name == "nt" else "clear")
        return

    if not escolha.isdigit():
        print("\033[1;31m\nEntrada inválida. Digite apenas números\033[0m")
        input("\nPressione enter para voltar ")
        os.system("cls" if os.name == "nt" else "clear")
        return

    escolha_int = int(escolha)

    if escolha_int < 1 or escolha_int > len(motoristas):
        print("\033[1;31m\nEscolha fora do intervalo.\033[0m")
        input("\nPressione enter para voltar ")
        os.system("cls" if os.name == "nt" else "clear")
        return

    motorista = motoristas[escolha_int - 1]
    usuario_nome = usuario_logado["nome"]

    if motorista == usuario_nome:
        print("\033[1;31m\nVocê não pode se autoavaliar\033[0m")
        input("\nPressione enter para voltar ")
        os.system("cls" if os.name == "nt" else "clear")
        return

    if usuario_nome not in avaliacoes:
        avaliacoes[usuario_nome] = {}

    if motorista in avaliacoes[usuario_nome]:
        print(f"\n\033[1mVocê já avaliou {motorista} antes. A nota será substituída.\033[0m")

    nota_txt = input("\nAvalie este motorista com uma nota de 0 a 5: ").strip()
    partes = nota_txt.split('.')
    valido = True

    if nota_txt == '' or len(partes) > 2:
        valido = False

    for parte in partes:
        if parte != "" and not parte.isdigit():
            valido = False

    if not valido:
        print("\033[1;31m\nNota inválida. Use apenas números e no máximo um ponto\033[0m")
        input("\nPressione enter para voltar ")
        os.system("cls" if os.name == "nt" else "clear")
        return

    nota = float(nota_txt)

    if nota < 0 or nota > 5:
        print("\033[1;31m\nNota fora do intervalo permitido (0 a 5)\033[0m")
        input("\nPressione enter para voltar ")
        os.system("cls" if os.name == "nt" else "clear")
        return

    avaliacoes[usuario_nome][motorista] = nota

    print("\033[1;32m\nObrigado! Avaliação registrada para:", motorista + "\033[0m")

    estrelas = '⭐' * int(nota)
    quebra = nota - int(nota)
    if quebra >= 0.75:
        estrelas += '⭐'
    elif quebra >= 0.25:
        estrelas += '◐'
    while len(estrelas) < 5:
        estrelas += '☆'

    print(f"\n{estrelas}\n")
    input("Pressione enter para voltar ao menu ")
    os.system("cls" if os.name == "nt" else "clear")