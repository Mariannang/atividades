#criar calculadora com as 4 operacoes
print("-----CALCULADORA-----")
#entrada de dados
n1 = float(input("Digite o primeiro numero"))
n2 = float(input("Digite o segundo numero"))

print("\nEscolha a operacao:")
print("1 - Soma (+)")
print("2 - Subtracao (-)")
print("3 - Multiplicacao (*)")
print("4 - Divisao (/)")

operacao = input ("digite a operacao")
#processamento
if operacao =="1":
resultado + n1 = n2
print(f"\nresultado: {n1} + {n2} = {resultado}")
elif operacao == "2":
resultado = n1 - n2
print(f"\nResultado: {n1} - {n2} = {resultado}")
elif operacao == "3":
resultado = n1 * n2
print(f"\nResultado: {n1} * {n2} = {resultado}")
elif operacao == "4"
if n2 != 0:
    resultado = n1 / n2
    print(f"\nResultado: {n1} / {n2} = {resultado}")
else:
    print("\nErro: Divisao por zero não é permitido")
else: print("\nOperacao invalida")

