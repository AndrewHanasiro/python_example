# lista = [1,2,1,5,8,6,9,4,3,5,7,4,0,4]
# number = 4
# resultado = 3

# def func_count(x, y):
#     a = 0
#     print(len(x))
#     for posi in range(len(x)):
#         print(posi, x[posi])
#         if x[posi] == y:
#             a = a + 1
#     print(a)

# lista = [2,4,3,2,1,5,2]
# number = 2
# func_count(lista,number)

# valor:  4   3   2   1   5
# posi:   0   1   2   3   4
# len(lista) = 5

# //-------------------------------------------------------------

# lista = [1,2,1,5,8,6,9,4,3,5,7,4,0,4]
# lista_number = [8,4,1]
# resultado = [1,3,2]

def func_count(x, y):
    list_count = []
    print(len(x),len(y))
    for posi in range(len(y)):
        count = 0
        for posi2 in range(len(x)):
            if y[posi] == x[posi2]:
                count = count + 1
        list_count.append(count)
    print(list_count)    
    

lista = [1,2,1,5,8,6,9,4,3,5,7,4,0,4]
lista_number = [8,4,1]
func_count(lista, lista_number)
