input1 = input()
input2 = input()
output = 0

listaNumeros = [int(num) for num in input2.split()]
listaNumeros.sort()

i = 1
for num in listaNumeros:
    if i != num:
        output = i
        break
    output = i + 1
    i = i + 1

print(output)


