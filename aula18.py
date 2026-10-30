'''teste = list()
teste.append('Marcelo')
teste.append(42)
galera = list()
galera.append(teste[:]) # Os dois pontos (:) serve para copiar a lista, possibiltando fazer as substuições de 'Marcelo' para "Ana" e a idade
teste[0] = 'Ana'
teste[1] = 21
galera.append(teste[:])
print(galera)'''


'''galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
#print(galera)
#print(galera[0])     # 3 OPÇÕES DE PRINT DE ACORDO COM A NECESSIDADE
#print(galera[2][1])
for p in galera:
    #print(p[0])
    #print(p[1])
    print(f'{p[0]} tem {p[1]} anos')'''

galera = list()
dado = list() # estrutura axiliar que pega os dados, para depois ir para estrutura principal que é 'GALERA'
totmai = totmen = 0 # posso fazer com variável simples. (não em variavel composta)
for c in range(0, 3): # Esse bloco 'FOR in RANGE' é para ler os dados
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:]) #Lembrar de fazer a Cópia [:]
    dado.clear() # para apagar os dados cada vez que for analisado
#print(galera) # Opção de de apresentação da lista

for p in galera: # Esse bloco 'FOR p in' é para ler se é maior ou menor de idade
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade')


