# Bruno Navarro Ivatiuk

#	Para obter os pontos relativos a este trabalho, você deverá criar um programa, utilizando a
#linguagem Python, C, ou C++. Este programa, quando executado, irá apresentar os resultados de
#operações que serão realizadas entre dois conjuntos de dados.
#	O programa que você desenvolverá irá receber como entrada um arquivo de texto (.txt)
#contendo vários conjuntos de dados e várias operações. Estas operações e dados estarão representadas
#em um arquivo de textos contendo apenas os dados referentes as operações que devem ser realizadas
#segundo a seguinte regra fixa: a primeira linha do arquivo de texto de entrada conterá o número de
#operações que estão descritas no arquivo, este número de operações será um inteiro; as linhas
#seguintes seguirão sempre o mesmo padrão de três linhas: a primeira linha apresenta o código da
#operação (U para união, I para interseção, D para diferença e C produto cartesiano), a segunda e
#terceira linhas conterão os elementos dos conjuntos separados por virgulas. A seguir está um exemplo
#das linhas que podem existir em um arquivo de testes para o programa que você irá desenvolver:
#		4
#		U
#		3, 5, 67, 7
#		1, 2, 3, 4
#		I
#		1, 2, 3, 4, 5
#		4, 5
#		D
#		1, A, C, 34
#		A, C, D, 23
#		C
#		3, 4, 5, 5, A, B, R
#		1, B, C, D, 1
#	Neste exemplo temos 4 operações uma união (U), uma interseção (I), um diferença (D) e um
#produto cartesiano (C). A união, definida por U, deverá ser executada sobre os conjuntos {𝟑, 𝟓, 𝟔𝟕, 𝟕} e
#{𝟏, 𝟐, 𝟑, 𝟒}, cujos elementos estão explicitados nas linhas posteriores a definição da operção (U).
#	A resposta do seu programa deverá conter a operação realizada, descrita por extenso, os dados
#dos conjuntos identificados, e o resultado da operação. No caso da união a linha de saída deverá conter
#a informação e a formatação mostrada a seguir:
#	União: conjunto 1 {3, 5, 67, 7}, conjunto 2 {1, 2, 3, 4}. Resultado: {3, 5, 67, 7, 1, 2, 4}
#	Seu programa deverá mostrar a saída no terminal, ou em um arquivo de textos. Em qualquer
#um dos casos, a saída será composta por uma linha de saída para cada operação constante no arquivo
#de textos de entrada formatada segundo o exemplo de saída acima. Observe as letras maiúsculas e
#minúsculas, e os pontos utilizados na formatação da linha de saída apresenta acima.
#	No caso do texto de exemplo, teremos 4 linhas, e apenas 4 linhas de saída, formatadas e
#pontuadas conforme o exemplo de saída acima. O uso de linhas extras na saída, ou erros de formatação,
#implicam em perda de pontos como pode ser visto na rubrica de avaliação constante neste documento.
#	Para que seu programa possa ser testado você deve criar, no mínimo, três arquivos de entrada
#contendo um número diferente de operações, operações com dados diferentes, e operações em ordem
#diferentes. Os arquivos de entrada criados para os seus testes devem estar disponíveis tanto no
#ambiente repl.it quanto no ambiente Github.
#	Observe que o professor irá testar seu programa com os arquivos de testes que você criar e com,
#no mínimo um arquivo de testes criado pelo próprio professor.


def remover_repeticoes(conjunto):
    '''
    Remove repetições transformando a lista em dicionário, já que estes não
    aceitam repetições e mantém a ordem dos elementos. Transforma em lista
    novamente para manter o formato.
    '''
    return list(dict.fromkeys(conjunto))


def operacoes(arq, linha, op):
    '''
    Recebe uma lista contendo as linhas do arquivo e
    imprime na tela o resultado da operação indicada.
    :param arq: lista contendo as linhas do arquivo.
    :param linha: posição onde se encontra a operação.
    :param op: tipo da operação.
    '''
    conjunto1 = arq[linha+1].split(', ')
    conjunto2 = arq[linha+2].split(', ')
    conjunto_resultado = []
    match op:
        case 'U':
            conjunto_resultado = conjunto1 + conjunto2
            conjunto_resultado = remover_repeticoes(conjunto_resultado)
            conjunto_resultado = ', '.join(conjunto_resultado)
            print("União: conjunto 1 {" + arq[linha+1] + "}, conjunto 2 {" + arq[linha+2] +
                  "}. Resultado: {" + conjunto_resultado + '}')
        case 'I':
            for elemento in range(len(conjunto1)):
                if conjunto1[elemento] in conjunto2:
                    conjunto_resultado.append(conjunto1[elemento])
            conjunto_resultado = remover_repeticoes(conjunto_resultado)
            conjunto_resultado = ', '.join(conjunto_resultado)
            print("Intersecção: conjunto 1 {" + arq[linha+1] + "}, conjunto 2 {" + arq[linha+2] +
                  "}. Resultado: {" + conjunto_resultado + '}')
        case 'D':
            for elemento in conjunto1:
                if elemento not in conjunto2:
                    conjunto_resultado.append(elemento)
            conjunto_resultado = remover_repeticoes(conjunto_resultado)
            conjunto_resultado = ', '.join(conjunto_resultado)
            print("Diferença: conjunto 1 {" + arq[linha+1] + "}, conjunto 2 {" + arq[linha+2] +
                  "}. Resultado: {" + conjunto_resultado + '}')
        case 'C':
            conjunto1 = remover_repeticoes(conjunto1)
            conjunto2 = remover_repeticoes(conjunto2)
            for x in conjunto1:
                for y in conjunto2:
                    conjunto_resultado.append(f"({x}, {y})")
            conjunto_resultado = ', '.join(conjunto_resultado)
            print("Produto Cartesiano: conjunto 1 {" + arq[linha+1] + "}, conjunto 2 {" + arq[linha+2] +
                  "}. Resultado: {" + conjunto_resultado + '}')


if __name__ == '__main__':
    nomeArquivo = "Teste1.txt"  # Modifique essa variável para alterar o arquivo.
    file = open(nomeArquivo, "rt")
    arquivo = file.read().splitlines()  # Transforma o arquivo em uma lista.
    quantOperacoes = int(arquivo[0])
    for loop in range(quantOperacoes):
        linhaOperacao = 1 + (3 * loop)
        operacao = arquivo[linhaOperacao]
        operacoes(arquivo, linhaOperacao, operacao)
