# coding: utf-8
# Aluno: Gabriel Max Vieira Matos - CC (UFCG)
# Matricula: 117110060
# Atividade: LyTBniv6O

# Entrada no número de vertices.
n = int(raw_input())
saida = []

for i in range(n):
	vertice = raw_input()
	conectados = raw_input()
	
	# Caso o vertice não possua nenhuma outro vértice
	# conectado a ele, esse vertice é adicionado na lista de
	# saída.
	
	if conectados == "":
		saida.append(vertice)

print (saida)
