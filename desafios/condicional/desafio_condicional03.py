# para saber se a categoria é E o peso bruto precisa ser maior que 6001. e se for necessário incluir
# esse valor para categoria E, como posso corrigir o código.


quantidade_rodas = int(input("Informe a quantidade de rodas do veículo: "))
peso_bruto = float(input("Informe o peso bruto do veículo em quilogramas: "))
quantidade_pessoas = int(input("Informe a quantidade de pessoas no veículo: "))

if quantidade_rodas == 2 or quantidade_rodas == 3:
    categoria = "Categoria A"
elif quantidade_rodas == 4 and quantidade_pessoas <= 8 and peso_bruto <= 3500:
    categoria = "Categoria B"
elif quantidade_rodas >= 4 and 3500 < peso_bruto <= 6000:
    categoria = "Categoria C"
elif quantidade_rodas >= 4 and quantidade_pessoas > 8:
    categoria = "Categoria D"
elif quantidade_rodas >= 4 and peso_bruto > 6001:
    categoria = "Categoria E"
else:
    categoria = "Categoria não determinada"

print(f"A categoria de habilitação recomendada para este veículo é: {categoria}")
