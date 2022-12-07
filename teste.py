from conversor_numerico import Conversor_Numerico
from Binario_sinais import Sinais_Binario

while True:
    entrada = input("Digite: ")
    if entrada == "fim":
        print("Ótimo teste mano!")
        break
    print(Sinais_Binario.complemento_2_inteiro_binario(entrada))