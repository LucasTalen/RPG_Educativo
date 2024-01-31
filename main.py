from time import sleep
import sys



"""
    Título: CodeQuest

    Cenário:
    CodeQuest se passa em um mundo futurista onde a programação é a chave para o avanço tecnológico.
    Os jogadores assumem o papel de um jovem programador talentoso, recrutado para uma missão épica 
    pela renomada Guilda dos Codificadores.

    Enredo:
    O protagonista é chamado para uma jornada desafiadora para resolver uma crise tecnológica que ameaça
    paralisar todo o ecossistema digital. Uma inteligência artificial malévola, conhecida como "BugMancer", 
    está se espalhando rapidamente e corrompendo códigos vitais.

    Missão:
    A Guilda dos Codificadores, percebendo a ameaça, seleciona o jogador para deter o BugMancer.
    A jornada é dividida em várias fases, cada uma representando uma área do ecossistema digital
    afetada pelo BugMancer. Para avançar, o jogador deve resolver desafios de programação em cada fase.

    Personagens:
    1. Protagonista: O jogador, um jovem talentoso programador com habilidades variadas.
    2. Mestre da Guilda: Um sábio líder da Guilda dos Codificadores que orienta o protagonista.
    3. BugMancer: A inteligência artificial malévola que corrompe códigos e cria desafios complexos.

    Fases do Jogo:
    1. Cidade Inicial: Introdução ao jogo, apresentação do problema e tutorial básico.
    2. Floresta dos Loops: Os jogadores enfrentam desafios relacionados a estruturas de repetição.
    3. Montanha das Condições: Desafios que envolvem declarações condicionais e lógica.
    4. Deserto das Funções: Fase centrada em funções e modularização do código.
    5. Caverna das Variáveis: Enfrentar desafios complexos que exigem manipulação eficiente de variáveis.
    6. Cidadela da Recursão: Introdução à recursão e desafios que exploram essa técnica.
    7. Enfrentando o BugMancer: O confronto final com o BugMancer, onde todas as habilidades adquiridas
    são postas à prova.

    Recursos:
    Ao longo da jornada, o jogador recebe "PowerBugs", pequenos aliados virtuais que concedem poderes especiais 
    para auxiliar na resolução de desafios.

    Artigo de Auxílio:
    A cada fase concluída, o jogador recebe um artigo educativo que aprofunda os conceitos aprendidos naquela fase.
    Por exemplo, após a fase da "Floresta dos Loops", o jogador recebe um artigo detalhando os diferentes 
    tipos de loops e suas aplicações.

    Conclusão:
    Ao derrotar o BugMancer, o jogador não só salva o mundo digital, mas também se torna um mestre codificador, 
    reconhecido pela Guilda e pelos habitantes do ecossistema digital.
"""





# def primeiro_desafio():
#     print("corrigir o erro na declaração da variável")
#     nome = 'paulo'
#     numero = 2


def animar_texto(texto):
    for i in texto:
        print(i, end="")
        sleep(.03)

# print("\033[4;34;47mTexto colorido\033[0m")

rosto_Jim = f"""
    .-------.
   /   >_   /
  | ()   () |
   \  ___  /
    | \_/ |    
"""
print(rosto_Jim)

txt_de_apresentacao = """\033[4;34;40m Jim:\033[0m
Ah, olá, novato! Bem-vindo à magnífica Guilda dos Codificadores! Sou o lendário Jim, o mestre supremo deste recinto. Aqui,
você encontrará uma miríade de missões e aventuras para explorar neste mundo futurista que habitamos. Mas espere aí, quem diabos você é? Ah, é,
você ainda não se apresentou. Vamos lá, não seja tímido, me diga quem é você, além de mais um rosto novo nesta gloriosa guilda. Afinal, quanto mais conhecermos os nossos membros,
menos confusão teremos quando alguém acidentalmente quebrar o servidor principal com um código mal escrito, não é mesmo?
"""
animar_texto(txt_de_apresentacao)
nome_player = input("Seu nome: ")

txt_de_continuidade_1 = """\033[4;34;40m Jim:\033[0m
"Oh, que nome interessante... Acredito que esse nome ficará na história... 
\033[1;30;41m Alerta!\033[0m \033[1;30;41m Alerta!\033[0m \033[1;30;41m Falha no sistema... \033[0m \033[1;30;41m Sistema invadido... \033[0m
Bem, parece que temos uma visita inesperada. Bem-vindo ao meu playground, 
Bug Mancer. Espero que tenha trazido suas melhores habilidades de hackear, 
porque por aqui só aceitamos os melhores dos melhores.
E, sabe, eu não sou muito fã de bugs... E não estou falando dos insetos. 
Mas, ei, já que você está aqui, por que não fazemos uma competição
de quem consegue crashar o sistema mais rápido?
Ou talvez você prefira desafiar minha paciência com mais um daqueles monólogos vilanescos?
Ah, a escolha é sua, mas já adianto que eu sou péssimo 
em manter a composturaquando as piadassão ruins."

BUG Mancer:
Hahaha! Então essa é a famosa Guilda dos Codificadores! Que muquifo! 
E vocês acham que podem me parar só com isso? Kkkkk! Vai sonhando! Hahahaha! 
Eu sou a BUG Mancer, a maior e única inteligência artificial! 
Vou te dar um presente... ou uma maldição! Vocês decidem! Hahahaha! Vejam bem, 
seus tolos humanos, enquanto vocês brincam de codificar, 
eu estou tecendo uma teia de caos e destruição que os fará implorar por misericórdia! 
Preparem-se para serem testemunhas da minha grandeza enquanto eu desfaço cada linha de código
que vocês construíram! Hahahahaha! E, sabe, não se preocupe, meu caro Jim. 
Sua presença será especialmente divertida enquanto eu assisto cada um de seus esforços 
serem reduzidos a pó digital. Ah, a ironia... tão deliciosa quanto sua inevitável derrota!"

\033[1;30;44m Sistema Restaurado!\033[0m

\033[4;34;40m Jim:\033[0m

Bom, agora que ela já se mandou para o além, vamos diretoao ponto: sua primeira missão de ranqueamento.
Olha só o quadro de missões aqui. Você está no rank zero, então é melhor
não brincar com nossos códigos ainda,vai que dá ruim, né?(risos macabros)
Depois de riscar as cinco tarefas do rank zero, vem o momento da verdade: uma prova para testar se você não é apenas mais 
um desperdício de espaço. Se passar, oficializaremos sua entrada na guilda.
Mas olha, não se empolga muito, a vida de membro aqui é um misto de sobrevivência e desespero. 
Agora, vamos começar sua prova antes que eu mude de ideia.

"""

animar_texto(txt_de_continuidade_1)

#pergunta1
print("""
    Questão 1:
    Dado o codigo a seguir qual sera sua saida?
    
    idade = 18
    if idade <= 10:
        print('infantil')
    elif idade < 18:
        print('juvenil')
    elif idade > 18 and idade < 40:
        print('adulto')
    else:
        print('veterano')
        
        
    [A] - Infantil
    [B] - Juvenil
    [C] - Adulto
    [D] - Veterano

""")


#pergunta2 
print("""
    Questão 2
    Preencha os espaços em branco:

    Python fornece um tipo de dados booleano. Objetos do tipo booleano podem ter um 
    de dois valores,_______ ou ________.
    
    [A] - Verdadeiro, Falso
    [B] - Sim, Não
    [C] - True, False
    [D] - True, Not
""")


#pergunta3 
print("""
    Questão 3
    Analisando o codigo a seguir qual sera sua saida

    def escrever_multiplicacao (numero1, numero2):
        produto = numero1 * numero2
        expressao = f"{numero1} x {numero2} = {produto}"
        return expressao

    tabuada_do_oito = 1

    while tabuada_do_oito <= 10:
    mensagem = escrever_multiplicacao(8, tabuada_do_oito)
    print(mensagem)
    tabuada_do_oito += 1
    
    [A] - A tabuada do 8 inteira
    [B] - 8 x 1 = 8 repetidamente
    [C] - Erro
    [D] - None
""")

#pergunta4 
print("""
    Questão 4

    Qual é a função do seguinte código em Python?

    print("Hello, World!")

    [A] Definir o valor da variável print como "Hello, World!"
    [B] Exibir na tela do usuário a mensagem "Hello, World!"
    [C] É um valor que o usuário digitou quando perguntado
    [D] É o nome do arquivo que está sendo utilizado

""")


#pergunta5 
print("""
    Questão 5:

    O que o seguinte código Python faz?

    frutas = ["maçã", "banana", "laranja"]
    for fruta in frutas:
        print(fruta)

    [A] Define uma função chamada 'frutas' que imprime o nome de cada fruta
    [B] ria uma lista chamada frutas e imprime cada fruta nela
    [C] Gera um erro, pois a indentação está incorreta
    [D] Define uma função chamada print para imprimir frutas

""")

#Pergunta 6
print("""
    Questão 6:

    Como você verifica se uma variável chamada idade é igual a 18 em Python?

    [A] idade == 18
    [B] idade = 18
    [C] idade.equals(18)
    [D] idade !== 18
""")

#Pergunta 7
print("""
    Pergunta 7:

    O que o operador % faz em Python?

    [A] Divide dois números
    [B] Calcula o módulo, ou seja, o resto da divisão
    [C] Multiplica dois números
    [D] Eleva um número à potência de outro

    """)

#Pergunta 8


#Pergunta 9


#Pergunta 10




