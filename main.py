line_p1s = []  # linhas do primeiro programa na versão que o usuário irá digitar
line_p2s = []  # linhas do segundo programa na versão que o usuário irá digitar
line_p1c = []  # linhas do primeiro programa na versão composta
line_p2c = []  # linhas do segundo programa na versão composta

def main():
    print("Primeiro Programa")
    print("Escreva o programa separando as linhas com enter e finalize com '")
    line_count = 1
    info = input("%i: " % line_count)
    while info != "'":
        line_p1s.append(info)
        line_count += 1
        info = input("%i: " % line_count)
    print(line_p1s)
    line_p1c = conversion(line_p1s)
    print(line_p1c)

    # vou deixar a parte do programa 2 aqui, mas comentada pra agilizar na hora de fazer os testes
    # na versão final a gente 'descomenta'
    """
    print("Segundo Programa")
    print("Escreva o programa separando as linhas com enter e finalize com '")
    line_count = 1
    info = input("%i: " % line_count)
    while info != "'":
        line_p2s.append(info)
        line_count += 1
        info = input("%i: " % line_count)
    print(line_p2s)
    line_p1c = conversion(line_p2s)
    """
    pass

def conversion(lines):
    """Conversion recebe como parametro as linhas digitadas pelo o usuário e converter para versão composta"""
    opc1 = []  # vetor que irá guardar a primeira informação do programa composto, ou seja, a função que ele irá executar em caso de true
    lc1 = []  # vetor que irá guardar a segunda informação do programa composto, ou seja, a linha que ele irá em caso de true
    opc2 = []  # vetor que irá guardar a terceira informação do programa composto, ou seja, a função que ele irá executar em caso de false
    lc2 = []  # vetor que irá guardar a quarta informação do programa composto, ou seja, a linha que ele irá em caso de false
    line_count = 1
    for line_original in lines:
        line = line_original.lower()
        if 'se' in line:
            # se for um Se...
            position_p1 = line.find('para ') + 5  # procura a posição do primeiro parâmentro
            # verifica de quantos dígitos é o número do parâmetro
            param1 = ''
            while position_p1 < len(line):
                if line[position_p1] != ' ':
                    param1 += line[position_p1]
                    position_p1 += 1
                else:
                    break
            position_p2 = position_p1+line[position_p1:].find('para ') + 5  # procura a posição do segundo parâmentro
            # verifica de quantos dígitos é o número do parâmetro
            param2 = ''
            while position_p2 < len(line):
                if line[position_p2] != ' ':
                    param2 += line[position_p2]
                    position_p2 += 1
                else:
                    break
            lc1.append(int(param1))
            lc2.append(int(param2))
            print(len(lines))
            if int(param1) == 0 or int(param1) > len(lines):
                opc1.append("parada")
            else:
                opc1.append("None")  # mais tarde, 'None' serão substituidos
            if int(param2) == 0 or int(param2) > len(lines):
                opc2.append("parada")
            else:
                opc2.append("None")  # mais tarde, 'None' serão substituidos
            #print(param1)
            #print(param2)
            #TODO: colocar exeções caso a sintaxe esteja errada
            #TODO: implementar o metodo que substitui os nones pela função que é executada
        else:
            if 'faça' in line:
                # se for um Faça...
                position_p1 = line.find('faça ') + 5  # procura a posição do primeiro parâmentro
                # verifica de quantos dígitos é o nome do parâmetro
                param1 = ''
                while position_p1 < len(line):
                    if line[position_p1] != ' ':
                        param1 += line_original[position_p1]
                        position_p1 += 1
                    else:
                        break
                position_p2 = position_p1 + line[position_p1:].find('para ') + 5  # procura a posição do segundo parâmentro
                # verifica de quantos dígitos é o número do parâmetro
                param2 = ''
                while position_p2 < len(line):
                    if line[position_p2] != ' ':
                        param2 += line[position_p2]
                        position_p2 += 1
                    else:
                        break
                opc1.append(param1)
                opc2.append(param1)
                lc1.append(int(param2))
                lc2.append(int(param2))
                #print(param1)
                #print(param2)
            else:
                raise NameError("Erro - O programa digitado é inválido")
        line_count += 1  # conta a linha atual
    return formatt(opc1,lc1,opc2,lc2)

def formatt(c1, c2, c3, c4):
    """Função que fomata o texto da função composta"""
    aux = []
    x = 0
    while x < len(c1):
        aux.append("(%s,%i),(%s,%i)" % (c1[x],c2[x],c3[x],c4[x]))
        x += 1
    return aux

main()