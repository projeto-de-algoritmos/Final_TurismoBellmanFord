import heapq
from time import perf_counter as timer

nodes = {   
    1: 'Ceilândia', 2: 'Samambaia', 3: 'Taguatinga', 4: 'Plano Piloto',
    5: 'Planaltina', 6: 'Águas Claras', 7: 'Recanto das Emas', 8: 'Gama', 
    9: 'Guará', 10: 'Sobradinho', 11:'Park Way',
    12: 'Congresso Nacional', 13: 'Palácio do Planalto', 14: 'Palácio Itamaraty',
    15: 'Palácio da Alvorada',
    16: 'Biblioteca Nacional', 17: 'Ponte JK', 18: 'Torre de TV', 19: 'Pontão do Lago Sul',
    20: 'Jardim Botânico de Brasília',
    21: 'Parque Ecológico de Águas Claras', 22: 'Ermida Dom Bosco', 23: 'Memorial JK',
    24: 'Centro Cultural Banco do Brasil',
    25: 'Museu Nacional', 26: 'Museu do Catetinho',
    27: 'Catedral Metropolitana de Brasília', 28: 'FGA'
}

grafo = {}
numVertices = 0
arestas = []

def adcVertice(vertice):
  global grafo
  global numVertices
  numVertices += 1
  grafo[vertice] = []


for cidade in nodes:
  adcVertice(cidade)

def adcAresta(node1, node2, distancia):
  global grafo, arestas
  arestas.append((node1, node2, distancia))
  grafo[node1].append((node2, distancia))
  grafo[node2].append((node1, distancia))

adcAresta(1, 2, 9)
adcAresta(1, 3, 7)
adcAresta(2, 3, 13)
adcAresta(2, 7, 10)
adcAresta(3, 6, 8)
adcAresta(3, 4, 24)
adcAresta(4, 9, 15)
adcAresta(4, 10, 23)
adcAresta(5, 10, 22)
adcAresta(6, 9, 17)
adcAresta(7, 8, 17)
adcAresta(8, 11, 17)
adcAresta(11, 4, 15)
adcAresta(4, 12, 4)
adcAresta(4, 13, 5)
adcAresta(4, 14, 4)
adcAresta(4, 15, 9)
adcAresta(4, 16, 4)
adcAresta(4, 17, 8)
adcAresta(4, 18, 4)
adcAresta(4, 19, 7)
adcAresta(4, 20, 16)
adcAresta(6, 21, 2)
adcAresta(4,22,17)
adcAresta(4,23,5)
adcAresta(4,24,9)
adcAresta(4,25,4)
adcAresta(11,26,15)
adcAresta(4,27,3)
adcAresta(8,28,5)

def printGrafo(grafo = grafo):
  for node in range(1, 12):
      print('[{}] {}:'.format(node, nodes[node]), end=' ')
      for vizinho in grafo[node]:
        if vizinho != grafo[node][-1]:
            print('[{}] {}'.format(vizinho[0], nodes[vizinho[0]]), end=' - ')
        else:
            print('[{}] {}'.format(vizinho[0], nodes[vizinho[0]]))

dijDist = []
def dijkstra(partida,destino, printar = True):
  h = []
  heapq.heappush(h,(0,partida))
  global dijDist, grafo
  while len(h)!=0:
      currcost,currvtx = heapq.heappop(h)
      if currvtx == destino:
          dijDist.append(currcost)
          if printar:
            print("{} -> {}: {} km".format(nodes[partida],nodes[destino],currcost), end='')
          break
      for (neigh,neighcost) in grafo[currvtx]:
          heapq.heappush(h,(currcost+neighcost,neigh))

dist =[]

def bellmanFord(partida, destino = 1, gerarLista = True):
    global dist
    dist = [float("Inf")] * (len(nodes) + 1)
    dist[partida] = 0
    for i in range(len(nodes)):
        for (node1, node2, distancia) in arestas:
            if dist[node1] != float('Inf') and dist[node1] + distancia < dist[node2]:
                dist[node2] = dist[node1] + distancia
                if node2 == destino and not gerarLista:
                    return
            if dist[node2] != float('Inf') and dist[node2] + distancia < dist[node1]:
                dist[node1] = dist[node2] + distancia
                if node1 == destino and not gerarLista:
                    return

def menu():
  while True:
      print('01. Listar Cidades')
      print('02. Listar Pontos Turísticos')
      print('03. Distancia entre cidade e ponto turístico')
      print('04. Mostrar Lista de Adjacencias')
      print('05. Comparar Dijkstra e Bellman-Ford')
      print('06. Encerrar')
      print('\nA função 3 foi modificada para incluir o algoritmo de Bellman-Ford')
      print('A função 5 compara Bellman-Ford e Dijkstra em todos os nós de forma geral\n')

      func = int(input('Selecione uma função(1~6): '))
      if func == 1:
          print(' ')
          for cidade in nodes:
              print('[{}]: {}'.format(cidade, nodes[cidade]))
              if cidade == 11:
                  break
          print(' ')
      elif func == 2:
          print(' ')
          for x in range(13, 30):
              print('[{}]: {}'.format(x, nodes[x]))
          print(' ')
      elif func == 3:
          partida = int(input('Selecione a cidade de partida(1 - 11): '))
          destino = int(input('Selecione o ponto turistico de destino(12 - 28): '))
          print(' ')
          print('Dijkstra:')
          t0 = timer()
          dijkstra(partida, destino)
          t1 = timer()
          print(' ({:.10f} s)'.format(t1-t0))
          print('Bellman Ford:')
          t2 = timer()
          bellmanFord(partida, destino, False)
          t3 = timer()
          print(dist[destino], 'km',end=' ')
          print('({:.10f} s)'.format(t3-t2))
          print(" ")
      elif func == 4:
          print(" ")
          printGrafo(grafo)
          print(" ")
      elif func == 5:
        print('\nLista de distancias do ponto 1:\n')
        t0 = timer()
        for i in nodes:
          dijkstra(1, i, False)
        t1 = timer()
        print(dijDist)
        print('Dijkstra: {:.10f} segundos\n'.format(t1-t0))
        t2 = timer()
        bellmanFord(1)
        t3 = timer()
        print(dist[1:])
        print('Bellman-Ford: {:.10f} segundos\n'.format(t3-t2))
      elif func ==6:
          return
      else:
          print('Função não definida!\n')
menu()