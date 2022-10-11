import streamlit as st
from controllers.app_controller import App_Controller
from view.interfaces_usuario import Interfaces_Usuario
from models.util import Util
from models.paginas import Paginas



if not(Util.validar_dicionario(st.session_state)):
    st.session_state["Controller"] = App_Controller()
    st.session_state["Controller"].setar_ambiente_primeiro_acesso()

controller_main = st.session_state["Controller"]
usuario_on = st.session_state["Logado"]  

if st.session_state["Pagina"] == Paginas.LOGIN.name:
    Interfaces_Usuario.exibir_pagina_login(controller_main)

elif st.session_state["Pagina"] == Paginas.HOME.name:
    print("Iniciando....")
    Interfaces_Usuario.exibir_pagina_principal(controller_main, usuario_on)
    print("\n")
    print("st.session_state['Logado']2:", st.session_state["Logado"])
    print("Desligando...")



elif st.session_state["Pagina"] == Paginas.CADASTRO.name:
    Interfaces_Usuario.exibir_pagina_cadastro(controller_main)




