def valorPagamento():
    # lista vazia e contador antes do while
    quantprest=0
    somaprest=[]
    while True:
        prestaçao=float(input('\nDigite o valor da Prestação: '))
        diatrasado=float(input('Digite quantos dias de atraso: '))
        
        prestaçaoj=prestaçao*1.03
        prestaçaoja=prestaçaoj*(0.001*diatrasado)
        prestaçaoj+=prestaçaoja
        print('Valor da prestação com juros:',prestaçaoj)
        # adicionar todos as prestações na lista
        somaprest.append(prestaçaoj)
        quantprest+=1
        # Quando digitar 2, irá dar output da lista já somado
        end=input('\nAdicionar outra prestação?\n1 - Adicionar outra prestação\n\n2 - Encerrar o programa\n\n')
        if end == '2':
            print('\nO valor total das',quantprest,'prestações deu:',sum(somaprest))
            break
        else:
            continue

valorPagamento()

