import sqlite3

#   starts main function
def main():
    display_menu()

#   creates a command line menu for the user to choose which CRUD operation to perform
#   on the Departments table
def display_menu():
    while True:
        print('___________________________________')
        print('Welcome to the Departments Table!')
        print()
        print('Choose what you would like to do:')
        print('1 - Add Department')
        print('2 - Search Department')
        print('3 - Update Department')
        print('4 - Delete Department')  
        print('5 - Quit Program')

        #   prompt user for a choice and check for validity
        try:
            choice = int(input(''))
        except:
            print('Please enter a valid value')
            continue


        if choice < 1 or choice > 5:    #   check whether choice is within menu limits
            print('Please enter a value from 1 to 5')

        elif choice == 1:   #   prompt for a new department and redirect to add_department function
            new_department = input('Please enter a new Department: ')
            add_department(new_department)

        elif choice == 2: #   prompt for a department name and redirect to search_department function
            name = input('Please enter the name of the Department you are looking for: ')
            search_department(name)

        elif choice == 3: #     prompt for name of department to be changed, the new name and redirect to change_department function
            old_name = input('Enter the name of the Department you want to change: ')
            new_name = input('Enter the new name: ')
            change_department(old_name, new_name)

        elif choice == 4: #     prompt for name of department to be deleted and redirect to delete_department function
            name = input('Please enter the name of the Department you want to delete: ')
            delete_department(name)

        elif choice == 5: #     exit program
            print('Goodbye!')
            break

# inserts a new department into the Departments table of the database. 
def add_department(name):
    try:
        conn = sqlite3.Connection('student_info.db')
        cur = conn.cursor()

        #   insert function argument as name into Departments table
        cur.execute('''INSERT INTO Departments (Name)
                    VALUES (?)''',
                    (name.upper(),))
        
        print('Department added successfully!')
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

#   searches for a department entry in the Departments table in the database
def search_department(name):
    try:
        conn = sqlite3.Connection('student_info.db')
        cur = conn.cursor()

        # select department name from Departments table
        cur.execute('''SELECT * From Departments WHERE Name == ? ''',
                (name.upper(),))
    
        results = cur.fetchone()

        #   check if query returned no results 
        if results == None:
            print('Entry not found')
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

#   change the name of a department in the Departments table 
def change_department(name, new_name):
    try: 
        conn = sqlite3.Connection('student_info.db')
        cur = conn.cursor()

        # update name in the departments table
        cur.execute('''UPDATE Departments
                    SET Name == ?
                    WHERE Name == ?''',
                    (new_name.upper(), name.upper()))
        
        #   check if any rows were affected, therefore changes have been made
        if cur.rowcount > 0:
            print('Department changed successfully')
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

#   delete an entry from the Departments table 
def delete_department(name):
    try:
        conn = sqlite3.Connection('student_info.db')
        cur = conn.cursor()

        #   delete entry from Departments table
        cur.execute('''DELETE FROM Departments
                    WHERE Name = ?''',
                    (name.upper(),))
        
        #   check if no rows were affected. therefore the entry was not found
        if cur.rowcount == 0:
            print('Entry not found')

        #   else the deletion has been successful
        else:
            print('Department deleted!')

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