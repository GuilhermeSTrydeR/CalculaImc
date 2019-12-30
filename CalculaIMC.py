#calcula IMC (indice de massa corporal)

#o valor da altura é recebido em centimetros
altura = int(input("digite sua altura em centimetros: "))
# o valor em centimetros é convertido em metros
altura = (altura / 100)

# o peso é recebido em quilogramas
peso = float(input("digite seu peso em quilogramas: "))

# nessa parte é feito o calculo de IMC
imc = (peso / (altura * altura))

# esse bloco abaixo define a descrção do IMC
if(imc < 18.5):
  desc = ("Abaixo do Peso")

if(imc >= 18.5 and imc < 30):
  desc = ("Peso Normal")

if(imc >= 25 and imc < 30):
  desc = ("Sobrepeso")

if(imc >= 30 and imc < 35):
  desc = ("Obesidade Grau 1")

if(imc >= 35 and imc < 40):
  desc = ("Obesidade Grau 2")

if(imc >= 40):
  desc = ("Obesidade Grau 3 ou Mórbida")

print("\n"+"IMC: %2.2f - %s" % (imc, desc))

input("\nAperte qualquer cecla para continuar")


