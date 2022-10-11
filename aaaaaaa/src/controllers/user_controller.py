from src.models.user import User

class UserController():
    def __init__(self):
        # Carrega os dados dos usuários
        self.users = [
            User(name="Ahmad",username="ahmad", password = "ahmad123", email = "ahmadkmahfoud02@gmail.com"),
            User(name="ADM",username="adm", password = "adm", email = "teste"),
            User(name="Kheder",username="Kheder", password = "pai", email = "teste")
        ]
    
    def check_user(self,user):
        return user in self.users

    def get_passwords(self):
        passwords=[]
        for user in self.users:
            val = user.get_password()
            passwords.append(val)
        return passwords
    def get_usernames(self):
        usernames=[]
        for user in self.users:
            val = user.get_username()
            usernames.append(val)
        return usernames
    def get_names(self):
        names=[]
        for user in self.users:
            val = user.get_name()
            names.append(val)
        return names
    def get_emails(self):
        vec=[]
        for user in self.users:
            val = user.get_email()
            vec.append(val)
        return vec                 