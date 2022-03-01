class TextProcessor:
    def __init__(self):
        self.pontuacao = {
            "pt-br": " ".join("!\"#$%'()*+,-./:;<>=?@[]\\^_`{~}").split()
        }

