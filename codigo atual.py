import os 
import platform

arquivo = open("Sistema de Treinos.txt", "a")
arquivo.close()

def clear():
    OS = platform.system()
    if OS == "Darwin":
        os.system("clear")
    else:
        os.system("cls")

clear()

def abrir_leitura():
    treino = open("Sistema de Treinos.txt", "r")
    conteudo = treino.read()
    treino.close()

    return conteudo

def pergunta():
    while True:
        resposta = input("Você quer continuar? s/n \nRESPOSTA: ").lower()

        if resposta == "s":
            clear()
            return True

        elif resposta == "n":
            return False
        else: 
            print("RESPOSTA INVÁLIDA!") 

def nomeDOtreino(conteudo):
    while True:
        try:
            nome_treino = input("Digite o nome do treino: ")
        except:
            if f"NOME DO TREINO: {nome_treino.upper().strip()}" in conteudo:
                print("O treino ja existe!\n")
                continue
        else:
            clear()
            break
    return nome_treino

def tipoDEtreino():
    while True:
        try:
            tipo_treino = int(input("[1] CORRIDA / [2] FORÇA / [3] SIMULADO HYROX \n\nDigite o tipo de treino entre os disponíveis: " ))
            
            if tipo_treino == 1:
                tipo = "CORRIDA"
                
            elif tipo_treino == 2:
                tipo = "FORÇA"
            
            elif tipo_treino == 3:
                tipo = "SIMULADO HYROX"
            
        except ValueError, TypeError: 
            clear()
            print("Resposta inválida!")
            continue
        else:
            break
    clear()
    return tipo

def intensidadeDEtreino():
    while True:
        try:
            intensidade_treino = int(input("[1] - LEVE / [2] - MODERADO / [3] - PESADO"
            "\nDigite o número de intensidade: "))

            if intensidade_treino == 1:
                intensidade_final = "Treino Leve"

            elif intensidade_treino == 2:
                intensidade_final = "Treino Moderado"

            elif intensidade_treino == 3:
                intensidade_final = "Treino Pesado"

        except:
            clear()
            print("Resposta Inválida!")
            continue
        
        else:
            break
    clear()
    return intensidade_final
    
def validar_data():
    from datetime import datetime
    while True:
        try:
            data = input("Digite a data do treino (dd/mm/aaaa): ")
            data_formatada = datetime.strptime(data, "%d/%m/%Y")

            clear()
            return data
                
        except ValueError:
            clear()
            print("Data inválida! Use o formato dd/mm/aaaa.\n")
            continue

def calcular_dias_restantes(data_):
    try:
        data_evento = datetime.datetime.strptime(data_.strip(), "%d/%m/%Y").date()
        data_hoje = datetime.date.today()
        diferenca = data_evento - data_hoje
        
        if diferenca.days > 0:
            return f"Faltam {diferenca.days} dias"
        elif diferenca.days == 0:
            return "É HOJE!"
        else:
            return f"Aconteceu há {abs(diferenca.days)} dias"
    except ValueError:
        return "Data inválida"

def adicionar_competicao(comp,data,local,cat):

    status_dias = calcular_dias_restantes(data)
    
    dados_competicao =(f"\n=========={comp}==========\n"
                       f"DATA: {data} \t{status_dias}\n"
                       f"LOCAL: {local}\n"
                       f"CATEGORIA: {cat}\n")
    
    arquivo = open("Competições.txt","a")
    arquivo.write(dados_competicao)
    arquivo.close()


arquivo = open("Sistema de Treinos.txt", "a")
arquivo.close()

while True:
   print("==========BEM VINDO AO HYROX PLANNER==========\n")
   opcao_escolhida = input("Você deseja:" 
    "\n[1] Adicionar\n"
      "[2] Visualizar treinos\n"
      "[3] Visualizar competições \n"
      "[4] Editar\n"
      "[5] Excluir\n"
      "[6] Adicionar competição \n"
      "[7] Parar"
      "\nRESPOSTA: ")

   clear()

   if opcao_escolhida == "1":
    
        conteudo = abrir_leitura()

        nome_treino = nomeDOtreino(conteudo)

        tipo = tipoDEtreino()

        data_treino = validar_data()

        duracao_treino = input("Digite o tempo de duração: ")
        clear()

        intensidade_final = intensidadeDEtreino()
            
        clear()
        
        treino = open("Sistema de Treinos.txt", "a")
        treino.write("Dados do Treino:" 
                        "\nNOME DO TREINO: " + nome_treino.upper().strip() + 
                        "\nTIPO DE TREINO: " + tipo + 
                        "\nDATA DO TREINO: " + data_treino + 
                        "\nDURAÇÃO DO TREINO: " + duracao_treino +
                        "\nINTENSIDADE DO TREINO: " + intensidade_final 
                        + "\n\n")
        clear()
        print("Treino Adicionado com Sucesso! \n\n")
        treino = open("Sistema de Treinos.txt", "r")
        treino.close()


   elif opcao_escolhida == "2":
        clear()
        treino = open("Sistema de Treinos.txt", "r")
        print(treino.read())
        treino.close()
        if not pergunta():
            break

    elif opcao_escolhida == "3":
            clear()
            print("==========COMPETIÇÕES==========")
    
            try:
                arquivo_comp = open("Competições.txt","r")
                conteudo_comp = arquivo_comp.read()
                arquivo_comp.close()
    
                if conteudo_comp.strip() =="":
                    print("Nenhuma competição cadastrada")
                else:
                    print(conteudo_comp)
    
            except FileNotFoundError:
                print("Nenhuma competição cadastrada ainda.")
                      
            while True:
                resposta = input("\nVocê quer continuar? s/n \nRESPOSTA: ").lower().strip()
                
                if resposta == "s":
                    clear()
                    break
                elif resposta == "n":
                    print("Programa Finalizado!")
                    exit()
                else:
                    print("RESPOSTA INVÁLIDA! Digite apenas 's' para sim ou 'n' para não.")
                    
   elif opcao_escolhida == "4":
        conteudo = abrir_leitura()
        treinos = conteudo.split("\n\n")

        while True:
            try:
                treino_antigo = input("Digite qual treino deseja editar: ")
            except:    
                if f"NOME DO TREINO: {treino_antigo.upper()}" not in conteudo:
                    print("Treino Inexistente!!\n\n")
                    continue
            else:
                clear()
                break
            
        treino_novo = nomeDOtreino(conteudo)

        tipo = tipoDEtreino()

        data_nova = validar_data()
        clear()

        duracao_nova = input("Digite o novo tempo de duração: ")
        clear()

        intensidade_final = intensidadeDEtreino()

        dados_novos = ("Dados do Treino: "
                       "\nNOME DO TREINO: " + treino_novo.upper().strip() + 
                       "\nTIPO DE TREINO: " + tipo +
                       "\nDATA DO TREINO: " + data_nova + 
                       "\nDURAÇÃO DO TREINO: " + duracao_nova + 
                       "\nINTENSIDADE DO TREINO: " + intensidade_final)

        for i in range(len(treinos)):
            if "NOME DO TREINO: " + treino_antigo.upper().strip() in treinos[i]:
                treinos[i] = dados_novos

        novo_conteudo = "\n\n".join(treinos)

        treino = open("Sistema de Treinos.txt", "w")
        treino.write(novo_conteudo)
        treino.close()
        clear()
        print("Treino editado com Sucesso!")

        if not pergunta():
            break


   elif opcao_escolhida == "5":
        conteudo = abrir_leitura()
        treinos = conteudo.split("\n\n")
        
        while True: 
            try:
                treino_excluir = input("Digite o treino que deseja excluir: ")
            except:  
                if f"NOME DO TREINO: " + treino_excluir.upper().strip() not in conteudo:
                    clear()
                    print("Treino inexistente!\n")
                    continue
            else:
                clear()
                break

        conjunto_fica = []
        
        for i in range(len(treinos)):
            if "NOME DO TREINO: " + treino_excluir.upper().strip() in treinos[i]:
                continue
            else:
                conjunto_fica.append(treinos[i])
                
        conjunto_fica = "\n\n".join(conjunto_fica)
        
        treino = open("Sistema de Treinos.txt", "w")
        treino.write(conjunto_fica)
        treino.close()
        print("Treino Excluído Com Sucesso!\n\n")

    elif opcao_escolhida == "6":

        nome_comp = input("Digite o nome da competição:")
        while True:
            data_comp = input("Digite a data da competição (DD/MM/AAAA): ")
            try:

                datetime.datetime.strptime(data_comp.strip(), "%d/%m/%Y").date()
                break

            except ValueError:
                print("Data inválida ou fora do padrão (DD/MM/AAAA). Tente novamente!\n")

        local_comp = input("Digite o local da competição:")
        cat_comp = input("Digite a categoria da competição:")

        adicionar_competicao(nome_comp,data_comp,local_comp,cat_comp)

        print("Competição adicionada com sucesso!\n\n")


    elif opcao_escolhida == "7":
        print("Programa Finalizado!")
        break


    else:
        print("Opção inválida!")
        if not pergunta():
            break

