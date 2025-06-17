import os
import funcoes

# ! Apresentar próxima segunda!!!

caronas_disponiveis = []
usuarios = []

# ! ========================= R13 - Importar usuários salvos no Arquivo =========================

if os.path.exists("usuarios.txt"):
    with open("usuarios.txt", "r", encoding="utf-8") as arquivo:
        for linhas in arquivo:
            nome, email, senha = linhas.strip().split(",")
            usuarios.append({'nome': nome, 'email': email, 'senha': senha})
caronas = []
reservas = []
usuario_logado = None
avaliacoes = {}


# ? ========================= Menu Principal =========================

while(True):
    print(""" 
  _______ ___ ___ ___ ___ _______ _______ _______ _______     _______ _______ _______ ®
 |   _   |   Y   |   Y   |   _   |   _   |       |   _   |   |   _   |   _   |   _   `
 |.  1___|.  1   |.  |   |.  1   |.  1___|.|   | |.  1   |   |.  1___|.  1   |.  l   /
 |.  |___|.  _   |.  |   |.  ____|.  __)_`-|.  |-|.  _   |   |.  |___|.  _   |.  _   |
 |:  1   |:  |   |:  1   |:  |   |:  1   | |:  | |:  |   |   |:  1   |:  |   |:  |   |
 |::.. . |::.|:. |::.. . |::.|   |::.. . | |::.| |::.|:. |   |::.. . |::.|:. |::.|:. |
 `-------`--- ---`-------`---'   `-------' `---' `--- ---'   `-------`--- ---`--- ---'
                                                                                      
 """)
    
    if(usuario_logado == None):
        permitidos = ['0', '1', '2', '3', '4', '6']
    elif(usuario_logado != None):
        permitidos = ['0', '1', '3', '4', '5', '6']
    
    funcoes.opc_menu(usuario_logado, permitidos)

    opcao_menu = input("Selecione uma opção: ")

    while opcao_menu not in permitidos:
        print("\n\033[1;31mOpção inválida!\033[0m\n")
        funcoes.opc_menu(usuario_logado, permitidos)
        opcao_menu = input("Selecione uma opção: ")

    if(opcao_menu == '0'):
        print("\n[0] Sim | [1] Não")
        son = input("\nTem certeza que desejar sair? ")
        if(son == '1'):
            continue
        elif(son == '0'):
            print("\nJá vai tarde...\n")
            break
        else:
            print("\033[1;31mOpção inválida!\033[0m\n")
            input("Pressione enter para continuar ")
            os.system("cls" if os.name == "nt" else "clear")
            continue

 #! ========================= R0 - Cadastrar novo usuário =========================

    elif(opcao_menu == '1'):
        funcoes.cadastrar_user(usuarios)
        if email == None:
            continue
        else:
            input("\nPressione enter para voltar ao menu principal ")
            os.system("cls" if os.name == "nt" else "clear")
        
 # ! ========================= R12 - Salvar usuários em Arquivo =========================

 #! ========================= R1 - Login =========================

    elif(opcao_menu == '2'):
        login_email = input("\nDigite seu email: ")
        login_senha = input("Digite sua senha: ")
        usuario_logado = funcoes.login_user(login_email, login_senha, usuarios)
        
        if usuario_logado:
            print("Login concluído!")
        else:
            print("Login falhou!")

 # ! ========================= R2 - Cadastro de Carona =========================

    elif(opcao_menu == '3'):
        os.system("cls" if os.name == "nt" else "clear")

        if(usuario_logado == None):
            print("\n\033[1;31mVocê precisa estar logado para acessar a aba de Chupetas!\033[0m\n")
            input("Pressione enter para voltar ao menu principal ")
            os.system("cls" if os.name == "nt" else "clear")
            continue

        while (True):
            os.system("cls" if os.name == "nt" else "clear")
            volta = False

            funcoes.tela_aba_chup()
            opcao_motorista = input("Selecione uma opção: ")
            
            if(opcao_motorista == '0'):
                os.system("cls" if os.name == "nt" else "clear")
                break

            elif(opcao_motorista == '1'):
                os.system("cls" if os.name == "nt" else "clear")
                funcoes.tela_cad_car()

                origem, volta = funcoes.cad_origem()

                destino, volta = funcoes.cad_destino(origem)
                if(volta):
                    continue
                
                data, volta = funcoes.cad_data()
                if(volta):
                    continue
                
                horario, volta = funcoes.cad_horario()
                if(volta):
                    continue

                vagas, volta = funcoes.cad_vagas()
                if(volta):
                    continue

                valor, volta = funcoes.cad_valor()
                if(volta):
                    continue

                caronas.append({
                    "motorista_nome": usuario_logado['nome'],
                    "motorista_email": usuario_logado['email'],
                    "origem": origem,
                    "destino": destino,
                    "data": data,
                    "horario": horario,
                    "vagas": vagas,
                    "valor": valor
                })

                print("\n\033[1;32mCarona cadastrada com sucesso!\033[0m\n")
                input("Pressione enter para continuar ")
                os.system("cls" if os.name == "nt" else "clear")
                if volta:
                    break
                continue

 # ? ========================= Editar caronas =========================

            elif(opcao_motorista == '2'):
                os.system("cls" if os.name == "nt" else "clear")
                funcoes.tela_editar_car()
                funcoes.ediatr_carona(caronas, usuario_logado)

 # ! ========================= R7 - Remover carona =========================

            elif(opcao_motorista == '3'):
                os.system("cls" if os.name == "nt" else "clear")
                funcoes.tela_remover_car()

                caronitas = funcoes.filtrar_caronitas(caronas, usuario_logado)
                if(caronitas == None):
                    continue

                funcoes.caronitas(caronitas)

                caronas, continuar_loop = funcoes.remover_caronitas(caronas, caronitas)
                if not continuar_loop:
                    continue

 # ! ========================= R14 - Relatório de totalizadores =========================

            elif(opcao_motorista == '4'):
                funcoes.gerar_chupetorio(caronas, usuario_logado)

 # ! ========================= R3 - Listar todas as caronas disponíveis =========================

    elif(opcao_menu == '4'):
        os.system("cls" if os.name == "nt" else "clear")

        if(usuario_logado == None):
            print("\n\033[1;31mVocê precisa estar logado para acessar a aba de passageiros!\033[0m\n")
            input("Pressione enter para voltar ao menu principal ")
            os.system("cls" if os.name == "nt" else "clear")
            continue
        while(True):
            funcoes.tela_aba_pass()
            opcao_passageiros = input("Selecione uma opção: ")

            if(opcao_passageiros == '0'):
                os.system("cls" if os.name == "nt" else "clear")
                break

            elif(opcao_passageiros == '1'):
                os.system("cls" if os.name == "nt" else "clear")

                funcoes.car_disp(caronas, caronas_disponiveis, reservas)

                funcoes.res_vaga(caronas, usuario_logado, reservas)

                funcoes.faz_res(caronas, usuario_logado, reservas)

 # ! ==================== R4 - Buscar carona por origem e destino ====================

            elif(opcao_passageiros == '2'):
                os.system("cls" if os.name == "nt" else "clear")
                while(True):
                    funcoes.tela_buscar_car()
                    buscar_origem = input("De: ").strip().title()
                    if(buscar_origem == '0'):
                        os.system("cls" if os.name == "nt" else "clear")
                        break
                    funcoes.bus_res_car(caronas_disponiveis, usuario_logado, reservas)

 # ? ========================= Mostrar Reservas =========================

            elif(opcao_passageiros == '3'):
                funcoes.ver_car_res(reservas, usuario_logado)

 # ! ========================= R6 - Cancelar reserva =========================

            elif(opcao_passageiros == '4'):
                funcoes.canc_res(usuario_logado, caronas)

 # ? ========================= Avaliar Motorista =========================

            elif (opcao_passageiros == '5'):
                os.system("cls" if os.name == "nt" else "clear")
                while True:
                    funcoes.tela_ava()
                    funcoes.ava_chup(caronas, usuario_logado)

 # ! ========================= R10 - Logout =========================

    if(usuario_logado != None):
        if(opcao_menu == '5'):
            os.system("cls" if os.name == "nt" else "clear")
            while(True):
                print("\n[0] Sim | [1] Não")
                ctz = input("\nTem certeza que desejar deslogar de sua conta atual? ")
                print("\n")
                if(ctz == '1'):
                    break
                elif(ctz == '0'):
                    permitidos.remove('5')
                    usuario_logado = None
                    os.system("cls" if os.name == "nt" else "clear")
                    break
                else:
                    print("\033[1;31mOpção inválida!\033[0m\n")
                    input("Pressione enter para continuar ")
                    os.system("cls" if os.name == "nt" else "clear")
                    continue

    elif(opcao_menu == '6'):
            
        os.system("cls" if os.name == "nt" else "clear")

        print("""
   ______      _ ____                                           ____          ___       __        
  / ____/_  __(_) / /_  ___  _________ ___  ___     _________ _/ __/___ _____/ (_)___  / /_  ____  rsrsrs
 / / __/ / / / / / __ \/ _ \/ ___/ __ `__ \/ _ \   / ___/ __ `/ /_/ __ `/ __  / / __ \/ __ \/ __ `
/ /_/ / /_/ / / / / / /  __/ /  / / / / / /  __/  (__  ) /_/ / __/ /_/ / /_/ / / / / / / / / /_/ /
\____/\__,_/_/_/_/ /_/\___/_/  /_/ /_/ /_/\___/  /____/\__,_/_/  \__,_/\__,_/_/_/ /_/_/ /_/\____/ 
                                                                                                  
                """)
        
        input("\nSai, tô com vergonha hihihi ")
        os.system("cls" if os.name == "nt" else "clear")
        continue