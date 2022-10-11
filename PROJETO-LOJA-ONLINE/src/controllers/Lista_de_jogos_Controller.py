from models.produtos.item import Item

class Lista_de_jogos_Controller():
    def __init__(self):
        self._lista_itens_cadastrados = [

            Item(nome="Vandal Sublime", descricao="Muito Divertido", valor=200.00, imagem="assets/pc/VandalSublime.jpg",),
            Item(nome="Phantom Oni", descricao="Muito Divertido", valor=200.00, imagem="assets/pc/Oni.jpg",),
            Item(nome="Faca Champions", descricao="Muito Divertido", valor=200.00, imagem="assets/pc/Facachamps.jpg",),
            Item(nome="Ghost Soberania", descricao="Muito Divertido", valor=200.00, imagem="assets/pc/Ghostsoberania.jpg",)
        ]

    def get_item_pelo_nome(self, nome):
        for item in self._lista_itens_cadastrados:
            if item.get_nome() == nome:
                return item
        return None
        
    
    def get_lista_itens_cadastrados(self):
        return self._lista_itens_cadastrados
    
    def montar_lista_nomes_itens(self):
        lista=[]
        for item in self._lista_itens_cadastrados:
            lista.append(item.get_nome())
        return lista

