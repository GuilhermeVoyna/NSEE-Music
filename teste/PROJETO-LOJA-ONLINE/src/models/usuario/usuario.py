from models.contato.contato import Contato
from models.carrinho.carrinho import Carrinho

class Usuario():
    def __init__(self, contato, senha):
        self._contato = contato
        self._nome_de_usuario = self._contato._email
        self._senha = senha
        self._carrinho_de_compras = Carrinho()
    
    def adicionar_compra(self, item):
        self._carrinho_de_compras.adicionar(item)
    
    def remover_compra(self, item):
        self._carrinho_de_compras.remover(item)
    
    def __str__(self) -> str:
        return f'Nome de Usuário:{self._nome_de_usuario} Contato:{self._senha} Contato:{self._contato} Carrinho de Compra:{self._carrinho_de_compras}'

    def validar_usuario(self):
        return (self._contato.validar_contato() and self._senha != '')
    
    def get_carrinho_de_compras(self):
        return self._carrinho_de_compras



    
    
    
