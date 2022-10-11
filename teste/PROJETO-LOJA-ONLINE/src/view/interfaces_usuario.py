import streamlit as st
import datetime as dt
from models.util import Util
import time

class Interfaces_Usuario():
    
    @staticmethod    
    def exibir_pagina_login(controller):

        # with st.form('Formulario Login'):

        st.title("Bem vindo ao Mundo dos Games!🚀")
        st.subheader("Login")

        usuario_login = st.text_input(label="E-mail", placeholder ="Digite seu E-mail", value="")
        usuario_senha = st.text_input(label="Senha", placeholder ="Digite sua Senha", type='password', value="")
        col1, col2, col3, col4, col5 = st.columns([1, 1, 1,3.35,1.1])
        with col1:
            st.button(
                label="Entrar", 
                on_click=controller._obj_user.validar_login,
                kwargs={"email_login": usuario_login, "senha_login": usuario_senha}
                )
        with col4:
            st.write("Novo por aqui? Faça agora seu Cadastro👉")
        with col5:
            st.button(
                label="Cadastro",
                on_click=controller.setar_ambiente_cadastro
                )
        Interfaces_Usuario.escrever_mensagem_aviso()
    
        # st.session_state["Controller"] = controller

        
    @staticmethod   
    def exibir_pagina_cadastro(controller):
        data_min = dt.date(1900, 1, 1)
        data_max = dt.date.today() 
        
        # with st.form('Formulario Cadastro',  clear_on_submit=True):

        st.title("Sua Jornada Começa Agora !🚀🔥")
        st.subheader("Meu Primeiro Acesso")

        col1, col2 = st.columns(2)
        with col1:
            usuario_nome = st.text_input(label="Nome", placeholder ="Digite seu Nome Completo", value="")
            usuario_email = st.text_input(label="E-mail", placeholder ="Digite seu endereço de E-mail", value="")
        with col2:
            usuario_telefone = st.text_input(label="Telefone", placeholder ="Digite seu Telefone", value="")
            usuario_data_nascimento = st.date_input(label="Data de Nascimento", min_value=data_min, max_value=data_max)
        
        usuario_senha = st.text_input(label="Senha", placeholder ="Digite uma senha", value="",  type='password')
        usuario_senha_2 = st.text_input(label="Confirmação de Senha", placeholder ="Digite novamente sua senha", value="", type='password')

        col1, col2 = st.columns([8, 1])
        lista_campos_cadastro = [usuario_nome, usuario_email, usuario_telefone, usuario_data_nascimento]
        lista_senhas = [usuario_senha, usuario_senha_2]
        with col1:
            st.button(label="Confirmar Cadastro", 
                    on_click=controller._obj_contato.confirmar_cadastro,
                    kwargs={"controller": controller, "lista_cadastro": lista_campos_cadastro, "lista_senhas": lista_senhas})

        Interfaces_Usuario.escrever_mensagem_aviso()
        with col2:
            st.button(
                    label='Voltar',
                    on_click=controller.setar_ambiente_primeiro_acesso)
        
        st.session_state["Controller"] = controller


    @staticmethod        
    def exibir_pagina_principal(controller, usuario_logado):
        st.sidebar.radio("Navegação",["Home", "Minha Conta", "About Us"])
        st.sidebar.button(label="Sair")
        # st.header("Os mais vendidos 🔥")    
        carrinho_de_compras = usuario_logado.get_carrinho_de_compras()
        qtde_itens_adicionados = f'Carrinho ({carrinho_de_compras.get_quantidade_itens()}) 🛒'
        loja, carrinho, pagamento = st.tabs(["Loja", qtde_itens_adicionados ,"Pagamento"])
        with loja:
            Interfaces_Usuario.exibir_busca_usuario(controller)
        with carrinho:
            Interfaces_Usuario.exibir_pagina_carrinho(controller, carrinho_de_compras, usuario_logado)



    @staticmethod        
    def exibir_busca_usuario(controller):
        st.header("A sua Loja favorita de Games!🎮")
        # ***** Variáveis Principais *****
        itens_cadastrados = controller._obj_item.get_lista_itens_cadastrados()
        lista_nome_itens_cadastrados = controller._obj_item.montar_lista_nomes_itens()
         # ***** Montagem da Caixa de Busca *****
        lista_caixa_de_busca = lista_nome_itens_cadastrados.copy()
        lista_caixa_de_busca.sort()
        lista_caixa_de_busca.insert(0, "Visualizar Todos")
        opcao_busca = st.selectbox(
                    label="Pesquise aqui seu jogo!", 
                    options=lista_caixa_de_busca, 
                    index=(0)
                    )

        Interfaces_Usuario.exibicao_items(controller, itens_cadastrados, opcao_busca)
        
    @staticmethod
    def exibicao_items(controller, catalogo_de_produtos, caixa_seletora):
        if caixa_seletora != "Visualizar Todos":
            try:
                item = controller.get_obj_item().get_item_pelo_nome(caixa_seletora)
                # indice = lista_itens_original.index(caixa_seletora)
                Interfaces_Usuario.exibir_infos_item(item, 200, 250)
            except:
                Interfaces_Usuario.exibir_produtos_3colunas(catalogo_de_produtos, 200, 250)
        else:
            Interfaces_Usuario.exibir_produtos_3colunas(catalogo_de_produtos, 200, 250)
    
    @staticmethod
    def exibir_produtos_3colunas(lista_itens, largura_imagem, altura_imagem):
        # **** lista deve ser divisvel por 3, pq sao 3 colunas****
        col1, col2, col3 = st.columns(3)
        list_coluna1=range(1,len(lista_itens)-1,3)
        list_coluna2=range(2,len(lista_itens),3)
        with st.container():
            for i, item in enumerate(lista_itens):
                if(i in list_coluna1):
                    with col1:
                        Interfaces_Usuario.exibir_infos_item(item, largura_imagem, altura_imagem)
                elif(i in list_coluna2):
                    with col2:
                        Interfaces_Usuario.exibir_infos_item(item, largura_imagem, altura_imagem)
                else:
                    with col3:
                        Interfaces_Usuario.exibir_infos_item(item, largura_imagem, altura_imagem)

    @staticmethod
    def exibir_infos_item(item, x, y):
        usuario_novo = st.session_state["Logado"]
        controller   = st.session_state["Controller"]
        st.subheader(item.get_nome())
        st.image(Util.ajustar_imagem(item.get_imagem(), x, y))
        st.info("R$ " + Util.converter_float_str_decimal_BR(item.get_valor()),icon="💵")
        botao_comprar = st.button(
                label="Adicionar ao carrinho", 
                key=item.get_nome(),
                on_click= usuario_novo.adicionar_compra,
                kwargs={"item": item}
                )

        if botao_comprar:
            print("USUARIO apos botao: ", usuario_novo)
            # usuario_novo.adicionar_compra(item)
            index = controller.get_obj_user().retornar_posicao_usuario_banco(st.session_state["Logado"])
            controller.get_obj_user().update_usuario_banco(usuario_novo, index)
            st.session_state["Logado"] = usuario_novo
            st.session_state["Controller"] = controller
            print("st.session_state['Logado']1:", st.session_state["Logado"])
            st.balloons()
            st.caption("Adicionado com Sucesso!")



    @staticmethod        
    def exibir_pagina_carrinho(controller, carrinho, usuario_logado):
        st.header("Confere tudo pra ver se não faltou nada! 😉")
        col1, col2, col3 = st.columns([1.5,1,1])
        dict = carrinho.dict_controle()
        print("dict:", dict)
        for item_nome in dict.keys():
            with col1:
                st.subheader(item_nome)
            with col2:
                st.write("")
                item = controller.get_obj_item().get_item_pelo_nome(item_nome)

                qtd = st.number_input(label         = "Contador Itens", 
                                key                 = item_nome*2,
                                min_value           = 0,
                                max_value           = 1000, 
                                value               = dict[item_nome][1], 
                                label_visibility    = "collapsed",
                                on_change           = usuario_logado.adicionar_compra,
                                        kwargs={"item": item}
                                )

                index = controller.get_obj_user().retornar_posicao_usuario_banco(usuario_logado)
                # item = controller.get_obj_item().get_item_pelo_nome(item_nome)
                print("item:", item)
                print("index:", index)

                if(qtd > dict[item_nome][0]):
                    
#              botao_comprar = st.button( label="Adicionar ao carrinho", 
                                #         key=item.get_nome(),
                                #         on_click= usuario_novo.adicionar_compra,
                                #         kwargs={"item": item}
                                #         )
                # if botao_comprar:
                #     print("USUARIO apos botao: ", usuario_novo)
                #     usuario_novo.adicionar_compra(item)
                #     index = controller.get_obj_user().retornar_posicao_usuario_banco(st.session_state["Logado"])
                #     controller.get_obj_user().update_usuario_banco(usuario_novo, index)
                #     st.session_state["Logado"] = usuario_novo
                #     st.session_state["Controller"] = controller
                #     st.balloons()
                #     st.caption("Adicionado com Sucesso!")


                    usuario_logado.adicionar_compra(item)
                    controller.get_obj_user().update_usuario_banco(usuario_logado, index)
                    
                    print("ENTROU")
                    # with st.spinner('Adicionando...'):
                    #     time.sleep(0.5)
                    #     st.success('Sucesso!')
                    # st.experimental_rerun()

                elif(qtd < dict[item_nome][0]):
                    print("SAIU")
                    usuario_logado.remover_compra(item)
                    controller.get_obj_user().update_usuario_banco(usuario_logado, index)
                    # st.experimental_rerun()
            
                st.session_state["Logado"] = usuario_logado
                st.session_state["Controller"] = controller

            with col3:
                valor_individual = Util.converter_float_str_decimal_BR(dict[item_nome][1]*qtd)
                st.subheader("R$ " + valor_individual)


    
    @staticmethod
    def escrever_mensagem_aviso():
        if(Util.validar_string(st.session_state["Caption"])):
            st.error(st.session_state["Caption"], icon="⚠️")
    