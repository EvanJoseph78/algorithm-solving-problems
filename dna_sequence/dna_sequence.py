input1 = input()

lista = [char for char in input1]

local_max_value = 1
global_max_value = 1

for i in range(0, len(lista)-1):
    if lista[i] == lista[i+1]:
        local_max_value = local_max_value + 1
    else:
        local_max_value = 1

    if local_max_value > global_max_value:
        global_max_value = local_max_value


print(global_max_value)
