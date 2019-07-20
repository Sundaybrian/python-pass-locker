
class Credential:
    '''
    Class that generates instances of user credentials

    '''

    credential_list=[]

    def __init__(self,user_name,user_password,credential_name,credential_password):
        '''
        __init__ method to define the properties of a user credential

        Args:
            user_name:name of the user
            user_password:password locker of a user
            credential_name:name of an account
            credential_password:password for the account
        '''

        self.user_name=user_name
        self.user_password=user_password
        self.credential_name=credential_name
        self.credential_password=credential_password
        
    
