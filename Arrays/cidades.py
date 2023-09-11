#Declara e inicializa uma listagem com 3 elementos
cidades=["Juiz de Fora", "Matias","Piau", "Rio"]
letras=['a','b','c','d','e','f','g','h','i','j']

#Declara lista vazia
cidades2=[]

#Exibe toda a estrutura
print(cidades)

#Exibe o segundo item da lista(Matias)
print(cidades[1])

#Exibe, na lista:
print(cidades[-1])#Último
print(cidades[-2])#Penúltimo
print(cidades[-4])#Inválido

print(letras[:3])#Mostrando os 3 primeiros itens
print(letras[3:])#Mostrando todos os valores após os 3 primeiros itens
print(letras[2:5])#Mostrando intervalo entre 2 e 5(ambos inclusos)
print(letras[2::2])

first3=letras[:3]
last3=letras[:-3]
print(first3)
print(last3)