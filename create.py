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
    credent.deletecredetials
