# coding: utf-8
# Aluno: Gabriel Max
# Matrícula: 117110060
# Atividade: RVzvIkifI

# Cria-se um grafo vazio e recebe-se o tamanho que o mesmo irá ter
grafo = {}
n = int(input())

# São adicionados ao grafo os vertices e seus vertices adjascentes
for i in range(n):
	vertice = input()
	adjacentes = input()
	grafo[vertice] = adjacentes.split()

# O conjunto de vértices que seram cortados
conj_vert = input().split()
conj = []

# Esse for adiciona a lista conj_y, os vertices pertecentes
# ao grafo que não estão na lista de corte, ou seja o complemento
for j in grafo.keys():
	if j not in conj_vert:
		conj.append(j)

lista = []
# Os dois for's seguintes, adicionam na lista vazia acima as arestas que serão 
# necessárias tirar para efetuar o corte
for i in conj_vert:
	aresta = ''
	for ele in conj:
		if i in grafo[ele]:
			aresta = str(i) + str(ele)
			lista.append(int(aresta))

for i in conj:
	aresta = ''
	for ele in conj_vert:
		if i in grafo[ele]:
			aresta = str(i) + str(ele)
			lista.append(int(aresta))

# A função sort organiza a lista em ordem crescente
lista.sort()

# Esse for imprime cada elemento da lista de arestas
for i in lista:
	print (int(i))
