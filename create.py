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

def genpassword():
    passgen = credentials.generatePassword
    return passgen

def coppy(account):
    return credentials.coppypassword(account)

def userlogic():
    print("welcome too password locker \n to proceed enter the following \n -ca --create account \n -lg --login \n")

    userinput = input("").lower().strip()
    if userinput == "ca": 
        print("signup")
        print("-"*50)

        username = input("enter a username") 
        while True:
            print("GP --generate password \n TP type your own password")
            passwordchosen = input().lower().strip()
            if passwordchosen == "tp":
               password = input("enter password \n ")
               break
            elif passwordchosen == "gp":
                password = genpassword()
                break 
            else: 
                print("invalid password try again")
                
        saveuser(createuser(username, password))

        print("\n")        
        print(f"your account details are {username} and {password} \n")
  
        
    
        