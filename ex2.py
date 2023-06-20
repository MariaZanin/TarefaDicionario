cadastro ={}

while True:
    nome = input('Digite o nome:')
    if nome == '':
     break
   
    idade = int(input('Digite a idade:'))
 
 #adiciona os dados ao dicionário
    cadastro[nome] = {"idade":idade,"nome":nome}
    
for nome, dados in cadastro.items():
    if dados["idade"] > 18:
       print(dados["idade"])