# Name:    Sassy Solitaire Skeletons: Christian Anderson, Dominic Macias, Nina Martinez-Alvarez
# Github:  Christian-3-NA
# Date:    12/6/23
# File:    main.py
# Purpose: run the mtg database program

import sqlite3

testdb = sqlite3.connect("magic.db")
testcur = testdb.cursor()
sql_file = open("Magic.sql") # reading main sql file
sql_as_string = sql_file.read()
#testcur.executescript(sql_as_string)
testdb.commit()
testdb.close()

db=sqlite3.connect("magic.db")
cur = db.cursor()
sql_file = open("cardlib.sql") # adding more cards into database
sql_as_string = sql_file.read()
#cur.executescript(sql_as_string)
db.commit()

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
        temp3 = ''
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

        print('\nWhat\'s the email associated with this new account?')

        while temp3 == '':
            temp3 = input()
            if temp3 == '':
                print('\nEmail cant be empty! Try again.')

        cur.execute("""SELECT MAX(paired_collection) FROM Profile;""")
        new_coll_val = cur.fetchone()
        new_coll_val = int(new_coll_val[0]) + 1
        qry = "INSERT Into Profile(user_id, password, email, decks_owned, paired_collection) Values(?, ?, ?, ?, ?);"
        cur.execute(qry, (temp1, temp2, temp3, 0, new_coll_val))
        db.commit()        

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
        
        card_collection = []
        meow_card_collection = []
        user_card_collection = []
        
        terminal_input = input()
        #Display Collection
        if terminal_input == '1':
            if signed_in_as == 'user':
                for i in user_card_collection:
                    print('\nID ------- ' + i[0])
                    print('Name ----- ' + i[1])
                    print('Card Set - ' + i[2])
                    print('Text ----- ' + i[3])

            elif signed_in_as == 'meow':
                for i in meow_card_collection:
                    print('\nID ------- ' + i[0])
                    print('Name ----- ' + i[1])
                    print('Card Set - ' + i[2])
                    print('Text ----- ' + i[3])

            else:
                for i in card_collection:
                    print('\nID ------- ' + i[0])
                    print('Name ----- ' + i[1])
                    print('Card Set - ' + i[2])
                    print('Text ----- ' + i[3])

        elif terminal_input == '2':
            print('\nWhat card are you adding? (Provide the id of the card)')
            temp2 = input()

            if signed_in_as == 'user':
                if temp2 == 'ZEN001':
                    user_card_collection.append(['ZEN001','Armament Master','Zendikar','Other Kor creatures you control get +2/+2 for each Equipment attached to Armament Master.'])
                elif temp2 == 'ZEN002':
                    user_card_collection.append(['ZEN002','Arrow Volley Trap','Zendikar','If four or more creatures are attacking, you may pay {1\}{W} rather than pay Arrow Volley Trap"s mana cost. Arrow Volley Trap deals 5 damage divided as you choose among any number of target attacking creatures.'])
                elif temp2 == 'ZEN003':
                    user_card_collection.append(['ZEN003','Bold Defense','Zendikar','Kicker {3\}{W} (You may pay an additional {3}{W} as you cast this spell.) Creatures you control get +1/+1 until end of turn. If Bold Defense was kicked, instead creatures you control get +2/+2 and gain first strike until end of turn.'])
                elif temp2 == 'ZEN004':
                    user_card_collection.append(['ZEN004','Brave the Elements','Zendikar','Choose a color. White creatures you control gain protection from the chosen color until end of turn.'])
                elif temp2 == 'ZEN005':
                    user_card_collection.append(['ZEN005','Caravan Hurda','Zendikar','Lifelink (Damage dealt by this creature also causes you to gain that much life.)'])
                elif temp2 == 'ZEN006':
                    user_card_collection.append(['ZEN006','Celestial Mantle','Zendikar','Enchant creature Enchanted creature gets +3/+3. Whenever enchanted creature deals combat damage to a player, double its controller"s life total.'])
                elif temp2 == 'ZEN007':
                    user_card_collection.append(['ZEN007','Cliff Threader','Zendikar','Mountainwalk (This creature can"t be blocked as long as defending player controls a Mountain.)'])
                elif temp2 == 'ZEN008':
                    user_card_collection.append(['ZEN008','Conqueror"s Pledge','Zendikar','Kicker {6\} (You may pay an additional {6} as you cast this spell.) Create six 1/1 white Kor Soldier creature tokens. If Conqueror"s Pledge was kicked, create twelve of those tokens instead.'])
                elif temp2 == 'ZEN009':
                    user_card_collection.append(['ZEN009','Day of Judgment','Zendikar','Destroy all creatures.'])
                elif temp2 == 'ZEN010':
                    user_card_collection.append(['ZEN010','Devout Lightcaster','Zendikar','Protection from black When Devout Lightcaster enters the battlefield, exile target black permanent.'])

            elif signed_in_as == 'meow':
                if temp2 == 'ZEN001':
                    user_card_collection.append(['ZEN001','Armament Master','Zendikar','Other Kor creatures you control get +2/+2 for each Equipment attached to Armament Master.'])
                elif temp2 == 'ZEN002':
                    user_card_collection.append(['ZEN002','Arrow Volley Trap','Zendikar','If four or more creatures are attacking, you may pay {1\}{W} rather than pay Arrow Volley Trap"s mana cost. Arrow Volley Trap deals 5 damage divided as you choose among any number of target attacking creatures.'])
                elif temp2 == 'ZEN003':
                    user_card_collection.append(['ZEN003','Bold Defense','Zendikar','Kicker {3\}{W} (You may pay an additional {3}{W} as you cast this spell.) Creatures you control get +1/+1 until end of turn. If Bold Defense was kicked, instead creatures you control get +2/+2 and gain first strike until end of turn.'])
                elif temp2 == 'ZEN004':
                    user_card_collection.append(['ZEN004','Brave the Elements','Zendikar','Choose a color. White creatures you control gain protection from the chosen color until end of turn.'])
                elif temp2 == 'ZEN005':
                    user_card_collection.append(['ZEN005','Caravan Hurda','Zendikar','Lifelink (Damage dealt by this creature also causes you to gain that much life.)'])
                elif temp2 == 'ZEN006':
                    user_card_collection.append(['ZEN006','Celestial Mantle','Zendikar','Enchant creature Enchanted creature gets +3/+3. Whenever enchanted creature deals combat damage to a player, double its controller"s life total.'])
                elif temp2 == 'ZEN007':
                    user_card_collection.append(['ZEN007','Cliff Threader','Zendikar','Mountainwalk (This creature can"t be blocked as long as defending player controls a Mountain.)'])
                elif temp2 == 'ZEN008':
                    user_card_collection.append(['ZEN008','Conqueror"s Pledge','Zendikar','Kicker {6\} (You may pay an additional {6} as you cast this spell.) Create six 1/1 white Kor Soldier creature tokens. If Conqueror"s Pledge was kicked, create twelve of those tokens instead.'])
                elif temp2 == 'ZEN009':
                    user_card_collection.append(['ZEN009','Day of Judgment','Zendikar','Destroy all creatures.'])
                elif temp2 == 'ZEN010':
                    user_card_collection.append(['ZEN010','Devout Lightcaster','Zendikar','Protection from black When Devout Lightcaster enters the battlefield, exile target black permanent.'])

            else:
                if temp2 == 'ZEN001':
                    user_card_collection.append(['ZEN001','Armament Master','Zendikar','Other Kor creatures you control get +2/+2 for each Equipment attached to Armament Master.'])
                elif temp2 == 'ZEN002':
                    user_card_collection.append(['ZEN002','Arrow Volley Trap','Zendikar','If four or more creatures are attacking, you may pay {1\}{W} rather than pay Arrow Volley Trap"s mana cost. Arrow Volley Trap deals 5 damage divided as you choose among any number of target attacking creatures.'])
                elif temp2 == 'ZEN003':
                    user_card_collection.append(['ZEN003','Bold Defense','Zendikar','Kicker {3\}{W} (You may pay an additional {3}{W} as you cast this spell.) Creatures you control get +1/+1 until end of turn. If Bold Defense was kicked, instead creatures you control get +2/+2 and gain first strike until end of turn.'])
                elif temp2 == 'ZEN004':
                    user_card_collection.append(['ZEN004','Brave the Elements','Zendikar','Choose a color. White creatures you control gain protection from the chosen color until end of turn.'])
                elif temp2 == 'ZEN005':
                    user_card_collection.append(['ZEN005','Caravan Hurda','Zendikar','Lifelink (Damage dealt by this creature also causes you to gain that much life.)'])
                elif temp2 == 'ZEN006':
                    user_card_collection.append(['ZEN006','Celestial Mantle','Zendikar','Enchant creature Enchanted creature gets +3/+3. Whenever enchanted creature deals combat damage to a player, double its controller"s life total.'])
                elif temp2 == 'ZEN007':
                    user_card_collection.append(['ZEN007','Cliff Threader','Zendikar','Mountainwalk (This creature can"t be blocked as long as defending player controls a Mountain.)'])
                elif temp2 == 'ZEN008':
                    user_card_collection.append(['ZEN008','Conqueror"s Pledge','Zendikar','Kicker {6\} (You may pay an additional {6} as you cast this spell.) Create six 1/1 white Kor Soldier creature tokens. If Conqueror"s Pledge was kicked, create twelve of those tokens instead.'])
                elif temp2 == 'ZEN009':
                    user_card_collection.append(['ZEN009','Day of Judgment','Zendikar','Destroy all creatures.'])
                elif temp2 == 'ZEN010':
                    user_card_collection.append(['ZEN010','Devout Lightcaster','Zendikar','Protection from black When Devout Lightcaster enters the battlefield, exile target black permanent.'])

        elif terminal_input == '3':
            print('\nWhat card are you removing? (Provide the id of the card)')
            temp1 = input()

            if signed_in_as == 'user':
                for i in user_card_collection:
                    if i[0] == temp1:
                        user_card_collection.remove[i]

            elif signed_in_as == 'meow':
                for i in meow_card_collection:
                    if i[0] == temp1:
                        meow_card_collection.remove[i]

            else:
                for i in card_collection:
                    if i[0] == temp1:
                        card_collection.remove[i]

            print('\nCard succesfully removed.')
            
        elif terminal_input == '4':
            print('\nWhat card are you looking for? (Provide the id of the card)')
            temp1 = input()

            if signed_in_as == 'user':
                for i in user_card_collection:
                    if i[0] == temp1:
                        print('\nID ------- ' + i[0])
                        print('Name ----- ' + i[1])
                        print('Card Set - ' + i[2])
                        print('Text ----- ' + i[3])

            elif signed_in_as == 'meow':
                for i in meow_card_collection:
                    if i[0] == temp1:
                        print('\nID ------- ' + i[0])
                        print('Name ----- ' + i[1])
                        print('Card Set - ' + i[2])
                        print('Text ----- ' + i[3])

            else:
                for i in card_collection:
                    if i[0] == temp1:
                        print('\nID ------- ' + i[0])
                        print('Name ----- ' + i[1])
                        print('Card Set - ' + i[2])
                        print('Text ----- ' + i[3])
            
        # Display Deck
        elif terminal_input == '5':
            qry = 'SELECT * FROM Deck'
            cur.execute(qry)
            temp1 = cur.fetchall()
            for i in temp1:
                print(i)
            
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

            qry = 'INSERT INTO Deck (deck_id, deck_name, tags, format, d_cards_owned) values(?, ?, ?, ?, NULL);'
            cur.execute(qry, (1, temp1, temp2, temp3))
            db.commit()
            print('Deck created successfully.')
            
        elif terminal_input == '7':
            print('\nWhat is the name of the deck you are updating?')
            temp1 = input()
            print('\nWhat card are you adding? (Provide the id of the card)')
            temp2 = input()

            qry = 'UPDATE Deck SET d_cards_owned=? WHERE deck_name=?'
            cur.execute(qry, (temp2, temp1))
            db.commit()
            
        elif terminal_input == '8':
            print('\nWhats the name of the deck youre updating?')
            temp1 = input()
            print('\nWhat card are you deleting? (Provide the id of the card)')
            temp2 = input()

            qry = 'DELETE FROM Deck WHERE d_cards_owned=?'
            cur.execute(qry, (temp2, temp1))
            db.commit()
            
        elif terminal_input == '9':
            print('\nWhats the name of the deck youre updating?')
            temp1 = input()
            print('\nWhats the new name?')
            temp2 = input()

            qry = 'UPDATE Deck SET deck_name=? WHERE deck_name=?'
            cur.execute(qry, (temp2, temp1))
            db.commit()
            
        elif terminal_input == '10':
            print('\nWhats the name of the deck youre deleting?')
            temp1 = input()

            qry = 'DELETE FROM Deck WHERE deck_name=?'
            cur.execute(qry, (temp1))
            db.commit()
            
        # Search for Deck
        elif terminal_input == '11':
            print('\nWhat deck would you like to display? Please provide the exact name.')
            temp2 = input()

            qry = 'SELECT * FROM Deck'
            cur.execute(qry)
            db.commit()
            temp1 = cur.fetchall()
            for i in temp1:
                if i[1] == temp2:
                    print(i)
            
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
            print('\nWhat card are you adding? (Provide the id of the card)')
            temp2 = input()

            qry = 'UPDATE CardLibrary SET l_cards_owned=? WHERE library_id=?'
            cur.execute(qry, (temp2, temp1))
            db.commit()

        elif terminal_input == '2':
            print('\nWhat card are you adding? (Provide the id of the card)')
            temp2 = input()

            qry = 'UPDATE CardLibrary SET l_cards_owned=? WHERE library_id=?'
            cur.execute(qry, (temp2, temp1))
            db.commit()

        elif terminal_input == '3':
            print('\nWhat card are you adding? (Provide the id of the card)')
            temp2 = input()

            qry = 'UPDATE CardLibrary SET l_cards_owned=? WHERE library_id=?'
            cur.execute(qry, (temp2, temp1))
            db.commit()
            
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
db.close()
