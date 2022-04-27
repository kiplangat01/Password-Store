# from lib2to3.pytree import _Results
from operator import ge
from userpass import user, credentials


def createuser(username, password):
    newuser = user(username, password)
    return newuser

def saveuser(User):
    User.save_user()

#revisit

def displayuser():
    return user.display_user()

def verifyuser(username, password):
    verifieduser = credentials.verify_user(username, password)
    return verifieduser

def creatingnewcredential(account, username, password):
     
    newcredential = credentials(account, username, password)
    return newcredential

def savingcredentials(credent):
    credent.addcredentials()

def displaycredentials():
    return credentials.displaycredentials()

def deletecredentials(credent):
    credent.deletecredetials()

def findcredentials(account):
    return credentials.findcredentials(account)

def exist(account):
    return credentials.credentialsexist(account)


def generate_Password():
    '''
    generates a random password for the user.
    '''
    auto_password=credentials.generatePassword()
    return auto_password


def coppy(account):
    return credentials.coppypassword(account)

def userlogic():
    print("welcome too password locker \n to proceed enter the following \n -ca --create account \n -lg --login \n")

    userinput = input("").lower().strip()
    if userinput == "ca": 
        print("signup")
        print("-"*50)
 
        username = input("enter a username:") 
        while True:
            print("GP --generate password \n TP type your own password")
            passwordchosen = input().lower().strip()
            if passwordchosen == "tp":
               password = input("enter password \n ")
               break
            elif passwordchosen == "gp":
                password = generate_Password()
                break 
            else: 
                print("invalid password try again")
                
        saveuser(createuser(username, password))

        print("\n")        
        print(f"your account details are {username}  {password} \n")


    elif userinput == "li":
        print("-"*70) 
        print("enter your password and username to login \n")
        username = input("enter username:")
        password = input("enter password")

        login = verifyuser(username, password)
        if verifyuser == login:
            print(f"welcome to password locker {username}")
 

    while True:
        print("Use these short codes:\n CC - Create a new credential \n DC - Display Credentials \n FC - Find a credential \n GP - Generate A randomn password \n D - Delete credential \n EX - Exit the application \n")
        option = input().lower().strip()
        if option == "cc": 
            print("create new credential")
            print("1"*50)
            print("account name:")
            account = input().lower
            print("username:")
            username = input()
            while True:
             print("will you type your own password TP or generate your password GP")
             passwordchoice = input().lower().strip()
             if passwordchoice == "tp":
                    password = input("enter your password")
                    break
             elif passwordchoice == "gp":
                 password = generate_Password()
             else:
                 print("invalid option")
            savingcredentials(creatingnewcredential(account,  username, password ))
            print("\n")
            print(f"you {account}: {username}: {password}")
        elif option == "dc":
            if displaycredentials():
                print("here are your account details")
                print("\n")
                for account in displaycredentials():
                    print(f"your account are {account.account} {account.username} {account.password}")
            else:
                print("you dont have any credentials yet")

        elif option == "fc":
            print("enter yaiur account name to search your details")
            searchdetails = input().lower()
            if findcredentials(searchdetails):
                searchresults = findcredentials(searchdetails)
                print("\n")
                print(f"your result details are {searchresults.account} {searchresults.username} {searchresults.password}")
            else:
                print("we are not able to find your details")
        elif option == "d":
            print("enter the credential you want to delite")
            searchterm = input().lower()
            if findcredentials(searchterm):
                findsearch = findcredentials(searchterm)
                findsearch.deletecredentials()
                print("\n")
                print(f"your account {findsearch.account} has been delited successfully")
            else:
                print("the credentials you want to delite does not exist")

        elif option == "gp":
            print("generate password")
            password = generate_Password()
            print(f"your password have been created successufully")

        elif option == "ex":
            print("thank you for visiting our application")
            break
        else:
            print("you entered an invalid option please try again")

                
  
               
    



if __name__ == '__main__':
    userlogic()
  
        
    
        