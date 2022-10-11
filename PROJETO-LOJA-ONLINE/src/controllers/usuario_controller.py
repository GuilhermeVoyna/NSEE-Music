from controllers.contato_controller import Contato_Controller
from models.usuario.usuario import Usuario
import streamlit as st
from models.util import Util
from models.paginas import Paginas

class Usuario_Controller():
    def __init__(self):
        lista_de_senhas = ["SenhaJoao", "SenhaMatheus", "a"]
        self._lista_usuarios_cadastrados = []
        for i, contato in enumerate(Contato_Controller()._lista_contatos_cadastrados):
            self._lista_usuarios_cadastrados.append(Usuario(contato, lista_de_senhas[i]))
    
    def validar_login(self, email_login, senha_login):
        if not(Util.validar_string(email_login) and Util.validar_string(senha_login)):
            st.session_state["Caption"] = "Preencher todos os campos!"
        else:
            for usuario in self._lista_usuarios_cadastrados:
                if(email_login == usuario._nome_de_usuario and senha_login == usuario._senha):
                    st.session_state["Logado"] = usuario
                    st.session_state["Pagina"] = Paginas.HOME.name
                    return
            st.session_state["Caption"] = "Usuário não Encontrado!"
    
    def retornar_posicao_usuario_banco(self, usuario):
        if usuario in self._lista_usuarios_cadastrados:
            return self._lista_usuarios_cadastrados.index(usuario)
        return None

    def exibir_usuarios(self):
      for usuario in self._lista_usuarios_cadastrados:
        print("Usuario:", usuario, "\n")
    
    def adicionar_usuario_banco(self, usuario_novo):
        self._lista_usuarios_cadastrados.append(usuario_novo)
    
    def adicionar_usuario_banco_posicao(self, usuario_novo, posicao):
        self._lista_usuarios_cadastrados.insert(posicao, usuario_novo)
    
    def remover_usuario_banco_posicao(self, posicao_usuario):
        self._lista_usuarios_cadastrados.pop(posicao_usuario)
    
    def remover_usuario_banco(self, usuario):
        self._lista_usuarios_cadastrados.remove(usuario)
    
    def update_usuario_banco(self, usuario_novo, posicao_user_antigo):
        self.remover_usuario_banco_posicao(posicao_user_antigo)
        self.adicionar_usuario_banco_posicao(usuario_novo, posicao_user_antigo)
    
    def get_lista_usuarios(self):
        return self._lista_usuarios_cadastrados

