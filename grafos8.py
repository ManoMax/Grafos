# coding: utf-8
# Aluno: Gabriel Max
# Matrícula: 117110060
# Atividade: SroLhG2Yi

# Funções:
def generate_edges(g):
    edges = []
    for node in g:
       for neighbour in g[node]:
            edges.append((node, neighbour))
    return edges

def generate_edgesSR(g):
    edges = []
    for node in g:
       for neighbour in g[node]:
            if not (neighbour,node) in edges: 
                edges.append((node, neighbour))
    return edges

# Numero de Vertices
n = int(raw_input())
grafo = {}

# Entrada de Vertices e Arestas no Grafo:
for i in range(n):
	vertice = raw_input()
	arestas = raw_input().split()
	grafo[vertice] = arestas

# Caminho percorrido a ser analisado:
caminho = raw_input().split()

# Passeio existe inicialmente.
# Nenhuma Aresta utilizada até o momento.
# Lista de Vertices presentes no Grafo.
passeio = True
utilizado = []
vertices = generate_edges(grafo)

# Compara se as Arestas e Vertices estão em ordem de um caminho:
for arestas in range(len(caminho)-1):
	if caminho[arestas][1] != caminho[arestas+1][0]:
		passeio = False

# Define um padrão de vizualização de Arestas:
for i in range(len(caminho)):
	v1 = caminho[i][0]
	v2 = caminho[i][1]
	compara = (v1, v2)
	# Analisa se esta presente no Grafo:
	if compara in vertices:
		# Analisa se foi utilizada:
		if compara not in utilizado:
			utilizado.append(compara)
			compara = (v2, v1)
			utilizado.append(compara)
		else:
			passeio = False
	else:
		passeio = False

vertices = generate_edgesSR(grafo)
if len(vertices) != len(caminho):
	passeio = False
	
print (passeio)
