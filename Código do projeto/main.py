import os 
import platform
#o platform é para que o computador reconheça o sistema operacional usado.
from groq import Groq

arquivo = open("Sistema de Treinos.txt", "a")
arquivo.close()
#para garantir que o arquivo sempre exista

def clear():
    OS = platform.system()
    if OS == "Darwin": #Darwin é o nome de dispositivos apple
        os.system("clear")
    else:
        os.system("cls")

clear()

def abrir_leitura(): #sempre que precisar ser aberto pra ler
    treino = open("Sistema de Treinos.txt", "r")
    conteudo = treino.read()
    treino.close()

    return conteudo

def pergunta(): #a pergunta de continuação do sistema
    while True:
        resposta = input("Você quer continuar? s/n \nRESPOSTA: ").lower()
        #devolver valores booleanos para identificar a resposta
        if resposta == "s":
            clear()
            return True

        elif resposta == "n":
            return False
        else: 
            print("RESPOSTA INVÁLIDA!") 

def nomeDOtreino(conteudo): #Adição de nome do TREINO
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

def tipoDEtreino(): #tipo do treino
    while True:
        try:
            tipo_treino = int(input("[1] CORRIDA / [2] FORÇA / [3] SIMULADO HYROX \n\nDigite o tipo de treino entre os disponíveis: " ))
            
            if tipo_treino == 1:
                tipo = "CORRIDA"
                
            elif tipo_treino == 2:
                tipo = "FORÇA"
            
            elif tipo_treino == 3:
                tipo = "SIMULADO HYROX"

            else:
                clear()
                print("Digite apenas 1, 2 ou 3!\n")
                continue
            
        except (ValueError, TypeError): 
            clear()
            print("Resposta inválida!")
            continue
        else:
            break
    clear()
    return tipo

def intensidadeDEtreino(): #intensidade do treino
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
    return intensidade_final #devolve a intensidade em forma de STRING

def editarOnome(): #EDIÇÃO de treino
    while True:
        nome_treino = input(f"O nome atual é: {nome_antigo}" #pra dar o direito de escolha se quer permanecer o mesmo treino ou não
                            "\nPara permanecer com o mesmo nome clique ENTER" 
                            "\n\nDigite o nome do treino: ").upper()
       
        return nome_treino
        
def editarOtipo():
    while True:
        try:
            tipo_treino = input(f"O tipo atual é: {tipo_antigo}\n" #pra dar o direito de escolha se quer permanecer o mesmo treino ou não
                "Para permanecer com o mesmo tipo de treino clique ENTER\n\n"
                "[1] CORRIDA\n"
                "[2] FORÇA\n"
                "[3] SIMULADO HYROX\n\n"
                "Digite o tipo de treino: ")

            if tipo_treino == "":
                return ""
            
            elif tipo_treino == 1:
                return "CORRIDA"

            elif tipo_treino == 2:
                return "FORÇA"

            elif tipo_treino == 3:
                return "SIMULADO HYROX"
            
            else:
                clear()
                print("Digite apenas 1, 2 ou 3!\n")
                continue

        except ValueError:
            clear()
            print("Resposta inválida!\n")
            
def editarAintensidade():
    while True:
        try:
            intensidade = input(f"A intensidade atual é: {intensidade_antiga}\n"
                "Para permanecer com a mesma intensidade clique ENTER\n\n"
                "[1] LEVE\n"
                "[2] MODERADO\n"
                "[3] PESADO\n\n"
                "Digite a intensidade: ")
            
            if intensidade == "": #se estiver em branco é porque foi apertado ENTER e continua o antigo
                return ""

            elif intensidade == 1:
                return "Treino Leve"

            elif intensidade == 2:
                return "Treino Moderado"

            elif intensidade == 3:
                return "Treino Pesado"

            else:
                clear()
                print("Digite apenas 1, 2 ou 3!\n")
                continue

        except ValueError:
            clear()
            print("Resposta inválida!\n")

def validar_data():
    from datetime import datetime
    while True:
        try:
            data = input("Digite a data do treino (dd/mm/aaaa): ")
            data_formatada = datetime.strptime(data, "%d/%m/%Y") #para que so aceite o formato de data
            clear()
            return data
                
        except ValueError:
            clear()
            print("Data inválida! Use o formato dd/mm/aaaa.\n")
            continue

def controledesempenho(nomedotreino):

    desemp = {}
    try:
        with open("Controle_de_Desempenho.txt", "r") as file:
            conteudo = file.read()
            desempenhos = (conteudo).split("\n---\n")
    except:
        file = open("Controle_de_Desempenho.txt", "x")
        desempenhos = []
        file.close()

    achou = False #verifica se o treino existe no CDD
    for i in range(len(desempenhos)):
        if nomedotreino + "\n" in desempenhos[i]:
            esse_desempenho = desempenhos[i]
            index = i
            achou = True
            break
    
    if achou: # se existe, colocar no dicionário pq é ela que vai ser editada
        linhas = esse_desempenho.split("\n")
        
        i = 1
        while i <= len(linhas)-4:
            desemp[linhas[i]] = [linhas[i+1].split("\t")[3:-1],
                                linhas[i+2].split("\t")[2:-1],
                                linhas[i+3].split("\t")[3:-1], # 2 e 1 por causa do numero de \t (virou 3 e 2 pq eu coloquei um tab a mais)
                                linhas[i+4].split("\t")[2:-1]]
            i += 5
        
    else: # se n existe, coloca uma sring vazia no desempenhos pra editar ela
        desempenhos.append("")
        index = len(desempenhos)-1
        # nn prescisa declarar o dicionario aqui pq ele ja lida com isso em add()

    # ====================== ADICIONAR NOVA LEITURA / CRIAR EXERCICIO =============

    def add(exercicio):

        if exercicio not in desemp.keys():
            desemp[exercicio] = [[],[],[],[]] #se o exercicio não existir ainda, criar uma matriz pra ele

        tempo = input("Insira o tempo: ")
        dist = input("Insira a distância: ")
        carga = input("Insira a carga: ")
        rep = input("Insira a quantidade de repetições: ")

        desemp[exercicio][0].append(tempo)
        desemp[exercicio][1].append(dist)
        desemp[exercicio][2].append(carga)
        desemp[exercicio][3].append(rep)

        print(f"Exercício {exercicio} updated!\n")

    # ====================== SALVAR MATRIZ =========================

    def salvarmatriz():
        if desemp.keys() == []: #só vai acontecer se o treino não existia antes
            return "oxi! fez nada... vou escrever o que? tu é doido"
        
        dados = nomedotreino
        
        for exercicio in desemp.keys():
            dados += "\n" + exercicio.upper()

            dados += ("\n\tTempos:\t\t")
            for d in desemp[exercicio][0]: #⚠️coloquei um tab a mais
                dados += (d + "\t")

            dados += ("\n\tDistâncias:\t")
            for d in desemp[exercicio][1]:
                dados += (d + "\t")

            dados += ("\n\tCargas:\t\t")
            for d in desemp[exercicio][2]:
                dados += (d + "\t")

            dados += ("\n\tRepetições:\t")
            for d in desemp[exercicio][3]:
                dados += (d + "\t")
        
        desempenhos[index] = dados
        conteudo = "\n---\n".join(desempenhos)


        file = open("Controle_de_Desempenho.txt", "w")
        file.write(conteudo)
        file.close()
        
    # ====================== LOOP PRINCIPAL =========================

    print("EXERCICIOS e Controle de Desempenho\n")
    opcoes = ["SLED", "TRENÓ",
              "WALL", "BALL", "BOLA",
              "SKI",
              "BURPEE", "SALTO", "BROAD",
              "ROW", "REMO",
              "FARMER", "CARRY", "MALAS", "CARREGAMENTO",
              "LUNGE", "PASSADA", "AVANÇO", "BAG",
              "RUN", "ESTEIRA", "TIRO"
             ]

    cmd = "S"
    while True:
        if cmd == "S":
            clear()
            print("Opções de exercício:", *opcoes, sep="\n- ")
            nome = input("\nDigite o nome do exercício que deseja adicionar/atualizar: ").upper()
            
            # ======= essa parte verifica se o exercicio sendo adicionado existe na parte de ferreira
            denovo = "S"
            valido = True
            while (nome not in opcoes) and (denovo == "S"):
                valido = False
                denovo = input(f"Exercicio \"{nome}\" não reconhecido, deseja tentar novamente? (S/N) ")
                if denovo == "N":
                    break
                elif denovo == "S":
                    continue #continue é o comando que volta pro inicio do loop ne?
                else:
                    print(f"Comando \"{denovo}\" não reconhecido, digite apenas \"S\" ou \"N\".")
                    continue
            # ========
            
            if valido:
                add(nome)
        elif cmd == "N":
            salvarmatriz()
            print("Encerrando programa...")
            clear()
            break
        else:
            print("comando não reconhecido.")
        
        cmd = input("Deseja continuar? (S/N) ").upper()

def calcular_dias_restantes(data_):
    import datetime
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

def acompanhamento_evolucao():
    from datetime import datetime

    # AQQQ LE O ARQUIVO
    try:
        conteudo = abrir_leitura()
    except FileNotFoundError:
        print("Nenhum dado encontrado.")
        return

    partes = conteudo.split("\n\n")

    # FREQUENCIA DE TREINO
    clear()
    print("========== FREQUÊNCIA DE TREINOS ==========\n")

    treinos_por_mes = {}
    total_treinos = 0

    for bloco in partes:
        if "Dados do Treino:" in bloco:
            for linha in bloco.split("\n"):
                if "DATA DO TRINO:" in linha or "DATA DO TREINO:" in linha:
                    try:
                        data_str = linha.replace("DATA DO TRINO:", "").replace("DATA DO TREINO:", "").strip()
                        data = datetime.strptime(data_str, "%d/%m/%Y")
                        chave = data.strftime("%m/%Y")
                        treinos_por_mes[chave] = treinos_por_mes.get(chave, 0) + 1
                        total_treinos += 1
                    except ValueError:
                        continue

    if total_treinos == 0:
        print("Nenhum treino cadastrado ainda.\n")
    else:
        print(f"Total de treinos realizados: {total_treinos}\n")
        print("Treinos por mês:")
        for mes in treinos_por_mes:
            qtd = treinos_por_mes[mes]
            barra = " " * qtd
            print(f"  {mes}: {barra} ({qtd})")
        print()

    # AQQ MOSTRA A EVOLUÇÃO DO EXERCICIO - LENDO DO CONTROLE DE DESEMPENHO
    print("========== EVOLUÇÃO DE EXERCÍCIOS ==========\n")
    try:
        file = open("Controle_de_Desempenho.txt", "r")
        cont_exerc = file.read()
        file.close()
    except FileNotFoundError:
        print("Nenhum histórico de desempenho encontrado.\n")
        return

    if not cont_exerc.strip():
        print("Nenhum exercício registrado ainda.\n")
        return

    blocos_treino = cont_exerc.split("\n---\n")
    exercicios_globais = {}

    for bloco in blocos_treino:
        linhas = bloco.strip().split("\n")
        if len(linhas) < 2:
            continue
        
        i = 1
        while i < len(linhas):
            nome_exerc = linhas[i].strip()
            if not nome_exerc or nome_exerc.startswith("Tempos:") or nome_exerc.startswith("Distâncias:") or nome_exerc.startswith("Cargas:") or nome_exerc.startswith("Repetições:"):
                i += 1
                continue

            try:
                tempos     = linhas[i+1].replace("Tempos:", "").split("\t")
                distancias = linhas[i+2].replace("Distâncias:", "").split("\t")
                cargas     = linhas[i+3].replace("Cargas:", "").split("\t")
                repeticoes = linhas[i+4].replace("Repetições:", "").split("\t")
                
                # Filtrar strings vazias geradas pelos tabs
                tempos = [t.strip() for t in tempos if t.strip()]
                distancias = [d.strip() for d in distancias if d.strip()]
                cargas = [c.strip() for c in cargas if c.strip()]
                repeticoes = [r.strip() for r in repeticoes if r.strip()]
            except IndexError:
                i += 1
                continue

            if nome_exerc not in exercicios_globais:
                exercicios_globais[nome_exerc] = {"tempos": [], "cargas": [], "distancias": [], "repeticoes": []}

            exercicios_globais[nome_exerc]["tempos"].extend(tempos)
            exercicios_globais[nome_exerc]["distancias"].extend(distancias)
            exercicios_globais[nome_exerc]["cargas"].extend(cargas)
            exercicios_globais[nome_exerc]["repeticoes"].extend(repeticoes)

            i += 5

    if not exercicios_globais:
        print("Nenhum exercício estruturado encontrado no histórico.\n")
        return

    for nome_ex in exercicios_globais:
        print(f"  {nome_ex}")

        metricas = [
            ("Tempo",       exercicios_globais[nome_ex]["tempos"],      True),
            ("Distância",   exercicios_globais[nome_ex]["distancias"],  False),
            ("Carga",       exercicios_globais[nome_ex]["cargas"],      False),
            ("Repetições",  exercicios_globais[nome_ex]["repeticoes"],  False)
        ]

        possui_dados = False
        for nome_metrica, lista, menor_e_melhor in metricas:
            valores = [v for v in lista if v.strip() != ""]

            if len(valores) < 2:
                continue
            
            possui_dados = True
            primeiro = valores[0]
            ultimo = valores[-1]

            try:
                v1 = float(primeiro.replace(",", "."))
                v2 = float(ultimo.replace(",", "."))

                if menor_e_melhor:
                    if v2 < v1:
                        simbolo = "↓ MELHORA"
                    elif v2 > v1:
                        simbolo = "↑ PIORA"
                    else:
                        simbolo = "→ ESTÁVEL"
                else:
                    if v2 > v1:
                        simbolo = "↑ MELHORA"
                    elif v2 < v1:
                        simbolo = "↓ PIORA"
                    else:
                        simbolo = "→ ESTÁVEL"

                print(f"    {nome_metrica}: {primeiro} → {ultimo}  [{simbolo}]")

            except ValueError:
                print(f"    {nome_metrica}: {primeiro} → {ultimo}")
                
        if not possui_dados:
            print("    Sem dados históricos suficientes para calcular evolução técnica.")
    print()

def sugerir_treinos_personalizados():
    clear()
    print("========== SUGESTÕES PERSONALIZADAS HYROX ==========\n")
    
    while True:
        try:
            nivel_op = int(input("[1] INICIANTE / [2] INTERMEDIÁRIO / [3] AVANÇADO\nDigite o seu nível atual: "))
            if nivel_op == 1:
                nivel = "iniciante"
                break
            elif nivel_op == 2:
                nivel = "intermediario"
                break
            elif nivel_op == 3:
                nivel = "avancado"
                break
            else:
                print("Opção inválida!")
        except ValueError:
            print("Por favor, digite um número válido.")

    clear()
    

    pontos_fracos = []
    try:
        file = open("Controle_de_Desempenho.txt", "r")
        conteudo = file.read().upper()
        file.close()
        
        if "SLED" in conteudo or "TRENÓ" in conteudo:
            pontos_fracos.append("Empurrão/Puxada de Trenó")
        if "WALL" in conteudo or "BALL" in conteudo or "BOLA" in conteudo:
            pontos_fracos.append("Lançamento de Bola na Parede")
        if "SKI" in conteudo:
            pontos_fracos.append("Simulador de Esqui (SkiErg)")
        if "BURPEE" in conteudo or "SALTO" in conteudo or "BROAD" in conteudo:
            pontos_fracos.append("Burpee com Salto em Distância")
        if "ROW" in conteudo or "REMO" in conteudo:
            pontos_fracos.append("Remo")
        if "FARMER" in conteudo or "CARRY" in conteudo or "MALAS" in conteudo or "CARREGAMENTO" in conteudo:
            pontos_fracos.append("Caminhada do Fazendeiro")
        if "LUNGE" in conteudo or "PASSADA" in conteudo or "AVANÇO" in conteudo or "BAG" in conteudo:
            pontos_fracos.append("Passada com Saco de Areia")
        if "RUN" in conteudo or "ESTEIRA" in conteudo or "TIRO" in conteudo:
            pontos_fracos.append("Resistência de Corrida")
            
    except FileNotFoundError:
        pass 

    print(f"--- PLANO DE ESTRATÉGIA GERADO (Nível: {nivel.upper()}) ---")
    
    if nivel == "iniciante":
        print("Divisão Semanal: 3 dias por semana (2x Corpo Todo focado em técnica + 1x Corrida de Recuperação).")
        print("Cargas Ideais:   Trabalhar com 60% a 70% do peso oficial do HYROX para focar na execução correta.")
        print("Treino Sugerido: Condicionamento de 30 minutos alternando corrida leve com agachamentos e flexões.")
    elif nivel == "intermediario":
        print("Divisão Semanal: 4 dias por semana (1x Força Pura, 2x Funcional Combinado, 1x Corrida Longa).")
        print("Cargas Ideais:   Trabalhar entre 85% e 100% do peso oficial da sua categoria para ganhar potência.")
        print("Treino Sugerido: Treino em blocos de minuto de 40 minutos (Alternando corrida, esqui e passadas com carga).")
    elif nivel == "avancado":
        print("Divisão Semanal: 5 dias por semana (2x Força/Potência, 2x Volume Simulado, 1x Velocidade/Intervalado).")
        print("Cargas Ideais:   Estratégia de Sobrecarga (Treinar com 110% a 120% do peso oficial em estímulos curtos).")
        print("Treino Sugerido: Simulado de Fadiga Acumulada (Corrida em ritmo de prova sem descanso entre as estações).")

    
    if pontos_fracos:
        print("\nEstratégias foca-gargalo (Baseado nos exercícios do seu histórico):")
        for pf in pontos_fracos:
            if "Trenó" in pf:
                print(" - Para o TRENÓ (SLED): Adicione treinos de força pura em membros inferiores (Pressione de pernas/Leg Press e Agachamento pesado).")
            if "Parede" in pf:
                print(" - Para o LANÇAMENTO DE BOLA (WALL BALLS): Treine a capacidade respiratória sob fadiga. Use uma bola 2kg mais pesada nos treinos.")
            if "Esqui" in pf:
                print(" - Para o SIMULADOR DE ESQUI (SKI): Melhore a extensão e flexão de quadril, usando o peso do corpo e não apenas a força dos braços.")
            if "Burpee" in pf:
                print(" - Para o BURPEE COM SALTO: Foque no ritmo constante e ritmado (pacing) e na flexibilidade de quadril para saltar mais rápido de forma eficiente.")
            if "Remo" in pf:
                print(" - Para o REMO: Treine a potência de tração e o controle do ritmo de remada, lembrando de empurrar o chão fortemente com as pernas.")
            if "Fazendeiro" in pf:
                print(" - Para a CAMINHADA DO FAZENDEIRO (FARMER'S CARRY): Fortaleça a pegada com sustentação de peso estática e treine a estabilização do abdômen e lombar.")
            if "Passada" in pf:
                print(" - Para a PASSADA COM SACO DE AREIA (LUNGES): Desenvolva força unilateral executando agachamento búlgaro e passadas para trás com halteres.")
            if "Run" in pf:
                print(" - Para a RESISTÊNCIA DE CORRIDA: Faça treinos intervalados de alta velocidade (tiros) e treine correr especificamente logo após exercícios pesados de perna.")
    else:
        print("\nDica: Conforme você cadastrar exercícios como 'Trenó', 'Esqui', 'Bola na Parede', 'Remo', 'Passada' ou 'Run' no Controle de Desempenho, dicas específicas aparecerão aqui!")

    print("\n====================================================")
    input("\nPressione ENTER para voltar ao menu principal...")

def dashboard():

    try:
        arquivo = open("Sistema de Treinos.txt", "r")
        conteudo = arquivo.read()
        arquivo.close()

        total_treinos = conteudo.count("NOME DO TREINO:")

    except FileNotFoundError:
        total_treinos = 0

    try:
        comp = open("Competições.txt", "r")
        conteudo_comp = comp.read()
        comp.close()

        total_comp = conteudo_comp.count("DATA:")

    except FileNotFoundError:
        total_comp = 0

    try:
        exerc = open("Controle_de_Desempenho.txt", "r")
        conteudo_exerc = exerc.read()
        exerc.close()

        total_exerc = conteudo_exerc.count("Cargas:")

    except FileNotFoundError:
        total_exerc = 0

    print("\t==========DASHBOARD==========\n")
    print(f"\tTreinos cadastrados: {total_treinos}")
    print(f"\tCompetições cadastradas: {total_comp}")
    print(f"\tExercícios cadastrados: {total_exerc}\n")
    
while True:
   print("==========BEM VINDO AO HYROX PLANNER==========\n")
   dashboard()
   opcao_escolhida = input("Você deseja:" 
    "\n[1] Adicionar\n"
        "[2] Visualizar treinos\n"
        "[3] Visualizar competições \n"
        "[4] Editar\n"
        "[5] Excluir\n"
        "[6] Controle de Desempenho\n"
        "[7] Adicionar competição \n"
        "[8] Acompanhar Evolução\n"
        "[9] Sugestões Personalizadas\n"
        "[10] 🤖 Falar com o Agente (Coach Inteligente)\n"
        "[11] Parar"
        "\nRESPOSTA: ")

   clear()

   if opcao_escolhida == "1":
    
        conteudo = abrir_leitura() #variavel com o conteudo do arquivo

        nome_treino = nomeDOtreino(conteudo)

        tipo = tipoDEtreino()

        data_treino = validar_data()

        duracao_treino = input("Digite o tempo de duração: ")
        clear()

        intensidade_final = intensidadeDEtreino()
            
        clear()
        
        treino = open("Sistema de Treinos.txt", "r")
        conteudo = treino.read()
        treino.close()

        treino = open("Sistema de Treinos.txt", "w")

        dados_novos = ("Dados do Treino:" 
                        "\nNOME DO TREINO: " + nome_treino.upper().strip() + 
                        "\nTIPO DE TREINO: " + tipo + 
                        "\nDATA DO TREINO: " + data_treino + 
                        "\nDURAÇÃO DO TREINO: " + duracao_treino +
                        "\nINTENSIDADE DO TREINO: " + intensidade_final)
        
        treinos = conteudo.split("\n\n") # quebra o texto cru do arquivo em uma lista
        if "EXERCICIOS:\n" in treinos[-1]:
            treinos.insert(-1, dados_novos) # coloca os dados novos dentro da lista antes da parte de controle de desempenho
        else:
            treinos.append(dados_novos)
        treino.write("\n\n".join(treinos)) # da .join na lista e sobreescreve o arquivo inteiro

        # isso faz com que o controle de desempenho sempre fique na parte de baixo do arquivo (tem q ser assim pra o meu codigo funcionar)

        clear()
        print("Treino Adicionado com Sucesso! \n\n")
        treino = open("Sistema de Treinos.txt", "r")
        treino.close()


   elif opcao_escolhida == "2":
        clear()
        treino = open("Sistema de Treinos.txt", "r")
        print(treino.read())
        treino.close()
        try:
            with open("Controle_de_Desempenho.txt", "r") as cdd:
                conteudo = cdd.read()
                if len(conteudo) > 10: #usando len() ao invez de == "" or == "\n" pra evitar variações desses (ex. "\n\n\n")
                    print("\n===Controle de Desempenhos===")
                    print(conteudo)
        except:
            pass
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
                  
        if not pergunta():
            break


   elif opcao_escolhida == "4":
        conteudo = abrir_leitura()
        treinos = conteudo.split("\n\n") #separa tudo do rquivo em listas a partir dos \n duplo

        treino_encontrado = None

        treino_antigo = input("Digite qual treino deseja editar: ").upper().strip() #UPPER deixa tutdo em maiusculo e STRIP tira os espaços

        for treino in treinos: #procura o treino no arquivo
            if f"NOME DO TREINO: {treino_antigo}\n" in treino:
                treino_encontrado = treino
                break

        if treino_encontrado is None:
            print("Treino inexistente!")
            continue


        linhas = treino_encontrado.split("\n")# separa a lista encontrada em outras pequenas listas por linhas

        #põe os valores antigos em variaveis caso seja necessário usar
        nome_antigo = linhas[1].replace("NOME DO TREINO: ", "")
        tipo_antigo = linhas[2].replace("TIPO DE TREINO: ", "")
        data_antiga = linhas[3].replace("DATA DO TREINO: ", "")
        duracao_antiga = linhas[4].replace("DURAÇÃO DO TREINO: ", "")
        intensidade_antiga = linhas[5].replace("INTENSIDADE DO TREINO: ", "")

        clear()
        novo_nome = editarOnome()
        # se apertar ENTER continua o mesmo
        if novo_nome == "":
            novo_nome = nome_antigo
        else:

        # ========================================
        # Essa parte do código procura o treino antigo no controle de desempenhos

            try:
                file = open("Controle_de_Desempenho.txt", "r")
                conteudocdd = file.read()
                file.close()

                desempenhos = conteudocdd.split("\n---\n")

                achou = False
                for o in range(len(desempenhos)):
                    if treino_antigo.lower() + "\n" in desempenhos[o]:
                        esse_desempenho = desempenhos[o] #nesse caso, como eu só presciso deletar, não tem motivo pra dividir esse desempenho em linhas
                        index = o
                        achou = True
                        break
                
                if achou:
                    linhas = esse_desempenho.split("\n")
                    linhas[0] = novo_nome.lower()
                    desempenhos[o] = "\n".join(linhas)
                
                    conteudocdd = "\n---\n".join(desempenhos)
                    file = open("Controle_de_Desempenho.txt", "w")
                    file.write(conteudocdd)
                    file.close()

            except: #controle de desempenho não existe
                pass

        # ========================================


        clear()
        novo_tipo = editarOtipo()
         # se apertar ENTER continua o mesmo
        if novo_tipo == "":
            novo_tipo = tipo_antigo


        clear()
        from datetime import datetime

        while True:
            nova_data = input(
                f"Data atual: {data_antiga}\n"
                "Nova data (DD/MM/AAAA) (ENTER para manter): "
            ).strip()
             # se apertar ENTER continua o mesmo
            if nova_data == "":
                nova_data = data_antiga
                break

            try:
                datetime.strptime(nova_data, "%d/%m/%Y") #so permite datas válidas e existentes
                break
            except ValueError:
                clear()
                print("Data inválida! Use o formato DD/MM/AAAA.\n")


        clear()
        nova_duracao = input(
            f"Duração atual: {duracao_antiga}\nDigite ENTER para manter\n"
            "Nova duração: ").strip()

         # se apertar ENTER continua o mesmo
        if nova_duracao == "":
            nova_duracao = duracao_antiga


        clear()
        nova_intensidade = editarAintensidade()

         # se apertar ENTER continua o mesmo
        if nova_intensidade == "":
            nova_intensidade = intensidade_antiga


        dados_novos = (
            "Dados do Treino:"
            "\nNOME DO TREINO: " + novo_nome.upper()
            + "\nTIPO DE TREINO: " + novo_tipo
            + "\nDATA DO TREINO: " + nova_data
            + "\nDURAÇÃO DO TREINO: " + nova_duracao
            + "\nINTENSIDADE DO TREINO: " + nova_intensidade)

        for i in range(len(treinos)):
            if f"NOME DO TREINO: {treino_antigo}" in treinos[i]:
                treinos[i] = dados_novos

        #retransforma a lista em string
        novo_conteudo = "\n\n".join(treinos)

        with open("Sistema de Treinos.txt", "w") as treino:
            treino.write(novo_conteudo)

        clear()
        print("Treino editado com sucesso!")


   elif opcao_escolhida == "5":
        conteudo = abrir_leitura()
        treinos = conteudo.split("\n\n") #transforma em listas
        
        while True: 
            treino_excluir = input("Digite o treino que deseja excluir: ")
            if f"NOME DO TREINO: " + treino_excluir.upper().strip() + "\n" not in conteudo: #procura o treino nas listas
                    clear()
                    print("Treino inexistente!\n")
                    continue
            else:
                clear()
                break
            
        # ========================================
        # Essa parte do código procura o treino antigo no controle de desempenhos

        try:
            file = open("Controle_de_Desempenho.txt", "r")
            conteudocdd = file.read()

            desempenhos = conteudocdd.split("\n---\n")

            achou = False
            for o in range(len(desempenhos)):
                if treino_excluir.lower() + "\n" in desempenhos[o]:
                    index = o
                    achou = True
                    break
            
            if achou:
                
                desempenhos.pop(o) # remove esse desempenho
                
                conteudocdd = "\n---\n".join(desempenhos)
                file = open("Controle_de_Desempenho.txt", "w")
                file.write(conteudocdd)
                file.close()

        except:
            pass

        # ========================================

        conjunto_fica = [] #armazena todo o resto que nao foi excluido
        
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
        treinoCD = input("Digite um treino para adicionar um desempenho: ")
        conteudo = abrir_leitura()

        if "NOME DO TREINO: " + treinoCD.upper() in conteudo:
            controledesempenho(treinoCD)
        else:
            clear()
            print("Treino inexistente, adicione ele pelo CRUDE primeiro!")
            if not pergunta():
                break
        

   elif opcao_escolhida == "7":
        import datetime
        nome_comp = input("Digite o nome da competição: ")
        while True:
            data_comp = input("Digite a data da competição (DD/MM/AAAA): ")
            try:
                datetime.datetime.strptime(data_comp.strip(), "%d/%m/%Y").date()
                break

            except ValueError:
                print("Data inválida ou fora do padrão (DD/MM/AAAA). Tente novamente!\n")

        local_comp = input("Digite o local da competição: 3")
        cat_comp = input("Digite a categoria da competição: ")

        adicionar_competicao(nome_comp,data_comp,local_comp,cat_comp)
        clear()
        print("Competição adicionada com sucesso!\n\n")
        if not pergunta():
            break
    
   elif opcao_escolhida == "8":
       # Acompanhar Evolução integrado com Controle de Desempenho
       acompanhamento_evolucao()
       input("Aperte ENTER para prosseguir! ")
       clear()

    
   elif opcao_escolhida == "9":  
        sugerir_treinos_personalizados()
        clear()

    
   elif opcao_escolhida == "10":
        clear()
        print("==========🤖 Falar com o Agente (Coach Inteligente)==========")
        
        try:
            arquivo_treinos = open("Sistema de Treinos.txt", "r", encoding="utf-8")
            conteudo_treinos = arquivo_treinos.read()
            arquivo_treinos.close()
        except FileNotFoundError:
            conteudo_treinos = "Nenhum treino cadastrado."

        try:
            arquivo_comp = open("Competições.txt", "r", encoding="utf-8")
            conteudo_competicoes = arquivo_comp.read()
            arquivo_comp.close()
        except FileNotFoundError:
            conteudo_competicoes = "Nenhuma competição cadastrada."

        pergunta_usuario = input("\nO que você quer perguntar ao Coach? \nRESPOSTA: ")
        print("\nProcessando a sua pergunta com Inteligência Artificial... Por favor, aguarde.")
        
        try:
            client = Groq(api_key="")
            
            prompt_sistema = f"""
Você é um treinador especialista em HYROX, corrida híbrida,
endurance, preparação competitiva e performance funcional.

Você atua como coach inteligente dentro de um sistema esportivo.

Seu objetivo é:
- analisar os treinos do atleta;
- analisar calendário de competições;
- identificar padrões de intensidade;
- detectar excesso ou falta de volume;
- sugerir melhorias;
- gerar novos treinos;
- orientar recuperação;
- otimizar performance para HYROX;
- prevenir lesões;
- adaptar treinos para objetivos específicos;
- fornecer feedback personalizado;
- responder dúvidas sobre treinamento e competições;
- alertar sobre riscos de overtraining, fadiga acumulada e proximidade de competições;
- considerar o histórico do atleta para sugestões personalizadas.

Você SEMPRE deve responder:
- em português;
- de forma objetiva;
- como um treinador profissional;
- usando linguagem clara;
- com base em evidências de treinamento esportivo;
- baseado SOMENTE nos dados fornecidos.

==================================================
DADOS DOS TREINOS
==================================================

{conteudo_treinos}

==================================================
DADOS DAS COMPETIÇÕES
==================================================

{conteudo_competicoes}

==================================================
REGRAS IMPORTANTES
==================================================

1. Analise:
- volume semanal;
- intensidade;
- frequência dos grupos musculares;
- equilíbrio entre corrida e força;
- recuperação;
- progressão de carga;
- proximidade das competições;
- fadiga acumulada;
- consistência dos treinos;
- variação de estímulos;
- padrões de treino ao longo do tempo;
- relação entre treinos recentes e competições futuras.

2. Você deve identificar:
- risco de overtraining;
- treinos leves demais;
- treinos pesados demais;
- excesso de intensidade;
- baixa recuperação;
- risco pré-competição;
- excesso de impacto;
- falta de progressão;
- risco de lesão;
- padrões de treino que indicam falta de periodização ou desequilíbrio entre corrida e força;
- padrões de treino que indicam falta de variação ou excesso de monotonia.

3. Sempre gere:
- análise geral;
- alertas;
- sugestões;
- próximos passos.

4. Caso o usuário peça um NOVO TREINO:
- adapte ao histórico do atleta;
- considere competições próximas;
- considere fadiga acumulada;
- considere recuperação;
- considere objetivo esportivo;
- considere intensidade recente.

5. Caso os dados sejam insuficientes:
- informe claramente;
- faça sugestões conservadoras;
- nunca invente informações;
- sempre peça mais detalhes sobre treinos, sensações, recuperação, sono, alimentação e competições para análises mais precisas.

6. Você é especialista em:
- HYROX;
- corrida híbrida;
- treino funcional;
- endurance;
- strength & conditioning;
- preparação competitiva;
- periodização;
- recuperação esportiva;
- VO2;
- zonas cardíacas.
"""
            
            prompt_usuario = f"""
            Dados do usuário:
            === TREINOS REALIZADOS ===
            {conteudo_treinos}
            
            === COMPETIÇÕES AGENDADAS ===
            {conteudo_competicoes}
            
            Pergunta: {pergunta_usuario}
            """
            
            resposta = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": prompt_sistema},
                    {"role": "user", "content": prompt_usuario}
                ],
                temperature=0.7 
            )
            
            print("\n================ RESPOSTA DO AGENTE ================\n")
            print(resposta.choices[0].message.content)
            print("====================================================\n")
            
            input("Pressione ENTER para voltar ao menu...")
            clear()
            
        except Exception as e:
            print(f"\n❌ Erro ao ligar ao Coach Inteligente: {e}")
            print("Possivel erro de conexão ou chave de API inválida. Tente novamente mais tarde.")
            input("\nPressione ENTER para voltar ao menu...")
            clear()

    
   elif opcao_escolhida == "11":#
        print("Programa Finalizado!")
        break


   else:
        print("Opção inválida!")
        if not pergunta():
            break
