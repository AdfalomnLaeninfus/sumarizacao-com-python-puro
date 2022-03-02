from concurrent.futures import process
from core.text import ProcessadorTexto

processador = ProcessadorTexto()

txt = """O que são stopwords?
As famosas Stopwords (ou palavras de parada – tradução livre) são palavras que podem ser consideradas irrelevantes para o conjunto de resultados a ser exibido em uma busca realizada em uma Search Engine. Exemplos: as, e, os, de, para, com, sem, foi. Lembre-se que para cada língua as stopwords mudam, ou seja, stopwords em inglês seriam: the, a, as, etc.

Outro ponto importante é que quando dizemos que as stopwords são irrelevantes isso depende muito da busca realizada, pois o contexto da busca fará toda a diferença para cada palavra usada na pesquisa realizada. Ou seja, ao desenvolver uma aplicação de filtragem de spans, realmente as stopwords irão atrapalhar, no entanto, em outros tipos de aplicações as stopwords podem ter valor e não podem ser descartadas.

Por que devo remover stopwords?
Esse processo faz parte do pré-processamento de dados realizado nas etapas iniciais de um pipeline de PLN. Quando devemos montar um Bag-of-words, por exemplo, a maior frequência de palavras serão stopwords. Pois estas palavras são utilizadas o tempo todo para dar sentido ao texto. Portanto, remover stopwords reduz o ruído dos dados analisados.   

Removendo stopswords “na mão” com python
Parece algo idiota o que vou mostrar agora, mas é uma solução relativamente viável. Você pode remover stopwords simplesmente listando as palavras que você quer remover dentro de um vetor:"""

texto_formatado = processador.pre_processamento(txt)

contagem_das_palavras = processador.frequencia_das_palavras(texto_formatado)

frequencia_proporcional = processador.frequencia_proporcional(contagem_das_palavras)

frases = processador.tokenize_de_frases(txt)

tok_palavras = [frases for frases in processador.tokenize_de_frases(txt)]

# print(processador.pontuacao["pt-br"])

# for i in tok_palavras:
#     for j in i:
#         processador.tokenize_de_palavras(j)

processador.tokenize_de_palavras("Adriano\né mó noob.")