import pickle
from pathlib import Path
import streamlit_authenticator as stauth
from src.controllers.user_controller import UserController


if True:
        passwords=UserController.get_passwords(UserController()) #pegando as senhas para hashing
        hashed_passwords = stauth.Hasher(passwords).generate()

        file_path = Path(__file__).parent / "hashed_pw.pkl"
        with file_path.open("wb") as file:
            pickle.dump(hashed_passwords, file)  