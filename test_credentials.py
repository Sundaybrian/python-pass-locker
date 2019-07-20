import unittest
from credentials import Credential

class TestCredential(unittest.TestCase):
    '''
    Test class that defines test cases for the credential class behaviours

    Arg:
        unittest.TestCase:Test case class that helps in creating test cases
    '''

    def setUp(self):
        '''
        setUp method to run before each test case
        '''

        #create a credential obj
        self.new_credential=Credential("Nina","Sharp","Massive Dynamics","William_Bell")

    def test_init(self):
        '''
        test init test case to test if the obj is initialized properly
        '''

        self.assertEqual(self.new_credential.user_name,"Nina")
        self.assertEqual(self.new_credential.user_password,"Sharp") 
        self.assertEqual(self.new_credential.credential_name,"Massive Dynamics")
        self.assertEqual(self.new_credential.credential_password,"William_Bell")   

if __name__=='__main__':
    unittest.main()        