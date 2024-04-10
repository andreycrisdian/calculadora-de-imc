

#Seu Índice de Massa Corporal (IMC) é: 22.86
#Categoria de Peso: Peso Normal

#MC < 18.5: Abaixo do Peso
#18.5 <= IMC < 25: Peso Normal
#25 <= IMC < 30: Sobrepeso
#30 <= IMC: Obeso

print("Bem-vindo à Calculadora de Índice de Massa Corporal (IMC)!")

weigth = float(input("Por favor, insira seu peso (em kg): "))

heigth = float(input("Agora, insira sua altura (em metros): "))


imc = weigth/(heigth * heigth)

if imc < 18.5:
    print("Seu Índice de Massa Corporal (IMC) é: " + str(imc))
    print("Categoria de Peso: Abaixo do peso")

elif imc >= 18.5 and imc < 25:
    print("Seu Índice de Massa Corporal (IMC) é: " + str(imc))
    print("Categoria de Peso: Peso Normal")

elif  imc >= 25 and imc < 30:
    print("Seu Índice de Massa Corporal (IMC) é: " + str(imc))
    print("Categoria de Peso: Sobrepeso")

else:
    print("Seu Índice de Massa Corporal (IMC) é: " + str(imc))
    print("Categoria de Peso: Obeso")
