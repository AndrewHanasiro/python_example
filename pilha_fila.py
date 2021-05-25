# Pilha: O primeiro que entra é o último que sai

def append(num,lista):
    return lista + [num]
    
def construir_lista(lista:list, indice:int):
    lista_n = []
    for posi in range(len(lista)):
        if indice != posi:
            lista_n = append(lista[posi], lista_n)
    return lista_n

def pop(lista, indice = -1):
    num_f = lista[indice]
    lista_f = construir_lista(lista, indice)
    return (num_f, lista_f)

lista=[]
lista=append("p1", lista)
lista=append("p2", lista)
lista=append("p3", lista)
lista=append("p4", lista)
(p4,lista)=pop(lista)
(p3,lista)=pop(lista)
(p2,lista)=pop(lista)
(p1,lista)=pop(lista)
print(p1,p2,p3,p4)

# Fila: O primeiro que entra é o primeiro que sai
lista=[]
lista=append("p1", lista)
lista=append("p2", lista)
lista=append("p3", lista)
lista=append("p4", lista)
(p1,lista)=pop(lista,0)
(p2,lista)=pop(lista,0)
(p3,lista)=pop(lista,0)
(p4,lista)=pop(lista,0)
print(p1,p2,p3,p4)

