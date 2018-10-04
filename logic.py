from tkinter import messagebox

#traduz de monolítica rotulada para formato de instruções compostas

def translation(line_p):
    line_count = 1
    newline_p = [] #string que irá salvar o programa formatado
    for line in line_p.split('\n'):
        if (line != ''):
            newline_p.append("%i: %s" % (line_count, line))
            line_count += 1
    if (line_count == 1):
        messagebox.showinfo(icon="error",title='Erro',message="Programa vazio.")
    else:
        #newline_p = newline_p[:-1]
        print("new= ")
        print(newline_p)
        newline_p = conversion(newline_p)
        print(newline_p)
        return newline_p

def numCorrection(array,n):
    '''Recebe um array de comandos e corrige o número de suas instruções'''
    for i, line in enumerate(array):
        # procura as posições dos dois parâmetros
        p1 = line.find(')') - 1
        p2 = p1 + 2 + line[p1+2:].find(')') - 1
        s = list(line)
        print(p1,p2)
        s[0] = str(int(s[0]) + n)
        # verifica se a instrução não leva para uma parada (0) ou para um ciclo (c)
        if(s[p1] != '0' and p1 != 'c'):
            s[p1] = str(int(s[p1]) + n)
        if(s[p2] != '0' and p2 != 'c'):
            s[p2] = str(int(s[p2]) + n)
        array[i] = "".join(s)
    return array

def paramNumber(position, line):
    '''Verifica de quantos dígitos é o número do parâmetro'''
    param = ''
    while position < len(line):
        if line[position] != ' ':
            param += line[position]
            position += 1
        else:
            break
    return param

def conversion(lines):
    """Conversion recebe como parametro as linhas digitadas pelo o usuário e converter para versão composta"""
    opc1 = []  # vetor que irá guardar a primeira informação do programa composto, ou seja, a função que ele irá executar em caso de true
    lc1 = []  # vetor que irá guardar a segunda informação do programa composto, ou seja, a linha que ele irá em caso de true
    opc2 = []  # vetor que irá guardar a terceira informação do programa composto, ou seja, a função que ele irá executar em caso de false
    lc2 = []  # vetor que irá guardar a quarta informação do programa composto, ou seja, a linha que ele irá em caso de false
    line_count = 1
    for line_original in lines:
        line = line_original.lower()
        # se for um Se...
        if 'se' in line:
            try:
                # procura a posição do primeiro parâmentro
                position_p1 = line.find('para ') + 5
                if (line[position_p1] == line[0]): 
                    messagebox.showinfo(icon="warning", title='Ciclo infinito', message="A instrução " + str(line[0]) + " aponta para ela mesma.")
                    return  
                param1 = paramNumber(position_p1, line)
                # procura a posição do segundo parâmentro
                position_p2 = position_p1 + line[position_p1:].find('para ') + 5
                if (line[position_p2] == line[0]): 
                    messagebox.showinfo(icon="warning", title='Ciclo infinito', message="A instrução " + str(line[0]) + " aponta para ela mesma.")
                    return
                if (line[position_p1] == line[position_p2]):
                    messagebox.showinfo(icon="error", title='Erro', message="A instrução " + str(line[0]) + " aponta para o mesmo lugar mais de uma vez.")
                    return
                param2 = paramNumber(position_p2, line)
                lc1.append(int(param1))
                lc2.append(int(param2))
                if int(param1) == 0 or int(param1) > len(lines):
                    opc1.append("parada")
                else:
                    opc1.append("None")  # mais tarde, 'None' serão substituidos
                if int(param2) == 0 or int(param2) > len(lines):
                    opc2.append("parada")
                else:
                    opc2.append("None")  # mais tarde, 'None' serão substituidos
                # print(param1)
                # print(param2)
            except:
                messagebox.showinfo(icon="error",title='Erro',message="Programa inválido.")
        else:
            # se for um Faça...
            if 'faça' in line:
                try:
                    # procura a posição do primeiro parâmentro
                    position_p1 = line.find('faça ') + 5
                    param1 = paramNumber(position_p1, line_original)
                    # procura a posição do segundo parâmentro
                    position_p2 = position_p1 + line[position_p1:].find('para ') + 5
                    if (line[position_p2] == line[0]): 
                        messagebox.showinfo(icon="warning", title='Ciclo infinito', message="A instrução " + str(line[0]) + " aponta para ela mesma.")
                        return 
                    param2 = paramNumber(position_p2, line)
                    lc1.append(int(param2))
                    lc2.append(int(param2))
                    opc1.append(param1)
                    opc2.append(param1)
                    # print(param1)
                    # print(param2)
                except:
                    messagebox.showinfo(icon="error",title='Erro',message="Programa inválido.")
            else:
                messagebox.showinfo(icon="error",title='Erro',message="Programa inválido.")
        # TODO: implementar o metodo que substitui os 'Nones' pela função que é executada
        line_count += 1  # conta a linha atual
    opc1, lc1, opc2, lc2, ignore = translate(opc1, lc1, opc2, lc2)
    return formatt(opc1,lc1,opc2,lc2,ignore)

def ifVerification(x, ca, cb, cc, cd, ignore):
    '''Verificação das instruções se'''
    y = cb[x] - 1  # ve para onde o campo está apontando
    while ca[x] == 'None':  # se o código se deparar com um teste ele irá verificar a próxima linha de comando
        if ca[y] == 'None':  # se a próxima linha de comando for outro teste ele irá a ignorar e ver para onde ela aponta
            if x < y:
                ignore.append(y)
            y = cb[y] - 1
            cb[x] = cb[y]-len(set(ignore))  # o teste original irá apontar para onde apontava o teste final
        else:
            ca[x] = ca[y]  # e fazer a função que ele fazia
            if x < y:
                ignore.append(y)
            if ca[y] == cc[y] and cb[y] == cd[y]:  # se for um faça o teste irá apontar para onde o faça aponta
                cb[x] = cb[y] - len(set(ignore))
                if len(ignore)>0:
                    if cb[y] <= min(ignore):
                        cb[x] = cb[y]
    return ca, cb, ignore

def translate(c1, c2, c3, c4):
    """Função que traduz de simples para composto"""
    # boa parte da função serve para criar um modelo de texto do fluxograma
    ignore = []  # conjunto de linhas desnecessárias no programa composto
    seq = [0]  # lista de linhas necessárias no programa composto, o primeiro sempre é traduzido
    x = 0
    while x < len(c1):  # enquanto ainda tiver codigo para traduzir
        if c1[x] == c3[x] and c2[x] == c4[x]:  # sempre que houver uma função faça a proxima linha de comando é garantida na tradução
            seq.append(c2[x] - 1)
        c1, c2, ignore = ifVerification(x, c1, c2, c3, c4, ignore) # verificação do campo true
        c3, c4, ignore =ifVerification(x, c3, c4, c1, c2, ignore) # verificação do campo false
        x += 1
    if max(seq) >= len(c1) or -1 in seq:  # caso haja um teste que aponte para uma parada adiciona uma parada ao código
        c1.append('parada')
        c2.append(0)
        c3.append('parada')
        c4.append(0)
        if -1 in seq:  # caso haja um parada direto para 0 redefine para o final
            seq.remove(-1)
            seq.append(x)
    return c1, c2, c3, c4, seq

def formatt(c1, c2, c3, c4, seq):
    """Função que formata o texto da função composta"""
    aux = []
    id_f = 1
    for x in seq:
        if c2[x] <= 0 and c1[x] != 'parada':  # corrige alguns apontamentos de parada
            c2[x] = len(seq)
        if c4[x] <= 0 and c3[x] != 'parada':
            c4[x] = len(seq)
        if c2[x] < 0 and c1[x] == 'parada':  # formaliza as paradas em 0
            c2[x] = 0
        if c4[x] < 0 and c3[x] == 'parada':
            c4[x] = 0
        aux.append("%i: (%s,%i),(%s,%i)" % (id_f, c1[x], c2[x], c3[x], c4[x]))
        id_f += 1
    return aux
