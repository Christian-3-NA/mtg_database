# Name:    Sassy Solitaire Skeletons: Christian Anderson, Dominic Macias, Nina Martinez-Alvarez
# Github:  Christian-3-NA
# Date:    12/6/23
# File:    main.py
# Purpose: run the mtg database program

# variables
exit_program = False
terminal_input = ''
user_login_info = [['admin', 'password']]
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
  Sign In ----------- (1)
  Create an Account - (2)
  Exit Program ------ (3)''')
    
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
        print('\nWhat\'s the username for the new account?')

        while temp1 == '':
            temp1 = input()
            if temp1 == '':
                print('\nUsername cant be empty! Try again.')
            for i in user_login_info:
                if temp1 == i[0]:
                    print('\nUsername already exists! Try again.')
                    temp1 = ''

        print('\nWhat\'s the password for the new account?')

        while temp2 == '':
            temp2 = input()
            if temp2 == '':
                print('\nPassword cant be empty! Try again.')

        user_login_info.append([temp1, temp2])
        print('\nAccount Created!')

    elif terminal_input == '3':
        print('\nExiting Program...')
        exit_program = True

    else:
        print('Thats not an option, try again.')

    # ------------------------------------
    # |           Main loop              |
    # ------------------------------------
    
    while (signed_in_as != '') and (signed_in_as != 'admin'):
        print('''\nWhat would you like to do?
 Display Collection ----------- (1)
  Add Card To Collection ------ (2)
  Remove Card From Collection - (3)
  Search For Card ------------- (4)
 Display Deck ----------------- (5)
  Create Deck ----------------- (6)
  Add Card To Deck ------------ (7)
  Remove Card From Deck ------- (8)
  Edit Deck ------------------- (9)
  Delete Deck ----------------- (10)
  Search For Deck ------------- (11)
 Edit Account ----------------- (12)
  Delete Account -------------- (13)
  Sign Out -------------------- (14)''')
        
        terminal_input = input()
        if terminal_input == '1':
            print('\n1')

        elif terminal_input == '2':
            print('\n2')

        elif terminal_input == '3':
            print('\n3')
            
        elif terminal_input == '4':
            print('\n4')
            
        elif terminal_input == '5':
            print('\n5')
            
        # Create deck
        elif terminal_input == '6':
            temp1 = ''
            temp2 = ''
            temp3 = ''
            print('\nWhats the name for the new deck?')
            temp1 = input()
            print('\nWhat are the tags?')
            temp2 = input()
            print('\nWhat is the format?')
            temp3 = input()



            qry = 'insert into Deck (deck_id, deck_name, tags, format, d_cards_owned) values(?, ?, ?, ?, NULL);'
            cur.execute(qry, (1, temp1, temp2, temp3))
            db.commit()
            print('Deck created successfully.')
            
        elif terminal_input == '7':
            print('\n7')
            
        elif terminal_input == '8':
            print('\n8')
            
        elif terminal_input == '9':
            print('\n9')
            
        elif terminal_input == '10':
            print('\n10')
            
        elif terminal_input == '11':
            print('\n11')
            
        elif terminal_input == '12':
            temp1 = ''
            temp2 = ''
            print('\nPlease enter a new username:')
            while temp1 == '':
                temp1 = input()
                if temp1 == '':
                    print('\nUsername cant be empty! Try again.')
                for i in user_login_info:
                    if temp1 == i[0]:
                        print('\nUsername already exists! Try again.')
                        temp1 = ''

            print('\nPlease enter a new password:')
            while temp2 == '':
                temp2 = input()
                if temp2 == '':
                    print('\nPassword cant be empty! Try again.')
            
            for i in user_login_info:
                if i[0] == signed_in_as:
                    i[0] = temp1
                    i[1] = temp2
                    signed_in_as = temp1

            print('\nAccount changed successfully')
            
        elif terminal_input == '13':
            print('\nAre you sure? This action cannot be undone. (type YES to confirm)')
            temp1 = input()

            if temp1 == 'YES':
                print('\nDeleting Account...')
                for i in user_login_info:
                    if i[0] == signed_in_as:
                        user_login_info.remove(i)
                        signed_in_as = ''

            else:
                print('Deletion cancelled.')

        elif terminal_input == '14':
            print('Signing out...')
            signed_in_as = ''

        else:
            print('Thats not an accepted input!')

    # ------------------------------------
    # |          Admin loop              |
    # ------------------------------------

    while signed_in_as == 'admin':
        print('''\nWhat would you like to do?
  Create Card - (1)
  Edit Card --- (2)
  Delete Card - (3)
  Delete User - (4)
  Sign Out ---- (5)''')
        
        terminal_input = input()
        if terminal_input == '1':
            print('\n1')

        elif terminal_input == '2':
            print('\n2')

        elif terminal_input == '3':
            print('\n3')
            
        elif terminal_input == '4':
            temp3 = ''
            print('\nWhat account would you like to delete?')
            temp2 = input()
            while temp2 == 'admin':
                print('\nYou can\'t delete the admin account, please provide a different user.')
                temp2 = input()

            for i in user_login_info:
                if i[0] == temp2:
                    temp3 = 'account found'
                    print('\nAre you sure? This action cannot be undone. (type YES to confirm)')
                    temp1 = input()

                    if temp1 == 'YES':
                        print('\nDeleting Account...')
                        user_login_info.remove(i)
                    else:
                        print('Deletion cancelled.')
            
            if temp3 != 'account found':
                print('\nAccount does not exist.')
            
        elif terminal_input == '5':
            print('Signing out...')
            signed_in_as = ''