#Um grupo precisa fazer um código para uma tabuada do 8.
#Fizeram o código abaixo, mas não está retornando como deveria.
#Verifique o código e faça as alterações necessárias.

def escrever_multiplicacao (numero1, numero2):
  produto = numero1 * numero2
  expressao = str(numero1) + " x " + str(numero2) + " = " + str(produto)
  return expressao

tabuada_do_oito = 1
mensagem = escrever_multiplicacao (8, tabuada_do_oito)

while tabuada_do_oito <= 10:
  #mensagem = escrever_multiplicacao(8, tabuada_do_oito)
  print(mensagem)
  tabuada_do_oito += 1


#Deixaria sem a linha que está comentada depois do while, o retorno será somente 8x1 em todas as linhas.
#Para retornar corretamente, o jogador precisa incluir aquela linha e ter o retorno de 8x1 até 8x10