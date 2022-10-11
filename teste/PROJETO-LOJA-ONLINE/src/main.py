import streamlit as st
from controllers.app_controller import App_Controller
from view.interfaces_usuario import Interfaces_Usuario
from models.util import Util
from models.paginas import Paginas



if not(Util.validar_dicionario(st.session_state)):
    st.session_state["Controller"] = App_Controller()
    st.session_state["Controller"].setar_ambiente_primeiro_acesso()

# ********** Carregar Banco de Dados **********
controller_main = st.session_state["Controller"]
usuario_logado = st.session_state["Logado"]  

if st.session_state["Pagina"] == Paginas.LOGIN.name:
    Interfaces_Usuario.exibir_pagina_login(controller_main)

elif st.session_state["Pagina"] == Paginas.HOME.name:
    # Util.limpar_tela()
    print("********* COMEÇOU *********")
    Interfaces_Usuario.exibir_pagina_principal(controller_main, usuario_logado)
    print("")
    print("st.session_state['Logado']2:", st.session_state["Logado"])
    print("********* Terminou *********")



elif st.session_state["Pagina"] == Paginas.CADASTRO.name:
    Interfaces_Usuario.exibir_pagina_cadastro(controller_main)


# controller_usuarios.exibir_usuarios()
# # print("st.session_state", st.session_state)
# # print("st.session_state:",  st.session_state)


