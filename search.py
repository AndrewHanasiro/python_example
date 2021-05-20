#bubblesort
# [3,5,2,7,1,4,6]
# [3,2,5,1,4,6,7]
# [2,3,1,4,5,6,7]
# [2,1,3,4,5,6,7]
# [1,2,3,4,5,6,7]

# def ordenar_bubblesort(lista):
#     esta_ordenado= False
#     acumulador = 0
#     while esta_ordenado == False:
#         for posi in range(len(lista)- 1):
#             if lista[posi] > lista[posi + 1]:
#                 acumulador = lista[posi + 1]
#                 lista[posi + 1] = lista[posi]
#                 lista[posi] = acumulador

#         esta_ordenado = True
#         for posi in range(len(lista)- 1):
#             if lista[posi] > lista[posi + 1]:
#                 esta_ordenado=False
#     return lista

def ordenar_bubblesort(lista):
    esta_ordenado= False
    acumulador = 0
    while esta_ordenado == False:
        esta_ordenado = True
        for posi in range(len(lista)- 1):
            if lista[posi] > lista[posi + 1]:
                acumulador = lista[posi + 1]
                lista[posi + 1] = lista[posi]
                lista[posi] = acumulador
                esta_ordenado=False
    return lista

lista = [3,5,2,7,1,4,6]
lista_ordenada = ordenar_bubblesort(lista)
print(lista_ordenada)


#-----------------------------------------------------
#insertion sort
# [3,5,2,7,1,4,6]
# [3,5,2,7,1,4,6]
# [2,3,5,7,1,4,6]
# [2,3,5,7,1,4,6]
# [1,2,3,5,7,4,6]
# [1,2,3,4,5,7,6]
# [1,2,3,4,5,6,7]
def coloca_numero_na_lista(lista_ordenada: list, numero: int) -> list:
    lista_temp=[] 
    posi = 0
    numero_foi_inserido=False
    while posi < len(lista_ordenada):
        if numero_foi_inserido:
            lista_temp.append(lista_ordenada[posi])
        else:
            if lista_ordenada[posi] < numero :
                lista_temp.append(lista_ordenada[posi])
            else:
                lista_temp.append(numero)
                lista_temp.append(lista_ordenada[posi])
                numero_foi_inserido=True
        posi=posi+1
    if not numero_foi_inserido:
        lista_temp.append(numero)
    return lista_temp

def ordenar_insertion_sort(lista):
    lista_ordenada=[]
    for posi in range(len(lista)):
        numero=lista[posi]
        lista_ordenada = coloca_numero_na_lista(lista_ordenada, numero)
    return lista_ordenada

lista = [3,5,2,7,1,4,6]
lista_ordenada2 = ordenar_insertion_sort(lista)
print(lista_ordenada2)


#-----------------------------------------------------
#selection sort

#1)procurar o menor numero na parte desordenada
#2)apaga-lo de sua posicao original
#3)coloca-lo na ultima posicao do ordenados
#4) volte para o passo 1 ate que a parte dos desordenados nao exista mais

def copy_list(lista:list) -> list:
    tamanho=len(lista)
    result = []
    for l in range(tamanho):
        result.append(lista[l])
    return result

def ache_menor_numero_da_lista(lista_ordenada, posi):
    menor = 9999999
    posi_menor = 0
    for posi1 in range(posi, len(lista_ordenada)):
        if lista_ordenada[posi1] < menor:
            menor = lista_ordenada[posi1]
            posi_menor = posi1
    return posi_menor

def coloca_numero_na_lista(posi: int, posi_menor:int, lista_ordenada:list):
    list_temp = copy_list(lista_ordenada)
    list_temp[posi] = lista_ordenada[posi_menor]
    list_temp[posi_menor] = lista_ordenada[posi]
    return list_temp

def ordenar_selection_sort(lista):
    for posi in range(len(lista)):
        posi_menor=ache_menor_numero_da_lista(lista, posi)        
        lista = coloca_numero_na_lista(posi, posi_menor, lista)
    return lista

lista = [3,5,2,7,1,4,6]
lista_ordenada3 = ordenar_selection_sort(lista)
print(lista_ordenada3)

#-----------------------------------------------------
#merge-sort
#[3,5,2,7,1,4,6,9,10,8,11]
#[[3,5],[2,7],[1,4],[6,9],[10,8,11]]
#[[3,5],[2,7],[1,4],[6,9],[8,10,11]]
# aqui acaba a devisões
#[[2,3,5,7],[1,4,6,9],[8,10,11]]
#[[1,2,3,4,5,6,7,9],[8,10,11]]
#[[1,2,3,4,5,6,7,8,9,10,11]]

#dividir o conjunto maior em duplas ate precise ou nao do ultimo ser um trio
#organizar dentro dos mini conjuntos
#juntar  em duplas em um conjunto e organiza-las
#repetir passo 2 ate que todos os mini conjuntos estejam juntos e organizados

def quantidade_faltante():

def verificar_dup_tri():
    pass

def separador_dupla():
    pass

def separador_trio():
    pass

def organizador_dupla():
    pass

def verif_continue():
    pass    


def ordenar_merge_sort(lista):
    for number in range (len())
    verificacao = verificar_dup_tri(lista)
    while verif_continue == True:
        lista_dupla_inicial = 
        lista_tripa_inicial = 
        
        if verificacao:
            lista_dupla = separador_dupla()
        else:
            lista_tripa = separador_trio()

        verif_continue()

# [3,5,2,7,1,4,6]
# verificacao




lista = [3,5,2,7,1,4,6]
lista_ordenada4 = ordenar_merge_sort(lista)
print(lista_ordenada4)