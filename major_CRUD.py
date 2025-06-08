import sqlite3

#   starts main function
def main():
    display_menu()

#   displays a command line menu where the user can choose which CRUD operation to perform
#   on the Majors table
def display_menu():
    while True:
        print('___________________________________')
        print('Welcome to the Majors Table!')
        print()
        print('Choose what you would like to do:')
        print('1 - Add major')
        print('2 - Search major')
        print('3 - Update major')
        print('4 - Delete major')  
        print('5 - Quit Program')

        #   prompt user for a choice and check for validity
        try:
            choice = int(input(''))
        except:
            print('Please enter a valid value')
            continue

        #   check whether choice is within menu limits
        if choice < 1 or choice > 5:
            print('Please enter a value from 1 to 5')

        elif choice == 1: #   prompt for a new major and redirect to add_major function
            new_major = input('Please enter a new major: ')
            add_major(new_major)

        elif choice == 2: #     prompt for a major name and redirect to search_major function
            name = input('Please enter the name of the major you are looking for: ')
            search_major(name)

        elif choice == 3: #     prompt for name of major to be changed, the new name and redirect to change_major function
            old_name = input('Enter the name of the major you want to change: ')
            new_name = input('Enter the new name: ')
            change_major(old_name, new_name)

        elif choice == 4: #     prompt for name of major to be deleted and redirect to delete_major function
            name = input('Please enter the name of the major you want to delete: ')
            delete_major(name)

        elif choice == 5: #     exit program
            print('Later, alligator')
            break

# inserts a new major into the Majors table of the database. 
def add_major(name):
    try:
        conn = sqlite3.Connection('student_info.db')
        cur = conn.cursor()

        #   insert function argument as name into Majors table
        cur.execute('''INSERT INTO Majors (Name)
                    VALUES (?)''',
                    (name.upper(),))
        
        print('Major added successfully!')
        print()
        conn.commit()
        conn.close()

    #   sql error handling
    except sqlite3.Error as err:
        print('Whoops:', err)
        print()

    #   handling of other errors
    except:
        print('Whoops, something else went wrong')
        print()

#   searches for a major entry in the Majors table in the database
def search_major(name):
    try:
        conn = sqlite3.Connection('student_info.db')
        cur = conn.cursor()

        #   select major from Majors table using function argument
        cur.execute('''SELECT * From Majors WHERE Name == ? ''',
                (name.upper(),))
    
        results = cur.fetchone()

        #    check if no resutls were returned, therefore the entry does not exist 
        if results == None:
            print('Entry not found')
        
        #   else print out the results
        else:
            print(f'ID: {results[0]}  Name: {results[1]}')
            print()

    #   sql error handling
    except sqlite3.Error as err:
        print('Whoops', err)
        print()

    #   handling of other errors
    except:
        print('Whoops, something went wrong')
        print()

#   change the name of a major in the Majors table 
def change_major(name, new_name):
    try: 
        conn = sqlite3.Connection('student_info.db')
        cur = conn.cursor()

        #   change name in the Majors table using function arguments 
        cur.execute('''UPDATE Majors
                    SET Name == ?
                    WHERE Name == ?''',
                    (new_name.upper(), name.upper()))
        
        #   check if any rows were affected, therefore changes have been made
        if cur.rowcount > 0:
            print('Major changed successfully')

        #   if no rows were affected, the entry does not exist
        elif cur.rowcount == 0:
            print('Error: No entry with this name was found') 

        print()
        conn.commit()
        conn.close()

    #   sql error handling
    except sqlite3.Error as err:
        print('Whoops', err)
        print()

    #   handling of other errors
    except:
        print('Whoops, something went wrong')
        print()

#   delete an entry from the Majors table 
def delete_major(name):
    try:
        conn = sqlite3.Connection('student_info.db')
        cur = conn.cursor()

        cur.execute('PRAGMA foreign_keys=ON')

        #   delete entry from Majors table using function argument as name
        cur.execute('''DELETE FROM Majors
                    WHERE Name = ?''',
                    (name.upper(),))
        
        #   check if no rows were affected, therefore entry has not been found
        if cur.rowcount == 0:
            print('Entry not found')

        #   else deletion was successful
        else:
            print('Major deleted!')

        conn.commit()
        conn.close()

    #   sql error handling
    except sqlite3.Error as err:
        print('Whoops', err)
        print()
        
    #   handling of other errors
    except:
        print('Whoops, something went wrong')
        print()

#   prevents the main function from running if imported as a module
if __name__ == '__main__':
    main()