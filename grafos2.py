# coding: utf-8
# Aluno: Gabriel Max Vieira Matos - CC (UFCG)
# Matricula: 117110060
# Atividade: PutJQBIjg

# Funções:
def degree(v,graph):
   adj_vertices = graph[v]
   return len(adj_vertices) + (adj_vertices.count(v))

# Entrada no número de vertices e definição de grafo.
n = int(input())
grafo = {}

# Acrescenta-se os vertices com suas respectivas conexões.
for i in range(n):
	vertice = input()
	adjacentes = input().split()
	grafo[vertice] = adjacentes

# Seleciona e print grau do Vertice a ser analisado.
print (degree(input(), grafo))
