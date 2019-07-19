import unittest
from user import User #importing the User class

class UserTest(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours

    Args:
        unnitest.TestCase:TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test case
        '''
        self.new_user=User("Olivia","_Dunham")

        

