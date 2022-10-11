from controllers.usuario_controller import Usuario_Controller
from controllers.Lista_de_jogos_Controller import Lista_de_jogos_Controller
from controllers.contato_controller import Contato_Controller


import streamlit as st
from models.paginas import Paginas

class App_Controller():
    def __init__(self):
        self._obj_user = Usuario_Controller()
        self._obj_contato = Contato_Controller()
        self._obj_item = Lista_de_jogos_Controller()
    
    def setar_ambiente_primeiro_acesso(self):
        st.session_state["Logado"]      = None
        st.session_state["Caption"]     = None
        st.session_state["Item"]        = None
        st.session_state["Pagina"]      = Paginas.LOGIN.name

    def setar_ambiente_cadastro(self):
        st.session_state["Logado"]      = None
        st.session_state["Caption"]     = None
        st.session_state["Item"]        = None
        st.session_state["Pagina"]      = Paginas.CADASTRO.name
    
    def get_obj_user(self):
        return self._obj_user
    
    def get_obj_contato(self):
        return self._obj_contato
    
    def get_obj_item(self):
        return self._obj_item

