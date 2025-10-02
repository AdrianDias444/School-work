print("====== Calculadora de IMC ======")

altura_cm = float(input("Insira sua altura em cm: "))
peso_kg = float(input("Insira seu peso em kg: "))

altura_m = altura_cm / 100

imc = peso_kg / (altura_m * altura_m)

if imc < 19:
    classificacao = "Magreza"
if 19 < imc < 25:
    classificacao = "Normal"
else:
    classificacao = "Obeso"

print("Seu IMC é", imc, "Sua classificação é -", classificacao)
