def separar_chave_valor(dicionario):
    chaves = []
    valores = []
    for chave, valor in dicionario.items():
        chaves.append(chave)
        valores.append(valor)
    return chaves, valores
    
dicionario2 = {'Primeiro':'Gabriel', 'Segundo': 'Maria', 'Terceiro': 'Murilo'}
chaves, valores = separar_chave_valor(dicionario2)
print(chaves)  
print(valores)