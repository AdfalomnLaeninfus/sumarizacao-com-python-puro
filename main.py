from core.text import ProcessadorTexto

processador = ProcessadorTexto()

txt = "Teu cú é bem aberto me passe ele agora, pois, \
    eu o quero pra mim rapariga, isso é bem excitante, \
    ao ponto de rasgar minhas calças, bem comum. \n\n\
    agora só me falta um cú"

texto_formatado = processador.pre_processamento(txt)

contagem_das_palavras = processador.frequencia_das_palavras(texto_formatado)

frequencia_proporcional = processador.frequencia_proporcional(contagem_das_palavras)

print(frequencia_proporcional)