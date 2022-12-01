class Conversor_Numerico:

    def decimal_binario(valor, tipo=int):
        if type(valor) != int:
            raise Exception("Essa função apenas funciona com valores inteiros, você pode usar ")##Não se esqueça de atualizar essa linha
        elif valor < 0:
            raise Exception("Essa função não funciona com valores negativos, você pode usar ")##Não se esqueça de atualizar essa linha
        elif valor == 0:
            return 0

        restos = []
        sequencia_retornada = ''
        while valor >= 1:
            resto = valor % 2
            restos.append(str(resto))
            valor //= 2
        for i in range(len(restos)-1,-1,-1):
            sequencia_retornada += restos[i]
        if tipo == str:
            return sequencia_retornada
        elif tipo == int:
            return int(sequencia_retornada)
        elif tipo == float:
            raise Exception("Essa função não funciona com valores em ponto flutuante, você pode usar ")##Não se esqueça de atualizar essa linha
        else:
            return int(sequencia_retornada)

###

    def decimal_octal(valor):
        if type(valor) != int:
            raise Exception("Essa função apenas funciona com valores inteiros, você pode usar ")##Não se esqueça de atualizar essa linha
        elif valor == 0:
            return 0
        elif valor < 0:
            sinal = -1
            valor = abs(valor)
        else:
            sinal = 1
        restos = []
        sequencia_retornada = ''
        while valor >= 1:
            resto = valor % 8
            restos.append(str(resto))
            valor //= 8
        for i in range(len(restos)-1,-1,-1):
            sequencia_retornada += restos[i]
        return int(sequencia_retornada) * sinal

###

    def decimal_hexadecimal(valor):
        tradutor = {0:'0',1:'1', 2:'2', 3:'3', 4:'4', 5:'5',6:'6', 7:'7', 8:'8', 9:'9', 10:'A',11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
        if type(valor) != int:
            raise Exception("Essa função apenas funciona com valores inteiros, você pode usar ")##Não se esqueça de atualizar essa linha
        elif valor == 0:
            return 0
        elif valor < 0:
            sinal = True
            valor = abs(valor)
        else:
            sinal = False
        valor = int(valor)
        restos = []
        sequencia_retornada = ''
        while valor >= 1:
            resto = valor % 16
            restos.append(tradutor.get(resto))
            valor //= 16
        for i in range(len(restos)-1,-1,-1):
            sequencia_retornada += restos[i]
        if sinal:
            return f'-{sequencia_retornada}'
        return sequencia_retornada
        
###

    def binario_decimal(valor, tipo=int):

        if type(valor) != int and type(valor) != str:
            raise Exception("Tipo de variável não aceito para essa função!")
        elif type(valor) == int:
            valor = str(valor)
        for a in valor:
            if a != '1' and a != '0':
                raise Exception("Essa função só aceita números binários!")
        expoente = 0
        soma = 0
        for i in range(len(valor)-1,-1,-1):
            soma += int(valor[i])*2**expoente
            expoente += 1
        if tipo == int:
            return soma
        elif tipo == str:
            return str(soma)
        else:
            return soma

###

    def binario_octal(valor, tipo=int):
        if type(valor) != int and type(valor) != str:
            raise Exception("Tipo de variável não aceito para essa função!")
        elif type(valor) == int:
            valor = str(valor)
        for a in valor:
            if a != '1' and a != '0':
                raise Exception("Essa função só aceita números binários!")
        valor = list(valor)
        while len(valor) % 3 != 0:
            valor.insert(0,'0')
        conversor = ''
        for i in range(0,len(valor),3):
            expoente = 2
            soma = 0
            for a in range(3):
                soma += int(valor[a+i])*2**expoente
                expoente -= 1
            conversor += str(soma)
        if tipo == str:
            return conversor
        else:
            return int(conversor)

###

    def binario_hexadecimal(valor, tipo=int):
        tradutor = {0:'0',1:'1', 2:'2', 3:'3', 4:'4', 5:'5',6:'6', 7:'7', 8:'8', 9:'9', 10:'A',11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
        if type(valor) != int and type(valor) != str:
            raise Exception("Tipo de variável não aceito para essa função!")
        elif type(valor) == int:
            valor = str(valor)
        for a in valor:
            if a != '1' and a != '0':
                raise Exception("Essa função só aceita números binários!")
        valor = list(valor)
        while len(valor) % 4 != 0:
            valor.insert(0,'0')
        conversor = ''
        for i in range(0,len(valor),4):
            expoente = 3
            soma = 0
            for a in range(4):
                soma += int(valor[a+i])*2**expoente
                expoente -= 1
            conversor += tradutor.get(soma)
        return conversor

###

    def octal_decimal(valor):
        valores = ['0', '1', '2', '3', '4', '5', '6', '7']
        if type(valor) != int and type(valor) != str:
            raise Exception("Essa Função apenas funciona com integrais e strings, caso esteja buscando valores em ponto flutuante favor buscar em  ") ### Não esqueça de completar a linha!
        if type(valor) == int:
            if valor < 0:
                sinal = -1
            else:
                sinal = 1
            valor = str(valor)
        else:
            if valor[0] == '-':
                sinal = -1
            else:
                sinal = 1
        for caractere in valor:
            if caractere not in valores:
                raise Exception("Essa função apenas funciona com números em sistema octal")
        
        expoente = 0
        soma = 0
        for a in range(len(valor)-1,-1,-1):
            try:
                soma += int(valor[a])*8**expoente
                expoente+=1
            except ValueError:
                #Caso exista o sinal '-' na string!
                pass
        return soma * sinal

###

    def octal_binario(valor):
        valores = ['0', '1', '2', '3', '4', '5', '6', '7']
        if type(valor) != int and type(valor) != str:
            raise Exception("Essa Função apenas funciona com integrais e strings, caso esteja buscando valores em ponto flutuante favor buscar em  ") ### Não esqueça de completar a linha!
        if type(valor) == int:
            if valor < 0:
                raise Exception("Essa Função converte binários em sua forma padrão, sem conversão de sinal!")
            valor = str(valor)
        else:
            if valor[0] == '-':
                raise Exception("Essa Função converte binários em sua forma padrão, sem conversão de sinal!")
        for caractere in valor:
            if caractere not in valores:
                raise Exception("Essa função apenas funciona com números em sistema octal")
        convertido = ''
        for numero in valor:
            numero = int(numero)
            restos = []
            if 4 > numero >= 2:
                convertido += '0'
            elif numero == 1:
                convertido += '00'
            elif numero == 0:
                convertido += '000'
            while numero >= 1:
                resto = numero % 2
                restos.append(str(resto))
                numero //= 2
            for i in range(len(restos)-1,-1,-1):
                convertido += restos[i]
        return convertido

###

    def octal_hexadecimal(valor):
        tradutor = {0:'0',1:'1', 2:'2', 3:'3', 4:'4', 5:'5',6:'6', 7:'7', 8:'8', 9:'9', 10:'A',11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
        valores = ['0', '1', '2', '3', '4', '5', '6', '7']
        if type(valor) != int and type(valor) != str:
            raise Exception("Essa Função apenas funciona com integrais e strings, caso esteja buscando valores em ponto flutuante favor buscar em  ") ### Não esqueça de completar a linha!
        if type(valor) == int:
            if valor < 0:
                raise Exception("Essa Função converte binários em sua forma padrão, sem conversão de sinal!")
            valor = str(valor)
        else:
            if valor[0] == '-':
                raise Exception("Essa Função converte binários em sua forma padrão, sem conversão de sinal!")
        for caractere in valor:
            if caractere not in valores:
                raise Exception("Essa função apenas funciona com números em sistema octal")
        convertido = ''
        for numero in valor:
            numero = int(numero)
            restos = []
            if 4 > numero >= 2:
                convertido += '0'
            elif numero == 1:
                convertido += '00'
            elif numero == 0:
                convertido += '000'
            while numero >= 1:
                resto = numero % 2
                restos.append(str(resto))
                numero //= 2
            for i in range(len(restos)-1,-1,-1):
                convertido += restos[i]
            
        conversao = list(convertido)
        while len(conversao) % 4 != 0:
            conversao.insert(0,'0')
        conversor = ''
        for i in range(0,len(conversao),4):
            expoente = 3
            soma = 0
            for a in range(4):
                soma += int(conversao[a+i])*2**expoente
                expoente -= 1
            conversor += tradutor.get(soma)
        return conversor

###

    def hexadecimal_decimal(valor, tipo=int):
        tradutor = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
        caracteres = ['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
        if type(valor) != str:
            raise Exception("Essa Função apenas funciona com strings") ### Não esqueça de completar a linha!
        if valor[0] == '-':
            sinal = -1
            valor = list(valor)
            valor.pop(0)
        else:
            sinal = 1
        for caractere in valor:
            if caractere not in caracteres:
                raise Exception("Essa função apenas funciona com números em Hexadecimal")
        expoente = 0
        soma = 0
        for a in range(len(valor)-1,-1,-1):
            soma += tradutor.get(valor[a])*16**expoente
            expoente += 1
        soma *= sinal
        if tipo == str:
            return str(soma)
        else:
            return soma

###

    def hexadecimal_binario(valor):
        tradutor = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
        caracteres = ['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
        if type(valor) != str:
            raise Exception("Essa Função apenas funciona com strings") ### Não esqueça de completar a linha!
        if valor[0] == '-':
            raise Exception("Essa Função converte binários em sua forma padrão, sem conversão de sinal!")
        for caractere in valor:
            if caractere not in caracteres:
                raise Exception("Essa função apenas funciona com números em Hexadecimal")
        convertido = ''
        for numero in valor:
            numero = tradutor.get(numero)
            restos = []
            if 8 > numero >= 4:
                convertido += '0'
            elif 4 > numero >= 2:
                convertido += '00'
            elif numero == 1:
                convertido += '000'
            elif numero == 0:
                convertido += '0000'
            while numero >= 1:
                resto = numero % 2
                restos.append(str(resto))
                numero //= 2
            for i in range(len(restos)-1,-1,-1):
                convertido += restos[i]
        return convertido

###

    def hexadecimal_octal(valor):
        tradutor = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
        caracteres = ['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
        if type(valor) != str:
            raise Exception("Essa Função apenas funciona com strings") ### Não esqueça de completar a linha!
        if valor[0] == '-':
            raise Exception("Essa Função converte binários em sua forma padrão, sem conversão de sinal!")
        for caractere in valor:
            if caractere not in caracteres:
                raise Exception("Essa função apenas funciona com números em Hexadecimal")
        convertido = ''
        for numero in valor:
            numero = tradutor.get(numero)
            restos = []
            if 8 > numero >= 4:
                convertido += '0'
            elif 4 > numero >= 2:
                convertido += '00'
            elif numero == 1:
                convertido += '000'
            elif numero == 0:
                convertido += '0000'
            while numero >= 1:
                resto = numero % 2
                restos.append(str(resto))
                numero //= 2
            for i in range(len(restos)-1,-1,-1):
                convertido += restos[i]
        convertido = list(convertido)
        while len(convertido) % 3 != 0:
            convertido.insert(0,'0')
        conversor = ''
        for i in range(0,len(convertido),3):
            expoente = 2
            soma = 0
            for a in range(3):
                soma += int(convertido[a+i])*2**expoente
                expoente -= 1
            conversor += str(soma)
        return conversor