start_campos = True
start_programa = True
campo = 1

while start_programa:
    while start_campos:

        match campo:
            case 1:
                try:
                    nome = str(input("DIgite seu nome: "))
                    campo += 1 
                except:
                        print("Valor nome invalido...")
            case 2:
                try:
                     idade = int(input("DIgite sua idade: "))
                     campo += 1
                except:
                         print("Idade invalida...")
            case 3:
                try:
                    peso =  float(input("DIgite seu peso:"))
                    start_campos = False
                except:
                        print("Peso invalido...")
    else:
                    print("Seu nome é ", nome)

                    print("Sua idade é ", idade, "anos.")

                    print("Seu peso é ", peso, "KG.")     

                    fim_programa = True
                    while fim_programa:
                        print("\nDeseja fializar o programa?\n")
                        try:
                            Confirma = str(input("DIgite S (SIM) ou N (não): "))
                            if Confirma == "S" or Confirma == "s":
                                fim_programa = False
                                start_programa = False
                            elif Confirma == "N" or Confirma == "n":
                                fim_programa = False
                                star_campos = True
                                campo = 1
                            else:
                                print("Valor invalido...")

                        except:
                                print("Campo invalido...")                               
else:
    print("\n--------------------CONCLUIDO--------------------\n")
