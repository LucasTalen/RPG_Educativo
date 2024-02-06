def achar_elemento(array, elemento):
  
  tamanho = len(array)
  
  for i in range(tamanho):
    if array[i] == elemento:

        print(f"O Nome {elemento} esta no Array")
        
        
  else:
    print(f"O nome {elemento} Não está no Aarry")

nomes = ["ana", "joao", "maria", "paulo"]

achar_elemento(nomes, "ana")