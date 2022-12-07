from conversor_numerico import Conversor_Numerico

class Sinais_Binario:
    
    def sinal_magnitude_inteiro_binario(valor):
        if type(valor) != str and type(valor) != int:
            raise Exception()
        elif type(valor) == str:
            try:
                valor = int(valor)
            except:
                raise Exception()
        if not 127 >= valor >= -127:
            raise Exception()
        if valor < 0:
            sinal = '1'
            valor = abs(valor)
        else:
            sinal = '0'
        

        convertido = Conversor_Numerico.decimal_binario(valor, str)
        while len(convertido) < 7:
            convertido = '0' + convertido
        convertido = sinal + convertido
        return convertido

    def sinal_magnitude_binario_inteiro(valor):
        if type(valor) != str and type(valor) != int:
            raise Exception()
        elif type(valor) == int:
            valor = str(valor)
        for letra in valor:
            if letra != '1' and letra != '0':
                raise Exception()
        if len(valor) > 8:
            raise Exception()
        elif len(valor) == 1:
            raise Exception()
        
        if valor[0] == '0':
            sinal = 1
        else:
            sinal = -1
        
        expoente = 0
        soma = 0
        for i in range(len(valor)-1,0,-1):
            soma += int(valor[i]) * 2 ** expoente
            expoente += 1
        
        return soma * sinal

    def complemento_1_inteiro_binario(valor):
        if type(valor) != str and type(valor) != int:
            raise Exception()
        elif type(valor) == str:
            try:
                valor = int(valor)
            except:
                raise Exception()
        if not 127 >= valor >= -127:
            raise Exception()
        if valor < 0:
            negativo = True
            valor = abs(valor)
        else:
            negativo = False
        
        convertido = Conversor_Numerico.decimal_binario(valor, str)
        while len(convertido) < 8:
            convertido = '0' + convertido

        if negativo:
            conversao = ''
            for letra in convertido:
                if letra == '1':
                    conversao += '0'
                else:
                    conversao += '1'
            return conversao

        return convertido

    def complemento_1_binario_inteiro(valor):
        if type(valor) != str and type(valor) != int:
            raise Exception()
        elif type(valor) == int:
            valor = str(valor)
        for letra in valor:
            if letra != '1' and letra != '0':
                raise Exception()
        if len(valor) > 8:
            raise Exception()
        if valor[0] == '1':
            negativo = True
        else:
            negativo = False
        
        if negativo:
            convertido = ''
            for letra in valor:
                if letra == '1':
                    convertido += '0'
                else:
                    convertido += '1'
        else:
            convertido = valor
        
        expoente = 0
        soma = 0
        for i in range(len(convertido)-1,0,-1):
            soma += int(convertido[i])*2**expoente
            expoente += 1
        
        return soma
    
    def complemento_2_inteiro_binario(valor):
        if type(valor) != str and type(valor) != int:
            raise Exception()
        elif type(valor) == str:
            try:
                valor = int(valor)
            except:
                raise Exception()
        if not 127 >= valor >= -128:
            raise Exception()
        if valor < 0:
            negativo = True
            valor = abs(valor)
        else:
            negativo = False
        
        convertido = Conversor_Numerico.decimal_binario(valor, str)
        while len(convertido) < 8:
            convertido = '0' + convertido
        
        if negativo:
            indice = 7
            conversao = ''
            for i in range(7,-1,-1):
                if convertido[i] == '1':
                    indice = i
                    break
            for j in range(indice,-1,-1):
                if convertido[j] == '1':
                    conversao += '0'
                else:
                    conversao += '1'
            for k in range(7, indice, -1):
                conversao += '0'
            return conversao
        return convertido
