carros = ['fusca', 'gol', 'cruze']
motos = ['fan 160', 'bros', 'bmwg310']
veiculos = carros + motos
veiculosbkp = veiculos.copy() #cria bkp copia dos dados

print(veiculos)


#adicinado avião
veiculos.append('avião')
print(veiculos) 

#mudando indice 0 para kombi
veiculos[0] = 'kombi'
print(veiculos)

#removendo avião
veiculos.remove('avião')
print(veiculos)

#removendo com função pop, remove ultimo ítem sem argumento, ou determina o índice para remoção
#retorna ítem removido
print(veiculos.pop(-2))
print(veiculos.pop())

print(veiculosbkp) #imprimindo o backup
print(veiculos)
