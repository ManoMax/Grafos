# coding: utf-8
# Aluno: Gabriel Max Vieira Matos - CC (UFCG)
# Matricula: 117110060
# Atividade: MOQStViSG

# Funções:
def degree(v,graph):
   adj_vertices = graph[v]
   return len(adj_vertices) + (adj_vertices.count(v))

def max_degree(g):
        seq = []
        for vertex in g:
            seq.append(degree(vertex,g))
        seq.sort(reverse=True)
        return seq[0]

def min_degree(g):
        seq = []
        for vertex in g:
            seq.append(degree(vertex,g))
        seq.sort(reverse=False)
        return seq[0]

# Entrada no número de vertices e definição de grafo.
n = int(input())
grafo = {}

# Acrescenta-se os vertices com suas respectivas conexões.
for i in range(n):
	vertice = input()
	adjacentes = input().split()
	grafo[vertice] = adjacentes

# Define se o grafo é completo ou não:
saida = True
if max_degree(grafo) != min_degree(grafo):
	saida = False
print (saida)
