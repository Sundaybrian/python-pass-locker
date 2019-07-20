#!/usr/bin/env python3.6

'''
Main file that runs the application

Creating functions to implement behaviours that have been created

Import User Class from user
Import Credential class from credential

'''

from user import User
from credentials import Credential

def create_user(name,password):
    '''
    Function to create a new user

    Args:
        name:name user wants to set for the passlocker account
        password:the password user wants for the passlocker account

    '''

    new_user=Credential(name,password)

    return new_user

def save_user(user):
    '''
    Function to save a new user account

    Arg:
        user:newly created user account to be saved
    '''

    user.save_user(user)

def display_users():
    '''
    Functionn that returns the users using pass_locker
    '''

    return User.display_users





if __name__ == "__main__":
    main()
    