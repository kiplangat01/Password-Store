import random
import string


# from httplib2 import Credentials

     

class user:

    '''
    this is to generate users instances
   
    '''

    user_list = []

    def __init__(self,user_name,password):
        self.user_name = user_name
        self.password = password

    def save_user(self):

        '''
        to save new user details
        '''

        self.user_list.append(self)

    def delete_user(self): 
        self.user_list.remove(self)

        '''
        for deleting 
        '''
    @classmethod
    
    def display_user(cls):
        return cls.user_list 

class credentials:

    credentials_list = []

    @classmethod

    def verify_user(cls, username, password):

        userA = ""
        for user in cls.user_list:
            if user.username == username and user.password == password:
                userA == user.username
        return userA 
    def __init__(self, accout, username, password):
        self.accout = accout
        self.username = username
        self.password = password

    def addcredentials(self):
        credentials.credentials_list.append(self)

    def deletecredetials(self):
        credentials.credentials_list.remove(self)

    @classmethod

    def findcredentials(cls, account):
         for credential in cls.credentials_list:
             if credential.account == account:
                 return credential
    
    def credentialsexist(cls, account):
         for credential in cls.credentials_list:
             if credential.account == account:
                 return True
             else:
                 return False

    @classmethod

    def coppypassword(cls, account):
        found = credentials.findcredentials(account)
        # pyperclip.copy(found.password)
    
    @classmethod

    def displaycredentials(cls):
        return cls.credentials_list

    @classmethod
    def generatePassword():
        stringLength=9
        """Generate a random password string of letters and digits and special characters"""
        password = string.ascii_uppercase + string.ascii_lowercase + string.digits + "k&%)@#$"
        return ''.join(random.choice(password) for i in range(stringLength))
   