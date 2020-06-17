



#CONVERSOR PARA LISTAS
a, b, c = "brayan", 20, True

lista = list([a, b, c])
for i in lista:
    print(type(i))

#CONVERSOS NUMEROS
d, e = 2.4, 3

print(int(d)) #converte para inteiro mas nao arredonda
print(float(e)) #adciona ponto flutuante


# FUNÇÃO FOR
#percorrendo lista
carros = ['fusca', 'kombi', 'onix']
for n in carros:
    print('Percorrendo itens da lista: ' + n)
#percorrendo range 
for a in range(0, 10, 3):
    print(a)
