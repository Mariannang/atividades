#calcule o raio de uma circuferencia
import math # para usar o valor de PI
print("-----Calculo do raio da circuferencia-----\n")
#entrada de usuario
circuferencia = float(input("Digite o valor da circuferencia (C);"))
#calcule o raio
raio = circuferencia / (2 * math.pi)
#saida formatada
print(f"O raio da circuferencia é: {raio:.2f}")