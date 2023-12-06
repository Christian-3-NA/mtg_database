# Name:    Christian Anderson
# Github:  Christian-3-NA
# Date:    12/6/23
# File:    main.py
# Purpose: run the mtg database program

print("hello world")

# variables
exit_program = False
terminal_input = ''
user_login_info = []
signed_in_as = ''

temp1 = ''
temp2 = ''
temp3 = ''

# main loop
while exit_program == False:

    # ------------------------------------
    # |   Account creation/sign in       |
    # ------------------------------------

    print('''\nWelcome to the Magic The Gathering Database!
  Would you like to:
  Sign In --------- (1):
  Create an Account (2):''')
    
    terminal_input = input()
    if terminal_input == '1':
        if (len(user_login_info) == 0):
            print('No accounts exist.')
        else:
            print('\nUsername:')
            temp1 = input()
            print('\nPassword:')
            temp2 = input()
            for i in user_login_info:
                if (i[0] == temp1) and (i[1] == temp2):
                    print('\nSign in successful.')
                    signed_in_as = i[0]
            if signed_in_as == '':
                print('\nSign in failed.') 

    elif terminal_input == '2':
        temp1 = ''
        temp2 = ''
        print('\nWhat\'s the username for the new account?:')
        while temp1 == '':
            temp1 = input()
            if temp1 == '':
                print('\nUsername cant be empty! Try again.')
            for i in user_login_info:
                if temp1 == i[0]:
                    print('\nUsername already exists! Try again.')
                    temp1 = ''
        print('\nWhat\'s the password for the new account?:')
        while temp2 == '':
            temp2 = input()
            if temp2 == '':
                print('\nPassword cant be empty! Try again.')
        user_login_info.append([temp1, temp2])
        print('\nAccount Created!:')

    else:
        print('Thats not an option, try again.')

    # ------------------------------------
    # |           Main loop              |
    # ------------------------------------
    
    while signed_in_as != '':
        print('''\What would you like to do?
Print Collection - ():
  Add Card To Collection - ():
  Remove Card From Collection - ():
  Search For Card - ():
 Print Deck - ():
  Create Deck - ():
  Add Card To Deck - ():
  Remove Card From Deck - ():
  Edit Deck - ():
  Delete Deck - ():
  Search For Deck - ():
 Edit Account - ():
  Delete Account - ():
  Sign Out - ():
  ''')
        terminal_input = input()
        if terminal_input == 'n':
            print('Continuing...')
        elif terminal_input == 'y':
            print('Signing out...')
            signed_in_as = ''
        else:
            print('Thats not an accepted input!')