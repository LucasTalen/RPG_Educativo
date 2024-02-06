from time import sleep
import sys
import subprocess










#variaveis globais

rosto_Jim = f"""

    .-------.
   /   >_   /
  | ()   () |
   \  ___  /
    | \_/ |    
"""
txt_de_apresentacao = """\033[4;34;40m Jim:\033[0m
Ah, olá, novato! Bem-vindo à magnífica Guilda dos Codificadores! Sou o lendário Jim, o mestre supremo deste recinto. Aqui,
você encontrará uma miríade de missões e aventuras para explorar neste mundo futurista que habitamos. Mas espere aí, quem diabos você é? Ah, é,
você ainda não se apresentou. Vamos lá, não seja tímido, me diga quem é você, além de mais um rosto novo nesta gloriosa guilda. Afinal, quanto mais conhecermos os nossos membros,
menos confusão teremos quando alguém acidentalmente quebrar o servidor principal com um código mal escrito, não é mesmo?
"""
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
Depois de riscar as dez tarefas do rank zero, vem o momento da verdade: uma prova para testar se você não é apenas mais 
um desperdício de espaço. Se passar, oficializaremos sua entrada na guilda.
Mas olha, não se empolga muito, a vida de membro aqui é um misto de sobrevivência e desespero. 
Agora, vamos começar sua prova antes que eu mude de ideia e lembre \033[1;30;41m qualquer tentativa de comédia na prova resultará em questões descansando eternamente no limbo das anulações.\033[0m

"""
fala_que_vai_verificar_a_prova = """\033[4;34;40m Jim:\033[0m

Hmm, então vamos ver como você se saiu. Será que é apenas mais um aspirante a programador 
de meia dúzia de meses ou se realmente tem o que é preciso para entrar nessa grandiosa guilda dos codificadores?
"""
texto_reprovou_na_prova = """
Ah, então você não conseguiu nem responder uma prova tão pífia. Normalmente, 
eu te chutaria logo para fora desta guilda; você não é digno de estar aqui. 
Mas como recebemos uma visita inesperada, quero ver o que o destino reserva para nós. 
Vá revisar sua prova naquele cantinho ali da sala e, quando aprender que programação 
não é brincadeira, volte e tente novamente.

Enfim, aqui está a explicação de cada questão da prova
    
"""
texto_passou_na_prova = """
Hahaha, nem tão inútil assim, pelo visto! Conseguiu passar nessa provinha que eu mesmo inventei. 
Parabéns, agora você é oficialmente parte dessa grandiosa guilda. Incrível, né? 
Haha, pode rir ou chorar, tanto faz. Bom, como membro oficial, você tem o 'privilégio' de acessar 
o quadro de missões e seu ranking atual é o sublime rank 1.

 Hora de afundar ou nadar, novato! Como de praxe, os calouros têm o 'privilégio' de resolver um 
bug de código para mostrar que não foram aprovados por pura sorte, haha! Então, novato, está 
pronto para o desafio? Haha, quem se importa, você vai ter que lidar com isso de qualquer forma. 
Aqui está o seu primeiro pesadelo para resolver: nossa função de verificação de pessoas está mais confusa 
do que um delírio de um lunático. Em vez de um valor correto, ela entrega dois. 
Agora prove que não é só um azarado que passou na prova por acidente."

"""
nota_da_prova = 0

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

def animar_texto(texto):
    for i in texto:
        print(i, end="")
        sys.stdout.flush()
        #sleep(.03)
        
def abrir_editor(editor,arquivo):
    subprocess.run([editor,arquivo])
    input("Após a edição aperte ENTER para continuar.")
    
    
def ler_arquivo_de_desafio(nome_do_desafio):
    with open(f'./desafios/{nome_do_desafio}', 'r') as desafio:
        return desafio.read()

def executar_desafio(nome_do_desafio): 
    return subprocess.run(['python', f'desafios/{nome_do_desafio}'],capture_output=True, text=True)

def verificar_resultado_do_desafio(resultado,saida_esperada):
    print("---")
    print(resultado)
    match resultado.returncode:
        case 0:
            #O codigo foi executado corretamente. Agora tem que verificar se a saida é o resultado esperado do desafio.
            print("def--" + resultado.stdout == saida_esperada)
            if resultado.stdout == saida_esperada:
                return True
            return False
        case 1:
            print("O codigo não rodou") 
            #O codigo não foi executado por erro do codigo 
            
        case _:
            ...
            #Erros inesperados
    return False

print(rosto_Jim)


animar_texto(txt_de_apresentacao)
nome_player = input("Seu nome: ")

animar_texto(txt_de_continuidade_1)


#pergunta1
print("""
    Questão 1:
    Dado o código a seguir, qual será a sua saída?
    
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
questao_1 = input("Digite sua resposta: ")
if questao_1.upper() == "D":
    nota_da_prova += 1

#pergunta2 
print("""
    Questão 2
    Preencha os espaços em branco:

    Python fornece um tipo de dado booleano. Objetos do tipo booleano podem ter um 
    de dois valores,_______ ou ________.
    
    [A] - Verdadeiro, Falso
    [B] - Sim, Não
    [C] - True, False
    [D] - True, Not
""")
questao_2 = input("Digite sua resposta: ")
if questao_2.upper() == "C":
    nota_da_prova += 1

#pergunta3 
print("""
    Questão 3
    Analisando o código a seguir, qual será a sua saida?

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
questao_3 = input("Digite sua resposta: ")
if questao_3.upper() == "A":
    nota_da_prova += 1

#pergunta4 
print("""
    Questão 4

    Qual é a função do seguinte código em Python?

    print("Hello, World!")

    [A] - Definir o valor da variável print como "Hello, World!"
    [B] - Exibir na tela do usuário a mensagem "Hello, World!"
    [C] - É um valor que o usuário digitou quando perguntado
    [D] - É o nome do arquivo que está sendo utilizado

""")
questao_4 = input("Digite sua resposta: ")
if questao_4.upper() == "B":
    nota_da_prova += 1

#pergunta5 
print("""
    Questão 5:

    O que o seguinte código Python faz?

    frutas = ["maçã", "banana", "laranja"]
    for fruta in frutas:
        print(fruta)

    [A] - Define uma função chamada 'frutas' que imprime o nome de cada fruta
    [B] - Cria uma lista chamada frutas e imprime cada fruta nela
    [C] - Gera um erro, pois a indentação está incorreta
    [D] - Define uma função chamada print para imprimir frutas

""")
questao_5 = input("Digite sua resposta: ")
if questao_5.upper() == "B":
    nota_da_prova += 1

#Pergunta 6
print("""
    Questão 6:

    Como você verifica se uma variável chamada idade é igual a 18 em Python?

    [A] - idade == 18
    [B] - idade = 18
    [C] - idade.equals(18)
    [D] - idade !== 18
""")
questao_6 = input("Digite sua resposta: ")
if questao_6.upper() == "A":
    nota_da_prova += 1
    
#Pergunta 7
print("""
    Pergunta 7:

    O que o operador % faz em Python?

    [A] - Divide dois números
    [B] - Calcula o módulo, ou seja, o resto da divisão
    [C] - Multiplica dois números
    [D] - Eleva um número à potência de outro

    """)
questao_7 = input("Digite sua resposta: ")
if questao_7.upper() == "D":
    nota_da_prova += 1
#Pergunta 8
print("""
    Pergunta 8:

    O que o seguinte código Python faz?

    for i in range(3, 8, 2):
        print(i)

    [A] - Imprime os números 3, 8 e 2
    [B] - Imprime os números 3, 5 e 7
    [C] - Imprime os números de 3 a 8
    [D] - Imprime os números 3, 4, 5, 6, 7, 8

    """)
questao_8 = input("Digite sua resposta: ")
if questao_8.upper() == "B":
    nota_da_prova += 1
#Pergunta 9
print("""
    Pergunta 9:

    Qual é a função da instrução 'else' em um bloco 'if' em Python?

    [A] - É executada se a condição do 'if' for verdadeira
    [B] - É opcional e não tem função específica
    [C] - É executada se a condição do 'if' for falsa
    [D] - É o fechamento da estrutura if

    """)

questao_9 = input("Digite sua resposta: ")
if questao_9.upper() == "C":
    nota_da_prova += 1
    
    

#Pergunta 10
print("""
    Pergunta 10:

    Como se solicita a entrada de um dado vindo do usuário em Python?

    [A] - input()
    [B] - read()
    [C] - user_input()
    [D] - get_user_input()

    """)

questao_10 = input("Digite sua resposta: ")
if questao_10.upper() == "A":
    nota_da_prova += 1
    


animar_texto(fala_que_vai_verificar_a_prova)
passou_na_prova = True if nota_da_prova >= 6 else False

if not passou_na_prova:
   
    animar_texto(texto_reprovou_na_prova)

#colocar as explicação das alternativas que errou
    if questao_1.upper() != "D":
        print("""
        ---------------------------------
        Questão 1 
        ---------------------------------
        O código apresenta uma estrutura condicional (if, elif, else) que avalia a variável 'idade' 
        e imprime uma categoria com base nas condições fornecidas. Vamos analisar as condições:

        • Se a idade for menor ou igual a 10, imprime 'infantil';
        • Se a idade for maior que 10 e menor que 18, imprime 'juvenil';
        • Se a idade for maior que 18 e menor que 40, imprime 'adulto';
        • Se nenhuma das condições anteriores for atendida, imprime 'veterano'. 

    """)
        input("Aperte qualquer tecla para continuar.")
    if questao_2.upper() != "C":
        print("""
        ---------------------------------
        Questão 2
        ---------------------------------
        
        Python fornece um tipo de dado booleano que pode ter um desses dois valores: 
        True (Verdadeiro) ou False (Falso). Os valores booleanos são frequentemente usados 
        em expressões condicionais e em lógica de programação.
    """)
        input("Aperte qualquer tecla para continuar.")
        
    if questao_3.upper() != "A":
        print("""
        ---------------------------------
        Questão 3
        ---------------------------------
        O código fornece a tabuada do 8 de 1 a 10 usando uma função chamada escrever_multiplicacao. 
        Essa função recebe dois números como argumentos, calcula o produto e retorna uma string 
        formatada contendo a expressão da multiplicação.

        O loop 'while' é usado para iterar sobre os números de 1 a 10, chamando a função 
        escrever_multiplicacao e imprimindo cada expressão de multiplicação.
    """)
        input("Aperte qualquer tecla para continuar.")
        

    if questao_4.upper() != "B":
        print("""
        ---------------------------------
        Questão 4
        ---------------------------------
        O comando print() é utilizado para imprimir informações na saída padrão, 
        que geralmente é a tela do computador do usuário.
    """)
        input("Aperte qualquer tecla para continuar.")
        
    if questao_5.upper() != "B":
        print("""
        ---------------------------------
        Questão 5
        ---------------------------------
        O código cria uma lista chamada frutas que contém três strings ("maçã", "banana", "laranja"). 
        Em seguida, ele utiliza um loop for para iterar sobre cada elemento da lista frutas e imprime 
        cada fruta na tela.
    """)
        input("Aperte qualquer tecla para continuar.")
        
    if questao_6.upper() != "A":
        print("""
        ---------------------------------
        Questão 6
        ---------------------------------
        '==' é o operador de igualdade em Python. Sendo assim, esse operador compara um dado valor 
        com o o valor atribuído na variável 'idade'.
    """)
        input("Aperte qualquer tecla para continuar.")
        
    if questao_7.upper() != "D":
        print("""
        ---------------------------------
        Questão 7
        ---------------------------------
        O operador % em Python realiza a operação de módulo, ou seja, 
        retorna o resto da divisão entre dois números.
    """)
        input("Aperte qualquer tecla para continuar.")
        
    if questao_8.upper() != "B":
        print("""
        ---------------------------------
        Questão 8
        ---------------------------------
        A função range(3, 8, 2),  gera uma sequência de números começando em 3, 
        indo até (mas não incluindo) 8, com um passo de 2. Em seguida, 
        o loop for itera sobre essa sequência e imprime cada número.
    """)
        input("Aperte qualquer tecla para continuar.")
        
    if questao_9.upper() != "C":
        print("""
        ---------------------------------
        Questão 9
        ---------------------------------
        A instrução 'else' em um bloco 'if' em Python é executada se a condição do 'if' for falsa.
    """)
        input("Aperte qualquer tecla para continuar.")
        
    if questao_10.upper() != "A":
        print("""
        ---------------------------------
        Questão 10
        ---------------------------------
        Em Python, a função utilizada para solicitar a entrada de um dado do usuário é input().
    """)
        input("Aperte qualquer tecla para continuar.")
        
else:
    animar_texto(texto_passou_na_prova)
    input("\nPressione ENTER quando estiver pronto para começar.")
    abrir_editor('notepad.exe' ,'desafios/laco_de_repeticao/desafio_laco_de_repeticao02.py')
    codigo_do_desafio = ler_arquivo_de_desafio('laco_de_repeticao/desafio_laco_de_repeticao02.py')
    resultado_do_desafio = executar_desafio('laco_de_repeticao/desafio_laco_de_repeticao02.py')
    passou_no_desafio = verificar_resultado_do_desafio(resultado_do_desafio,"O Nome ana esta no Array\n")#True or False
    print(passou_no_desafio)
    if passou_no_desafio:
        animar_texto("""
Haha, então parece que você não é apenas um sortudo que passou na prova por mero acaso. 
Você é realmente digno de estar nesta guilda dos codificadores. Parabéns por sobreviver à seleção, 
meu mais novo recruta, haha. Agora vá descansar, porque amanhã vamos descobrir o que a 'Bug Mancer' preparou para nós. 
Espero que não seja nada que deixe seu coração mais gelado do que o código mal escrito de um estagiário!

Fim do Ato 0 - Introdução""")
    else:
        animar_texto("""
Hum, então você realmente foi um ratinho sortudo que passou na prova por mero acaso e não conseguiu resolver um simples código. 
Parece que alguém esqueceu de atualizar o cérebro antes de vir. Não volte aqui até conseguir decifrar um algoritmo decente 
ou até sua mãe permitir que você jogue no porão de novo. A propósito, eu já pedi para o capanga preparar uma gaiola bem confortável 
para você. Acho que vai precisar."""
)
