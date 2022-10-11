from models.usuario.usuario import Usuario
from models.contato.contato import Contato
import datetime as dt
import streamlit as st
from models.util import Util
from models.paginas import Paginas

class Contato_Controller():
    def __init__(self):
        self._lista_contatos_cadastrados = [Contato(nome="Joao da Silva", email="joao@gmail.com", telefone="(11)923456789", data_nascimento=dt.date(1999, 1, 1)),
                                            Contato(nome="Matheus da Silva", email="matheus@gmail.com", telefone="(11)901234567", data_nascimento=dt.date(1979, 9, 11)),
                                            Contato(nome="a", email="a", telefone="(11)975327165", data_nascimento=dt.date(1995, 5, 3))
        ]
    
    def confirmar_cadastro(self, controller, lista_cadastro, lista_senhas):
        st.session_state["Pagina"] = Paginas.CADASTRO.name
        novo_contato = Contato(nome=lista_cadastro[0], email=lista_cadastro[1], telefone=lista_cadastro[2], data_nascimento=lista_cadastro[3])
        novo_usuario = Usuario(contato=novo_contato, senha=lista_senhas[0])
        if(not(novo_usuario.validar_usuario()) or not(Util.validar_string(lista_senhas[1]))):
            st.session_state["Caption"] = "Campos obrigatórios não preenchidos!"
        elif(lista_senhas[0] != lista_senhas[1]):
            st.session_state["Caption"] = "As senhas não conferem!"
        elif(self.checar_contato(novo_contato)):
            st.session_state["Caption"] = "Usuário já Cadastrado!"
        else:
            controller.get_obj_contato().adicionar_contato_banco(novo_contato)
            controller.get_obj_user().adicionar_usuario_banco(novo_usuario)
            controller.setar_ambiente_primeiro_acesso()
        
    def checar_contato(self, novo_contato):
        for contato in self._lista_contatos_cadastrados:
            if(novo_contato.get_email() == contato._email):
                return True
        return False
    
    def exibir_contatos(self):
      for contato in self._lista_contatos_cadastrados:
        print("Contato:", contato)
    
    def adicionar_contato_banco(self, novo_contato):
        self._lista_contatos_cadastrados.append(novo_contato)
    
    def get_lista_contatos(self):
        return self._lista_contatos_cadastrados


