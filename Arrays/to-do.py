'''
Objetivo: criar um lista de tarefas. Depois o usuário decide o que fazer com as tarefas.
'''
import os
tarefas=[]
des=True
RED   = "\033[1;31m" 
CYAN  = "\033[1;36m"
RESET = "\033[0;0m"

while(des==True):
    os.system("cls")
    tarefas.append(input("Lista de tarefas do dia.\nInsira as tarefas:"))
    exit=input("Deseja continuar?(Y/N)")
    if exit == "Y":
       print(" ")
    else:
        des=False
    for i in range(len(tarefas)):
        print(i,") ",tarefas[i])
while(des==False):
    os.system("cls")
    for i in range(len(tarefas)):
        print(i,") ",tarefas[i])

    exit=input("\n1)Concluir tarefa\n2)Excluir tarefa\n3)Limpar Lista\n4)Finalizar programa")
    if exit == "1":
        os.system("cls")
        for i in range(len(tarefas)):
            print(i,") ",tarefas[i])
        qual=int(input(CYAN + "Qual tarefa foi concluída?" + RESET))
        tarefas[qual]= tarefas[qual] + (CYAN + " Ok!" + RESET)
    elif exit == "2":
        os.system("cls")
        for i in range(len(tarefas)):
            print(i,") ",tarefas[i])
        qual=int(input(RED + "Qual tarefa excluir?" + RESET) )
        tarefas.pop(qual)
    elif exit =="3":
        tarefas.clear()
    elif exit == "4":
        des=True
        os.system("cls")
    else:
        print()