from models.produtos.item import Item

class Catalogo_Controller():
    def __init__(self):
        self._lista_itens_cadastrados = [
            Item(nome="Overwatch", descricao="Muito Divertido", valor=200.00, imagem="assets/pc/jogo1.jpg",),
            Item(nome="The Sims 4", descricao="Muito Divertido", valor=200.00, imagem="assets/pc/jogo2.jpg",),
            Item(nome="Grand Theft Auto V", descricao="Muito Divertido", valor=200.50, imagem="assets/pc/jogo3.jpg",),
            Item(nome="Minecraft", descricao="Muito Divertido", valor=200.00, imagem="assets/pc/jogo5.jpg",),
            Item(nome="Fortnite", descricao="Muito Divertido", valor=200.00, imagem="assets/pc/jogo6.jpg",),
            Item(nome="Spider-Man", descricao="Muito Divertido", valor=200.00, imagem="assets/ps4/jogo1.jpg",),
            Item(nome="Doom", descricao="Muito Divertido", valor=200.00, imagem="assets/ps4/jogo2.jpg",),
            Item(nome="Fifa 19", descricao="Muito Divertido", valor=200.00, imagem="assets/ps4/jogo3.jpg",),
            Item(nome="Cyberpunk 2077", descricao="Muito Divertido", valor=200.00, imagem="assets/ps4/jogo4.jpg",),
            Item(nome="Jump Force", descricao="Muito Divertido", valor=200.00, imagem="assets/ps4/jogo6.jpg",),
            Item(nome="Watch Dogs", descricao="Muito Divertido", valor=200.00, imagem="assets/ps4/jogo7.jpg",),
            Item(nome="Battlefiel 2042", descricao="Muito Divertido", valor=200.00, imagem="assets/ps4/jogo8.jpg",),
            Item(nome="Horizon Forbidden West", descricao="Muito Divertido", valor=200.00, imagem="assets/ps4/jogo5.jpg",),
            Item(nome="Grand Theft Auto  IV", descricao="Muito Divertido", valor=200.00, imagem="assets/pc/jogo4.jpg",),
            Item(nome="Uncharted 4: A Thief's End", descricao="Muito Divertido", valor=200.00, imagem="assets/ps4/jogo9.jpg",)
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

