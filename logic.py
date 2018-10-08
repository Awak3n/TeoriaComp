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
        messagebox.showinfo(icon="error", title='Erro', message="Programa vazio.")
    else:
        newline_p = conversion(newline_p)
        return newline_p

def numCorrection(array,n):
    '''Recebe um array de comandos e corrige o número de suas instruções'''
    for i in range(0, int(len(array) / 5)):
        array[0 + (i * 5)] = int(array[0 + (i * 5)] + n/5)
        if array[1 + (i * 5)] is 'parada':
            array[2 + (i * 5)] = 0
        elif (array[1 + (i * 5)] is not 'parada' or array[1 + (i * 5)] is not 'ciclo'):
            array[2 + (i * 5)] = int(array[2 + (i * 5)] + n/5)
        if array[3 + (i * 5)] is 'parada':
            array[4 + (i * 5)] = 0
        elif (array[3 + (i * 5)] is not 'parada' or array[3 + (i * 5)] is not 'ciclo'):
            array[4 + (i * 5)] = int(array[4 + (i * 5)] + n/5)
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
            except:
                messagebox.showinfo(icon="error", title='Erro', message="Programa inválido.")
                return
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
                except:
                    messagebox.showinfo(icon="error",title='Erro',message="Programa inválido.")
                    return
            else:
                messagebox.showinfo(icon="error", title='Erro', message="Programa inválido.")
                return
        line_count += 1  # conta a linha atual
    opc1, lc1, opc2, lc2, ignore, dicionario = translate(opc1, lc1, opc2, lc2)
    return formatt(opc1,lc1,opc2,lc2,ignore, dicionario)

def ifVerification(x, ca, cb, cc, cd, ignore):
    '''Cria o diagrama de fluxo em forma de texto de cada instrução'''
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
                    if min(ignore) == 1:
                        copia = set(ignore)
                        controle = list(copia)[1]
                    else:
                        controle = min(ignore)
                    if cb[y] <= controle:
                        cb[x] = cb[y]
    return ca, cb, ignore

def translate(c1, c2, c3, c4):
    """Função que traduz de simples para composto"""
    ignore = []  # conjunto de linhas desnecessárias no programa composto
    seq = [0]  # lista de linhas necessárias no programa composto, o primeiro sempre é traduzido
    dicionario = {}
    x = 0
    while x < len(c1):  # enquanto ainda tiver codigo para traduzir
        if c1[x] == c3[x] and c2[x] == c4[x]:  # sempre que houver uma função faça a linha de comando apontada pelo faça é garantida na tradução
            y = c2[x] - 1
            try:
                if c1[y] == c3[y] and c2[y] == c4[y]:
                    if y not in seq:
                        seq.append(y)
                        dicionario[y] = len(seq) + 1
                    else:
                        seq.append(y)
                        dicionario[y] = c2[y]
                else:
                    seq.append(y)
            except:
                seq.append(y)
        c1, c2, ignore = ifVerification(x, c1, c2, c3, c4, ignore) # verificação do campo true
        c3, c4, ignore = ifVerification(x, c3, c4, c1, c2, ignore) # verificação do campo false
        x += 1
    if max(seq) >= len(c1) or -1 in seq:  # caso haja um teste que aponte para uma parada adiciona uma parada ao código
        c1.append('parada')
        c2.append(0)
        c3.append('parada')
        c4.append(0)
        if -1 in seq:  # caso haja um parada direto para 0 redefine para o final
            seq.remove(-1)
            seq.append(x)
    return c1, c2, c3, c4, seq, dicionario

def formatt(c1, c2, c3, c4, seq, dicionario):
    """Função que formata o texto da função composta"""
    aux = []
    id_f = 1
    for x in seq:
        if c2[x] <= 0 and c1[x] != 'parada':  # corrige alguns apontamentos de parada
            c2[x] = len(seq)
        if c4[x] <= 0 and c3[x] != 'parada':
            c4[x] = len(seq)
        if c2[x] < len(c1) and c1[x] == 'parada':  # formaliza as paradas em 0
            c2[x] = 0
        if c4[x] < len(c1) and c3[x] == 'parada':
            c4[x] = 0
        if x in dicionario.keys():
            aux.append(id_f)
            aux.append(c1[x])
            aux.append(dicionario[x])
            aux.append(c3[x])
            aux.append(dicionario[x])
        else:
            aux.append(id_f)
            aux.append(c1[x])
            aux.append(c2[x])
            aux.append(c3[x])
            aux.append(c4[x])
        id_f += 1
    return aux

def finiteArrayDefinition(array, n):
    '''Define a Cadeida de Conjuntos Finitos'''
    fullseq = [] # irá conter a sequência dos passos desta verificação
    seq = ['e'] # irá conter a cadeira de conjuntos finitos
    fullseq.extend(seq)
    # encontra a última da parada
    for i in range(int(n + (len(array) / 5) - 1), n - 1, -1):
        # verifica se a instrução possui uma parada
        if (array[2 + (5 * (i - n))] == 0 or array[4 + (5 * (i - n))] == 0):
            limit = array[0 + (5 * (i - n))]
            seq.append(array[0 + (5 * (i - n))])
            fullseq.extend(seq)
            break
    # procura todas as menções à essa instrução e as anteriores
    x = 1
    while (x != 0):
        x = 0
        for i in range(limit - 1, n - 1, -1):
            # verifica se a intrução aponta para a instrução anterior e se ainda não foi inclusa na sequência
            if (array[0 + (5 * (i - n))] not in seq and (array[2 + (5 * (i - n))] in seq or array[4 + (5 * (i - n))] in seq)):
                seq.append(array[0 + (5 * (i - n))])
                fullseq.extend(seq)
                x += 1
    return showSeq(fullseq),seq, limit

def showSeq(fullseq):
    '''Retorna a sequência de instruções formatada'''
    aux = ''
    count = 0
    i = 0
    while(i < len(fullseq)):
        seq = []
        if (fullseq[i] == 'e'):
            seq.append(fullseq[i])
            i += 1
            while (i < len(fullseq) and fullseq[i] != 'e'):
                seq.append(fullseq[i])
                i += 1
            aux += ("A{0}: {1}\n".format(count, seq))
            count+=1
    aux += ("A{0}: {1}\n".format(count, seq))
    return aux

def cycleSimplify(array, limit, n):
    '''Simplificação de Ciclos (caso seja necessário)'''
    # verifica se há alguma instrução fora do limite do programa
    if (limit != int(n + len(array)/5)):
        out_of_bounds = [] # guardará o número das instruções a serem removidas
        for i in range(limit, int(n + len(array) / 5)):
            if (array[4 + (5 * (i - n))] > 0):
                out_of_bounds.append(array[0 + (5 * (i - n))])
            # caso haja o formato (instrução,número),(parada,0), a instrução antes da parada será ignorada
            if (i != limit):
                if (array[2 + (5 * (i - n))] > 0):
                    out_of_bounds.append(array[0 + (5 * (i - n))])
        # remoção das linhas fora do limite
        while (limit != int(n + len(array) / 5)):
            array.pop()
        # substituição das instruções fora do limite por ciclos
        for i in range(n, int(n + len(array) / 5)):
            for j in range(1,3):
                if (array[j*2 + (5 * (i - n))] in out_of_bounds):
                    array[(j*2-1) + (5 * (i - n))] = "ciclo"
                    array[j*2 + (5 * (i - n))] = 'w'
    return array

def textFormat(array):
    '''Transforma o array em uma string para ser exibida'''
    aux = ''
    for i in range(0, int(len(array)/5)):
        aux += ("{0}: ({1},{2}),({3},{4})\n".format(array[0 + (5 * i)], array[1 + (5 * i)], array[2 + (5 * i)], array[3 + (5 * i)], array[4 + (5 * i)]))
    # Adiciona uma instrução de ciclo ao final do programa
    if ('ciclo' in array):
        return aux+("{0}: ({1},{0}),({1},{0})\n".format('w',"ciclo"))
    else:
        return aux

