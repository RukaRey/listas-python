amigos=['Neymar','Messi','Luan Gameplays',"Saninplay","AAA"]


amigos.append("Juan")#Adiciona um novo item ao final da lista
amigos.insert(1,"Sans Undertale")#Adiciona um item em um local determinado 
amigos.insert(0,"Jonas Especializado")#Adiciona um item como o primeiro da lista sem apagar outros itens
#Remover elementos:
amigos.remove("Saninplay")
amigos.pop(4)

#Exibe itens da lista de modo mais confortável aos olhos
for i in range(len(amigos)):
    print(amigos[i])
