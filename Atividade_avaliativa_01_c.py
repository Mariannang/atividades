#criar calculadora com as 4 operacoes
start_programa = True
recebe_campos = True
campo = 1
print("-----CALCULADORA-----")
while start_programa:
    while recebe_campos:
         match campo:
            case 1:
                try:
                    #entrada de dados
                    n1 = float(input("Digite o primeiro numero"))
                    campo += 1
                except:
                        print("Valor invalido...")

            case 2:
                try:
                    n2 = float(input("Digite o segundo numero"))
                    campo += 1
                except:
                        print("Valor invalido...")
            case 3:
                try:
                    print("\nEscolha a operacao:")
                    print("1 - Soma (+)")
                    print("2 - Subtracao (-)")
                    print("3 - Multiplicacao (*)")
                    print("4 - Divisao (/)")

                    operacao = str(input ("digite a operacao"))
                    recebe_campos = false
                except:
                    print("Valor invalido...")

    else:

#processamento
            if operacao =="1":
              resultado = n1 + n2
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
    
                print("\nErro: Divisao por zero não é permitido")
else: print("\nOperacao invalida")

fim_programa = True
while fim_programa:
    print("\nDeseja finalizar o programa?\n")
    try:
        confirma = str(input("Digite S (SIM) ou N (calcule novamente): "))
        if confirma == "s" or confirma "S":
        fim_programa = False
        start_programa = False
        if confirma == "n" or confirma "N":
            fim_programa = False
            recebe_campos = True
            campo = 1
            except:
                print("Operacao invalida...")
else:
    print("\n----------------CONCLUIDO-----------------\n")


