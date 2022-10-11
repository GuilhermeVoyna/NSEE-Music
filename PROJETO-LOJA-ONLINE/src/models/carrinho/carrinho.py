class Carrinho():
    def __init__(self):
        self._itens = []

    def calcular_valor_total(self):
        total = 0
        for item in self._itens:
            total += item.get_valor()
        return total

    def get_quantidade_itens(self):
        return len(self._itens)

    def adicionar(self, item):
        self._itens.append(item)

    def remover(self, item):
        if item in self._itens:
            self._itens.remove(item)

    def get_itens(self):
        return self._itens
    
    def dict_controle(self):
        print("self._itens:", self._itens)
        dict = {}
        for item in self._itens:
            if not (item.get_nome() in dict.keys()):  
                dict[item.get_nome()] = [item.get_valor(), 1]
            else:
                dict[item.get_nome()][1] += 1
        return dict

    def __str__(self):
        return f'Itens:{self._itens}'