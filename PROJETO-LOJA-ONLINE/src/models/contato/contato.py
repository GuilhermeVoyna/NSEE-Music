from models.util import Util

class Contato():
    def __init__(self, nome, email, telefone, data_nascimento):
        self._nome = nome
        self._email = email
        self._telefone = telefone
        self._idade = Util.calcular_idade(data_nascimento)
        self._primeiro_nome = self.resgatar_primeiro_nome()

    
    def __str__(self) -> str:
        return f'Nome Completo:{self._nome} Email:{self._email} Telefone:{self._telefone} Idade:{self._idade} Primeiro Nome{self._primeiro_nome}'

    def validar_contato(self):
        return (self._nome != '' and self._email != '' and self._telefone != '' and self._idade != '' and self._primeiro_nome != '')
    
    def get_email(self):
        return self._email

    def resgatar_primeiro_nome(self):
        if(Util.validar_string(self._nome)):
            return self._nome.split()[0]
        return ""

