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
    

