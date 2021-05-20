list_numbers = [1,8,6,9,7,3,4,5,2]

print(list_numbers)

ok = False
while(ok != True):
    ok = True
    for i in range(len(list_numbers) - 1): 
        if(list_numbers[i] > list_numbers[i+1]):
            temp = list_numbers[i]
            list_numbers[i] = list_numbers[i+1]
            list_numbers[i+1] = temp
            ok = False
            print(list_numbers)
            
    print("fim while")

print(list_numbers)

for contador in range(8): 
    print(contador)
