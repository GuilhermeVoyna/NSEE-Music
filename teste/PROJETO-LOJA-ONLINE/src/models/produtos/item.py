class Item():
    #Método construtor
    def __init__(self, nome, descricao, valor, imagem):
        self._nome = nome
        self._descricao = descricao
        self._valor = valor
        self._imagem = imagem
    
    def get_valor(self):
        return self._valor

    def get_descricao(self):
        return self._descricao

    def get_nome(self):
        return self._nome
        
    def get_imagem(self):
        return self._imagem

    def __str__(self) -> str:
        return f'Produto:{self._nome} Descrição:{self._descricao} Valor:{self._valor} Imagem:{self._imagem}'

        return self._nome + str(self._valor)

    # def __eq__(self, __o: object) -> bool:
    #     if(isinstance(__o,Item)):
    #         return self._nome == __o.get_nome()
    #     return False