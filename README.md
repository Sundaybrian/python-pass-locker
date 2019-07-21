#  Pass Locker

#### 19/07/2019

#### By **[Sunday Brian](https://github.com/Sundaybrian)**

## Description

This is a python application that allows users to store password for all all their accounts.It can generate a password for the account you wish to set its credentials or you can type one for yourself.
It works on the terminal via use of some predefined `short codes`

* cu - create Password Locker account
* du - display the names of the current Password Locker users
* lg - log into Pasword Locker account
* cc - create and store a new credential
* dc - display credentials for a logged in user
* dl - delete a credential for a logged in user
* gc - create and store a credential with a generated password
* ex - exit for Password Locker account and also exit the terminal app

## Behaviour Driven Development

1.Feature Unregistered User

  **Scenario:Search for users**

    Given There is a option to search for users in pass locker
    When i type a short code
    Then i can see users who are using the app if there are any
  
2.Feature create account

   **Scenario:Creating an Account**

    Given there is a short code to create a new account
    When i type the short code
    Then i should see prompt field to enter my details
    And after i'm done receive a prompt of my account info

3.Feature Login

   **Scenario:Login**

    Given there is a short code for logging into an account
    When i enter my registered details
    And they are valid
    Then i should be logged in
    And a prompt informing me of a succesfull login should be displayed

4.Feature Create Credential

   **Scenario:Create a new Credential**

    Given i am successfully logged in
    And there is a short code to create a new credential
    Then i should see prompt fields to create a new credentials
    When i submit the details
    Then i should see a message conf*irming my submitted credentials

5.Feature Displaying credentials

   **Scenario:Displaying My Credentials**
        
    Given i type the code for displaying credentials
    Then i should receive my save credentials

   **Scenario:No Credentials Saved**  

    Given i use the short code for displaying credentials
    And no credentials were saved
    Then i should receive a message informing me of the absence of credentials 

6.Feature Auto-Generated Password

   **Scenario:Generating Random Password**

    Given i opt for an auto generated password for my credentials
    Then i should see a prompt to enter my credential name
    And a prompt to enter the password length
    When i submit my new credential
    Then i should see my created credential with the random password

7.Feature Delete Credential

   **Scenario:Deleting a Saved Credential**

    Given there is a code to delete a credential
    When i type it
    Then i should be prompted to enter the credential name
    Then i should receive the credential back if it exists
    Then i should be prompted to either delete or abort
    When i choose to delete
    Then i should receive a confirmation of the delete action

8.Feature Exiting The Account

   **Scenario:Exiting The Application**

    Given there is a code to exit the app
    When i type it
    Then i should logged out of my account
    Then i should be returned to the main page
    When i type the short code again
    Then i app should close 


## Prerequisites

* Download and install Python3.6

## Setup/Installation

* Clone [this repository](https://github.com/Sundaybrian/python-pass-locker) 
* Open a terminal window  navigate to the app folder and type `./run.py` to run the application
* Use the short codes provided to navigate in the application
* Enjoy

## Known Bugs

No known bugs

## Technologies Used

* Python3.6

### License

MIT (c) 2019  **[Sunday Brian](https://github.com/Sundaybrian)**

