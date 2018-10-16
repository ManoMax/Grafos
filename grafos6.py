# coding: utf-8
# Aluno: Gabriel Max
# Matrícula: 117110060
# Atividade: Q2xcPgAZU

def generate_edges(g):
    edges = []
    for node in g:
       for neighbour in g[node]:
            edges.append((node, neighbour))
    return edges

n = int(raw_input())
grafo = {}

for i in range(n):
	vertice = raw_input()
	arestas = raw_input().split()
	grafo[vertice] = arestas

caminho = raw_input().split()

passeio = True

utilizado = []
vertices = generate_edges(grafo)

for arestas in range(len(caminho)-1):
	if caminho[arestas][1] != caminho[arestas+1][0]:
		passeio = False

for i in range(len(caminho)):
	v1 = caminho[i][0]
	v2 = caminho[i][1]
	compara = (v1, v2)
	if compara in vertices:
		if compara not in utilizado:
			utilizado.append(compara)
			compara = (v2, v1)
			utilizado.append(compara)
		else:
			passeio = False
	else:
		passeio = False

print passeio
