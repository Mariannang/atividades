#Um grupo de profissionais da saude calculam o IMC de seus pacientes utilizando o site da UNIMED. Porem, a empresa, possui muitos problemas com instabilidade de internet.
#Cabera a voce como programador Python criar um programa que calcule o IMC do usuario baseado no site da UNIMED:
#Obs: Lembre-se de que o resultado do programa devera retornar o nome do cliente,idade, peso, valor do IMC e Classificacao.

#### receber os dados
#receber o nome do cliente
Nome = str(input("Digite seu nome "))

#receber idade
try:
 Idade = int(input("Digite sua idade "))
except:
   print("Valor invalido!")


#receber peso
try:
 Peso = int(input("DIgite seu peso "))
except: 
print("valor invalido!")


#receber altura
Altura = float(input("DIgite sua altura "))

###processo de dados
# calcular IMC
# IMC = peso / altura
imc = Peso / (Altura * Altura)
#verificar se a idade e maior ou igual a 20 e menor que 61
#verificar a tabela e classificar 
if Idade > 20 and Idade < 61:
    if imc < 18.5:
        classificacao = "Baixo peso"
    elif imc > 18.5 and imc <= 24.99
    classificacao = "normal"
    elif imc >= 25 and imc <= 29.99
 classificacao = "Sobrepeso"
 else:
 classificacao = "Obeso"
 elif idade > 60:
 if imc < 22:
    classificacao = "baixo peso"
 elif imc >= 22 and imc <= 27:
    elif imc > 27 and imc < 29.99
 classificacao = "sobrepeso"
else:
classificacao = "obeso"

#devolver os dados
print("Seu nome e: ", Nome)
print("Sua idade e:", Idade)
print("Seu peso e:", Peso)
print("sua altura e: ", Altura)
print("Seu IMC e: ", imc)

