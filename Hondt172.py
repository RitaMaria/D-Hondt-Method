#####################################
###########Projeto de Programação 1
#### GRUPO 172
#### Ana Francisca Seixas Fernandes  fc54785
#### Irene Cristina de Oliveira Gaspar fc54818
#### Rita Maria Olivera Rodrigues fc54859
#####################################


################### Etapa 0 ###################

def hondt(numeroMandatos, votacao):
    """ Aplica o método de Hondt

    Requires: numeroMandatos int > 0, votacao lista de tuplos
    (partido, nvotos) com nvotos >= 0
    Ensures: devolve uma lista de tuplos (partido, mandatos),
    com a mesma ordem da lista votacao
    """
    partidos = [p for (p,v) in votacao]
    listavotacao = [[a,b] for (a,b) in votacao]
    listacompleta = []
    for [p,v] in listavotacao:
        for mandatos in range(1, numeroMandatos+1):
            listacompleta.append([p, v/mandatos])
    listaordenada = sorted(listacompleta, key = lambda t:t[1])
    listaordenada.reverse()
    n = 1
    while n < len (listaordenada):
        if listaordenada[n-1][1] == listaordenada[n][1]:
            votacaoordenada = sorted(votacao, key = lambda t:t[1])
            partidosmaisvotos = [p for (p,v) in votacaoordenada]
            while partidosmaisvotos.index(listaordenada[n-1][0]) > partidosmaisvotos.index(listaordenada[n][0]):
                listaordenada.insert(n-1,listaordenada[n])
                listaordenada.pop(n+1)
        n += 1
    listavotosmaiores = listaordenada[0:numeroMandatos]
    listapartidosfinal = [i[0] for i in listavotosmaiores]
    listafinal = []
    for partido in partidos:
        listafinal.append((partido, listapartidosfinal.count(partido)))
    return listafinal

def importar_votacoes(nomeFicheiro):
    """ Importa a tabela com as votações detalhadas por distrito

    Requires: nomeFicheiro é uma string representando um ficheiro de texto
    Ensures: devolve uma tabela (uma lista de listas) com as votações lidas do
    ficheiro; nesta tabela, os elementos da primeira linha são strings, e em cada
    uma das restantes linhas, o primeiro elemento é string e os restantes são int.
    """

    listavotacoes = []
    with open(nomeFicheiro,"r",encoding = "utf-8") as file:
        conteudo = file.readlines()
    for line in conteudo:
        votacoes = line.strip("\n").rstrip().split(" ")
        listavotacoes.append(votacoes)
    n = 1
    while n < len(listavotacoes):
        for i in range(1,len(listavotacoes[n])):
            listavotacoes[n][i] = int(listavotacoes[n][i])
        n += 1
    return listavotacoes


################### Etapa 1 ###################
def mandatos_por_circulo(totalDeputados, votacoes):
    """ Calcula o número de mandatos associado a cada círculo

    Requires:
      totalDeputados é o número de mandatos a atribuir; é um int >0;
      votacoes é uma tabela no formato conforme devolvido por importar_votacoes
    Ensures: devolve uma lista de tuplos (distrito, nMandatos) onde distrito
             é string e nMandatos é int
    """
    listavotos = []
    for x in votacoes:
        listavotos.append((x[0],x[1]))
    listavotos.pop(0)
    return hondt(totalDeputados,listavotos)

def assembleia(total_deputados, votacoes):
    """Calcula a distribuição final da assembleia

    Requires: total_deputados é o número de deputados a eleger, 
              votacoes é uma tabela no formato conforme devolvido por
              importar_votacoes
    Ensures: Uma lista de tuplos (nome de partido, numDeputados), 
             ordenada pela mesma ordem do ficheiro original
    """
    mandatosporcirculo = mandatos_por_circulo(total_deputados,votacoes)
    listavotospartidos = []
    listapartidos = votacoes[0][6:]
    for x in range(1,len(votacoes)):
        listavotospartidos.append(list(zip(listapartidos,votacoes[x][6:])))
    mandatos = []
    for x in mandatosporcirculo:
        mandatos.append(x[1])
    mandatosvotos = list(zip(mandatos,listavotospartidos))
    listamandatos = []
    for x in mandatosvotos:
        listamandatos.append(hondt(x[0],x[1]))
    numerodeputados = []
    n = 0
    while n < len(listapartidos):
        soma = sum(x[n][1] for x in listamandatos)
        numerodeputados.append(soma)
        n += 1
    listaassembleia = list(zip(listapartidos,numerodeputados))
    return listaassembleia

################### Etapa 2 ###################
#SUGESTÃO: crie duas variáveis globais numeroMandatos e votacoes onde guarda
#o numero de mandatos da assembleia e a lista com o formato construído em
#importar_votacoes

def determinaNumMandatos(n):
    """Define o número de mandatos da assembleia

    Requires: n int > 0
    Ensures: O número de mandatos a considerar é n
    """
    return n

def quantosMandatos():
    """Mostra o número de mandatos da assembleia

    Requires:
    Ensures: imprime o número de mandatos da assembleia
    """
    return print ("A assembleia tem ", numeroMandatos , "mandatos")

def repor(nomeFicheiro):
    """Lê e carrega em memória o ficheiro com o nome dado

    Requires: nomeFicheiro é uma string com um nome de ficheiro válido
    Ensures: devolve uma tabela (uma lista de listas) com as votações lidas do
    ficheiro; nesta tabela, os elementos da primeira linha são strings, e em cada
    uma das restantes linhas, o primeiro elemento é string e os restantes são int.
    """
    global votacoes
    votacoes = importar_votacoes(nomeFicheiro)
    return votacoes

def listarDistritos(votacoes):
    """Mostra a lista de distritos carregados em memória listados de 0 em diante

    Requires: votacoes é uma tabela construída com o formato igual ao construído 
              em importar_votacoes
    Ensures: imprime no écran a lista de distritos com os respetivos números
    """
    for x in range(0,len(votacoes)-1):
        print(str(x)+":",votacoes[x+1][0])
        
def mostrarVotacao(numDistrito, votacoes):
    """Mostra a votação dos partidos no distrito com o número dado

    Requires: - numDistrito é um número de distrito válido
              - votacoes é uma tabela no formato conforme devolvido por
              importar_votacoes
    Ensures: imprime no écran a votação nos partidos no distrito referido
    """
    print(numDistrito,votacoes[numDistrito+1][0])
    for j in range(len(votacoes[0][6:])):
        print(votacoes[0][j+6]+",",votacoes[numDistrito+1][j+6])
        
def mostrarNumMandatos(numMandatosAssembleia, numDistrito, votacoes):
    """Mostra o número de mandatos que o distrito com o número dado elege

    Requires: - numMandatosAssembleia é int > 0
              - numDistrito é um número de distrito válido
              - votacoes é uma tabela no formato conforme devolvido por
              importar_votacoes
    Ensures: devolve o número de mandatos que o distrito elege
    """
    mandatosporcirculo = mandatos_por_circulo(numMandatosAssembleia,votacoes)
    print(mandatosporcirculo[numDistrito][0]+":",mandatosporcirculo[numDistrito][1])
    
def agruparDistritos(listaNumsDistritos, votacoes):
    """Agrupa os distritos dados num só

    Requires: - todos os elementos de listaNumsDistritos são números de
                distritos válidos
              - votacoes é uma lista com o formato construído em
              importar_votacoes
    Ensures: altera a tabela votacoes, agrupando os distritos de
             listaNumsDistritos, com os seus nomes concatenados e separados
             por '+' e seguidos dos números acumulados de inscritos, votantes,
             brancos, nulos e válidos e depois os votos acumulados dos partidos.
             O novo distrito deve ficar na posição onde estava originalmente
             o primeiro dos distritos a agrupar
    """
    votacoes.pop(0)
    listaconjunta = []
    for x in listaNumsDistritos:
        listaconjunta.append(votacoes[x])
    listamerge = list(zip(*listaconjunta))
    listamerge2 = listamerge.copy()
    listamerge2.pop(0)
    listasoma = [sum(tuple) for tuple in listamerge2]
    tuplo = listamerge[0]
    listasoma.insert(0,"+".join(tuplo))
    minimo = min(listaNumsDistritos)
    votacoes.insert(minimo,listasoma)
    n = 0
    while n < len(listaNumsDistritos):
        votacoes.pop(minimo+1)
        n += 1
        
def mostraMandatos(numMandatosAssembleia, numDistrito, votacoes):
    """Mostra o nome do distrito e a atribuição dos mandatos aos partidos nesse
       distrito por ordem decrescente do número de eleitos

    Requires: - numMandatosAssembleia é int > 0
              - numDistrito eh um número de distrito válido
              - votacoes é uma tabela no formato conforme devolvido por
              importar_votacoes
    Ensures: mostra a distribuição dos mandatos atribuídos no distrito referido
    """
    mandatosporcirculo = mandatos_por_circulo(numMandatosAssembleia,votacoes)
    listavotospartidos = []
    listapartidos = votacoes[0][6:]
    for x in range(1,len(votacoes)):
        listavotospartidos.append(list(zip(listapartidos,votacoes[x][6:])))
    mandatos = []
    for x in mandatosporcirculo:
        mandatos.append(x[1])
    mandatosvotos = list(zip(mandatos,listavotospartidos))
    listamandatos = []
    for x in mandatosvotos:
        listamandatos.append(hondt(x[0],x[1]))
    print(votacoes[numDistrito+1][0])
    mostramandatos = []
    for x in listamandatos[numDistrito]:
        if x[1] != 0:
            mostramandatos.append(x)
    mostramandatos = sorted(mostramandatos, key = lambda t:t[1])
    mostramandatos.reverse()
    for x in mostramandatos:
        print(x[0],x[1])
        
def mostraAssembleia(numMandatosAssembleia, votacoes):
    """Mostra a composição final da assembleia, ordenada
    por ordem decrescente do número de eleitos

    Requires: - numMandatosAssembleia é int > 0
              - votacoes é uma tabela no formato conforme devolvido por
              importar_votacoes
    Ensures: mostra a composição final da assembleia, ordenada por ordem
             Decrescente do número de eleitos (partidos com 1 ou mais mandatos)
    """
    listaassembleia = assembleia(numMandatosAssembleia, votacoes)
    listaassembleia = sorted(listaassembleia, key = lambda t:t[1])
    listaassembleia.reverse()
    listaassembleiafinal = []
    for x in listaassembleia:
        if x[1] != 0:
            listaassembleiafinal.append(x)
    for x in listaassembleiafinal:
        print(x[0],x[1])
        
def graficoTarte(numMandatosAssembleia, votacoes):
    """Desenha e mostra um gráfico de tarte com a composição da assembleia

    Requires: - numMandatosAssembleia é int > 0
              - votacoes é uma tabela no formato conforme devolvido por
              importar_votacoes
    Ensures: mostra o gráfico de tarde com a composição da assembleia
    """
    constituicaoassembleia1 = assembleia(numMandatosAssembleia,votacoes)
    constituicaoassembleia2 = []
    for x in constituicaoassembleia1:
        if x[1] != 0:
            constituicaoassembleia2.append(x)
    partidos = []
    sizes = []
    for x in constituicaoassembleia2:
        partidos.append(x[0])
        sizes.append(x[1])
        
    import matplotlib.pyplot as plt
    fig1,ax1 = plt.subplots()
    ax1.pie(sizes,labels = partidos)
    ax1.axis("equal")
    plt.show()
    
def menu():
    """Método que mostra o menu ao utilizador

    Ensures: Repetidamente, imprime um menu como o apresentado
    no enunciado, pede os dados necessários para a opção escolhida e
    invoca a função adequada à opção escolhida  
    """
    print("Bem-vindo ao sistema de simulçãao do método de Hondt.")
    print("Eis as suas opções:")
    print("-- determina número de mandatos (escolha d)")
    print("-- mostra quantos mandatos o sistema considera (escolha qm)")
    print("-- repor ficheiro de dados (escolha r)")
    print("-- listar distritos (escolha l)")
    print("-- mostrar votação de um distrito (escolha mv)")
    print("-- mostrar número de mandatos de um distrito (escolha mn)")
    print("-- agrupar distritos (escolha a)")
    print("-- mostrar mandatos de um distrito (escolha mm)")
    print("-- mostrar assembleia (escolha ma)")
    print("-- gráfico de tarte (escolha gt)")
    print("-- terminar (escolha q)")
    escolha = input("A sua escolha: ")

    while (escolha != "q"):
        if escolha == "d":
            global numeroMandatos
            numeroMandatos = int(input("Escreva um número inteiro positivo: "))
            determinaNumMandatos(numeroMandatos)
        if escolha == "qm":
            quantosMandatos()
        if escolha == "r":
            ficheiro = input("Escreva o nome do ficheiro: ")
            repor(ficheiro)
        if escolha == "l":
            listarDistritos(votacoes)
        if escolha == "mv":
            distrito = int(input("Escreva o número do distrito: "))
            mostrarVotacao(distrito, votacoes)
        if escolha == "mn":
            distrito = int(input("Escreva o número do distrito: "))
            mostrarNumMandatos(numeroMandatos,distrito,votacoes)
        if escolha == "a":
            print("Escreva uma lista com números de distritos")
            listadistritos = []
            numero = int(input("Escreva o número de elementos da lista: "))
            for i in range(0,numero):
                elemento=int(input("Escreva um elemento: "))
                listadistritos.append(elemento)
            listadistritos.sort()
            agruparDistritos(listadistritos, votacoes)
        if escolha == "mm":
            distrito = int(input("Escreva o número do distrito: "))
            mostraMandatos(numeroMandatos, distrito,votacoes)
        if escolha == "ma":
            mostraAssembleia(numeroMandatos,votacoes)
        if escolha == "gt":
            graficoTarte(numeroMandatos,votacoes)

        escolha = input("A sua escolha: ")
        
    else:
        print("Terminar")
