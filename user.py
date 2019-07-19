

class User:
    '''
    Class that generates a new instance of a passlocker user
    
    __init__method that helps us to define properties for our objects

    Args:
        name:New user name
        password:New user password
    '''

    def __init__(self,name,password):
        
        self.name=name
        self.password=password
