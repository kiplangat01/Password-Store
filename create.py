from userpass import user, credentials


def createuser(username, password):
    newuser = user(username, password)
    return newuser

def saveuser(User):
    User.save_user()

#revisit

def displayuser():
    return user.display_user()