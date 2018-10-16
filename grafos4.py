# coding: utf-8
# Aluno: Gabriel Max Vieira Matos - CC (UFCG)
# Matricula: 117110060
# Atividade: NfVzkCF6m

# Funções:
def degree(v,graph):
   adj_vertices = graph[v]
   return len(adj_vertices) + (adj_vertices.count(v))

def generate_edges(g):
    edges = []
    for node in g:
       for neighbour in g[node]:
            if not (neighbour,node) in edges: 
                edges.append((node, neighbour))
    return edges

# Entrada no número de vertices e definição de grafo.
n = int(raw_input())
grafo1 = {}

# Acrescenta-se os vertices com suas respectivas conexões no Grafo1.
for i in range(n):
	vertice = raw_input()
	adjacentes = raw_input().split()
	grafo1[vertice] = adjacentes

n = int(raw_input())
grafo2 = {}

# Acrescenta-se os vertices com suas respectivas conexões no Grafo1.
for i in range(n):
	vertice = raw_input()
	adjacentes = raw_input().split()
	grafo2[vertice] = adjacentes

# Define o Grafo2 é subgrafo do Grafo1:
saida = True
for i in range(len(generate_edges(grafo2))):
	if generate_edges(grafo2)[i] not in generate_edges(grafo1):
		saida = False

print (saida)
