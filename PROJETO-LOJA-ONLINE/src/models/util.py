import datetime as dt
from PIL import Image as img
import os

class Util():
    @staticmethod
    def calcular_idade(data_nascimento):
        today = dt.date.today()
        idade = today.year - data_nascimento.year - ((today.month, today.day) < (data_nascimento.month, data_nascimento.day))
        return idade

    @staticmethod
    # Retorna True se campo diferete de vazio
    def validar_string(campo_str):
        return(campo_str != None and campo_str!="")


    @staticmethod
    # Retorna True se dicionario diferente de vazio
    def validar_dicionario(dict):
        return len(dict.keys()) != 0

    @staticmethod
    def validar_lista(lista):
        for valor in lista:
            if not(Util.validar_string(valor)):
                return False
        return True

    @staticmethod
    def limpar_tela():
        os.system('cls')

    @staticmethod
    def ajustar_imagem(path_imagem,x,y):
        imagem = img.open(path_imagem)
        return imagem.resize((x, y))

    @staticmethod
    def converter_float_str_decimal_BR(valor):
        result = str("{:.2f}".format(valor))
        return result.replace(".",",")
    
    @staticmethod
    def tratar_lista_valores_duplicados(lista):
        return ([ [i, lista.count(i)] for i in set(lista)])

    

