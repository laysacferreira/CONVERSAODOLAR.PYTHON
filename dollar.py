import os

dollar = float(input("Digite o valor do dólar: "))
reais = float(input("Digite o valor em reais: "))

dolares = reais / dollar

print("Valor convertido em dólar:", round(dolares, 2))