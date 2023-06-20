def maior(* núm):
    cont = maior = 0
    for valor in núm:
        print(f'{valor}', end=' ')
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print('O maior valor é: {}'.format(maior))
    
    
maior(5,6,9,23)
    