dicionario = {}

while True:
    cidade = input("Digite o nome da sua cidade: ")
    if cidade == '':
        break
    
    sigla = (input("Digite a sigla de seu estado: "))

#Adiciona os dados ao dicionário 
    dicionario[cidade] = {"cidade": cidade, "sigla": sigla}

#Imprime o cadastro completo

print(dicionario)