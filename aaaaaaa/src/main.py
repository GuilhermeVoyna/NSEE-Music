
import pickle
from pathlib import Path
from unicodedata import name

import streamlit as st  # pip install streamlit
import streamlit_authenticator as stauth
from controllers.cart_controller import CartController  # pip install streamlit-authenticator

from src.controllers.user_controller import UserController
from src.controllers.product_controller import ProductController
import hashing

st.set_page_config(page_title="حبيبي", page_icon="assets\Logo.png", layout="wide")


# --- USER AUTHENTICATION ---
names = UserController.get_names(UserController())
usernames = UserController.get_usernames(UserController())

# load hashed passwords

try:
    file_path = Path(__file__).parent / "hashed_pw.pkl"
    file_path.open("rb")
except:
    hashing

with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

authenticator = stauth.Authenticate(names, usernames, hashed_passwords,
    "Steam", "abcdef", cookie_expiry_days=30)

#usuario: adm
#senha: adm

name, authentication_status, username = authenticator.login("تسجيل الدخول", "main")
if authentication_status == False:
    st.error("اسم المستخدم / كلمة المرور غير صحيح")
    st.session_state["Cart"] = CartController()

if authentication_status == None:
    st.warning("الرجاء إدخال اسم المستخدم وكلمة المرور الخاصة بك")
    
    st.session_state["Cart"] = CartController()

if authentication_status:
    authenticator.logout("تسجيل خروج")
    st.sidebar.title(f"أهلا وسهلا *{name}*")
    st.sidebar.image("https://i0.statig.com.br/bancodeimagens/imgalta/6n/eg/mr/6negmrmw5dl6br825gkgbmw0z.jpg")
    st.sidebar.markdown("***")
    st.sidebar.title(f"مرهم بريمو")
    st.sidebar.markdown("***")

    tab1, tab2= st.tabs(["Habibi","Carrinho"])

    # --- Comidinhas ---
    with tab1: 
            st.title("اصفحه") #Esfihas

            st.markdown("***")
            st.text("")
            col1,col2 = st.columns(2,gap="large")

    with col1:
        index = 0
        product = ProductController.get_product(ProductController(),index)
        c = st.container()
        c.markdown(f"## {product.get_name()}")
        c.image(f"{product.get_url()}", width = 300)
        c.markdown(f"## R${product.get_price()}")
        quantity0 = c.number_input(label = " "*index, format = "%i", step = 1,min_value = 1)
        c.button(label = f"+ Cart", key = index, on_click= st.session_state["Cart"].add_product, args = (product, quantity0))
    with col2:
        index = 1
        product = ProductController.get_product(ProductController(),index)
        c = st.container()
        c.markdown(f"## {product.get_name()}")
        c.image(f"{product.get_url()}", width = 300)
        c.markdown(f"## R${product.get_price()}")
        quantity1 = c.number_input(label = " "*index, format = "%i", step = 1,min_value = 1)
        c.button(label = f"+ Cart", key = index, on_click= st.session_state["Cart"].add_product, args = (product, quantity1))
    with col1:
        index = 2
        product = ProductController.get_product(ProductController(),index)
        c = st.container()
        c.markdown(f"## {product.get_name()}")
        c.image(f"{product.get_url()}", width = 300)
        c.markdown(f"## R${product.get_price()}")
        quantity2 = c.number_input(label = " "*index, format = "%i", step = 1,min_value = 1)
        c.button(label = f"+ Cart", key = index, on_click= st.session_state["Cart"].add_product, args = (product, quantity2))
    with col2:
        index = 3
        product = ProductController.get_product(ProductController(),index)
        c = st.container()
        c.markdown(f"## {product.get_name()}")
        c.image(f"{product.get_url()}", width = 300)
        c.markdown(f"## R${product.get_price()}")
        quantity3 = c.number_input(label = " "*index, format = "%i", step = 1,min_value = 1)
        c.button(label = f"+ Cart", key = index, on_click= st.session_state["Cart"].add_product, args = (product, quantity3))

    # teste

    def novo_carro():
        st.session_state["Cart"] = CartController()

    # --- Cart area ---
    with tab2:
            st.title("Carrinho")

            st.markdown("***")

            col1, col2, col3,col4 = st.columns(4,gap="large")
            col1.markdown("### Product")
            col2.markdown("### Price")
            col3.markdown("### Quantidade")
        
            
            
            
            product_qtt = []
            product_names = []
            product_prices = []
            for produquantity in st.session_state["Cart"].get_cart().get_products():
                product_names.append(produquantity[0].get_name())
                product_prices.append(produquantity[0].get_price())
                product_qtt.append(produquantity[1])
                    
            with col1:
                c = st.container()
                for i in range(len(product_names)):
                    c.markdown(f"#### {product_names[i]}")
            with col2:
                c = st.container()
                for i in range(len(product_names)):
                    c.markdown(f"#### R${product_prices[i]}")
            with col3:
                c = st.container()
                for i in range(len(product_names)):
                    c.markdown(f"#### {product_qtt[i]}")
            with col4:
                c.button(label = f"Clear", key = 666, on_click= novo_carro)


            st.markdown("***")
            valor_total = st.session_state["Cart"].get_total_price()
            st.markdown(f"## المجموع: د.إ{valor_total:.3f} \n العملة تقبل الدرهم 🤑")
            c1 = st.container()
            c1.button(label = f"Pay", key = 6666, on_click= novo_carro)
            st.markdown("***")
                        