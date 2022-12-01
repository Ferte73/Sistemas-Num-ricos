from conversor_numerico import Conversor_Numerico

while True:
    entrada = input("Digite: ").upper()
    if entrada == "fim":
        print("Ótimo teste mano!")
        break
    print(Conversor_Numerico.hexadecimal_octal(entrada))