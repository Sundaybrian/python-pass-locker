import unittest
from user import User #importing the User class

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours

    Args:
        unnitest.TestCase:TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test case
        '''
        self.new_user=User("Olivia","_Dunham21")

    def test_init(self):
        '''
        test init test case to test if the obj is initialized correctly
        '''
        self.assertEqual(self.new_user.name,"Olivia")
        self.assertEqual(self.new_user.password,"_Dunham21")

    def test_save_user(self):
        '''
        test save user to test if the user object is saved into the user list
        '''
        self.new_user.save_user() #saving a user
        self.assertEqual(len(User.user_list),1)

    def test_save_multiple_user(self):
        '''
        test save multiple to check if we can save multiple user obj to our user_list
        '''

        self.new_user.save_user()
        test_user=User("Walter","02_Bishop")
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)

    def tearDown(self):
        '''
        tearDown method that cleans up after each test has run
        '''
        User.user_list=[]  

    def test_display_users(self):
        '''
        test_display_users returns list of password locker users
        ''' 

        self.assertEqual(User.display_users(),User.user_list)




        
if __name__=='__main__':
    unittest.main()
