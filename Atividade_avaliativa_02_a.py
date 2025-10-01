start_campos =

while start_campos:
    match campo:
        case 1:
            try: 
                nome = str(input("Digite nome "))
                campo += 1
            except:
                print("valor nome invalido")
        case 2:
            try:
                idade = int(input("Digite idade "))
                campo += 1
            except:
                print("valor idade invalido")
        case 3:
            try:
                peso = float(input("Digite peso "))
                start_campos = False
            except:
                print("valor peso invalido")

else:
    print("Seu nome e: ", Nome)

    print("Sua idade e:", Idade)
    
    print("Seu peso e:", Peso)


        