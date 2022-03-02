class ProcessadorTexto:
    def __init__(self):
        self.pontuacao = {
            "pt-br": "! \" # $ % ' ( ) * + , - . / : ; < > = ? @ [ ] \\ ^ _ ` { ~ } “ ” \\n \\t \\r".split()
        }

        self.stopwords = {
            "pt-br": [
                "a", "as", "o", "os",
                "e", "é", "ao", "aos",
                "em", "um", "uma", "uns",
                "do", "da", "de", "dos",
                "das", "com", "não", "à",
                "mais", "mas", "ele", "ela",
                "eles", "elas", "como", "nós",
                "vós", "seu", "sua", "seus",
                "suas", "nosso", "nós", "apenas",
                "no", "na", "nos", "nas", "pois",
                "me", "eu", "tu", "mim", "só",
                "isso", "pra", "se", "ou", "que",
                "são", "por", "que", "ser", "você",
                "para", "faz", "podem", "sem", "foi",
                "etc", "seja", "irão", "fará",
                "toda", "quando", "entanto", "entretanto",
                "acaso", "caso", "esse", "essa", "serão",
                "dar", "este", "esta", "estes", "estas",
                "vou", "irei", "quer", "pode"
            ]
        }

    def pre_processamento(self, txt:str):
        """Método que auxilia no processamento deixando de formar mais organizada
        e limpa para o processamento posterior, com o texto todo minúsculo e
        sem nenhum digito.
        
        return (str):
            text_formatado (str)"""
        
        tokens = list()
        texto_formatado = txt.lower()

        for token in txt.split():
            tmp = ""

            for letra in token:
                if letra not in self.pontuacao["pt-br"]:
                    tmp = tmp + letra
            
            if tmp not in self.stopwords["pt-br"] and not tmp.isdigit():
                tokens.append(tmp)
                
        texto_formatado = " ".join(tokens)

        return texto_formatado

    def frequencia_das_palavras(self, txt:str):
        contagem = dict()
        palavras = txt.split()

        for i in palavras:
            if i not in contagem:
                contagem.setdefault(i, 1)
            else:
                contagem[i] += 1
        
        return contagem
    
    def frequencia_proporcional(self, itens:dict):
        frequencia = dict()
        maximo = max([value for item, value in itens.items()])

        for item, valor in itens.items():
            if item not in frequencia.keys():
                frequencia.setdefault(item, valor/maximo)

        return frequencia

    def tokenize_de_frases(self, txt:str):
        frases = list()

        tmp = ""
        for i in txt:
    
            if i == ".":
                tmp += i
                frases.append([tmp.strip()])
                tmp = ""
            else:
                tmp += i

        return frases
    
    def tokenize_de_palavras(self, txt:str):
        txt = txt.lower()
        lista_de_palavras = list()

        tmp = ""

        for letra in txt:
            print(tmp)
            for sinal in self.pontuacao["pt-br"]:
                if sinal in tmp:
                    tmp.replace(sinal, ' ')

            if letra not in self.pontuacao["pt-br"] and letra and tmp not in self.pontuacao["pt-br"]:
                tmp += letra
            elif letra in self.pontuacao["pt-br"]:
                lista_de_palavras.append(tmp)
                tmp = letra
            else:
                lista_de_palavras.append(tmp)
                lista_de_palavras.append(letra)
                tmp = ""

        print(lista_de_palavras)
