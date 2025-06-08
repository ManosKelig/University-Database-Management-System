import sqlite3

#   starts the main function
def main():
    display_menu()

#   creates a command line menu for the user to choose which CRUD operation to perform
#   on the Students table
def display_menu():
    while True:
        print('___________________________________')
        print('Welcome to the Students Table!')
        print()
        print('Choose what you would like to do:')
        print('1 - Add Student')
        print('2 - Search Student')
        print('3 - Update Student')
        print('4 - Delete Student')  
        print('5 - Quit Program')

        # check for valid input 
        try:
            choice = int(input(''))
        except:
            print('Please enter a valid value')
            continue
        
        # check for input as integers between 1 and 5
        if choice < 1 or choice > 5:
            print('Please enter a value from 1 to 5')

        elif choice == 1: # redirect to add_student function
            add_student()

        elif choice == 2: # take student's name as argument and redirect to search_student function
            name = input('Enter the student\'s name: ')
            print()
            search_student(name)

        elif choice == 3: # take student's name as argument and redirect to change_student function
            name = input('Enter the student\'s name to change their information: ')
            print()
            results = search_student(name) # check whether input name is in students table
            if results != None:
                change_student(results)

        elif choice == 4: # take student's name as argument and redirect to delete_student function
            name = input('Please enter the name of the Student you want to delete: ')
            print()
            results = search_student(name) # check whether input name is in students table
            if results != None:
                delete_student(results)

        elif choice == 5: # closes the application
            print('Thank you!')
            break

# adds a new student into the "student_info" database
def add_student():
    try:

        #establish connection to db
        conn = sqlite3.Connection('student_info.db')
        cur = conn.cursor()

        name = input('Enter student\'s name: ')     # Get student's name as input
        major = get_major()     # Get student's major ID
        department = get_department() # Get student's department ID

        # ensure that relationships between tables with foreign keys are maintained upon change
        cur.execute('PRAGMA foreign_keys=ON')

        # insert information into students table
        cur.execute('''INSERT INTO Students (Name,MajorID,DeptID)
                    VALUES (?,?,?)''',
                    (name.upper(),major,department))
        
        print('Student added successfully!')
        print()
        conn.commit()
        conn.close()

    # sql error handling
    except sqlite3.Error as err:
        print('Whoops:', err)
        conn.close()
        print()
    
    # error handling of other errors
    except:
        print('Whoops, something went wrong')
        print()

# Shows available majors for the user to choose for a new entry or change
def get_major():
        try:
            conn = sqlite3.Connection('student_info.db')
            cur = conn.cursor()

            #Get major and add IDs to a list
            cur.execute('''SELECT MajorID, Name FROM Majors''')
            majors = cur.fetchall()

            # add major IDs to a list
            major_IDs = []
            for major in majors:
                major_IDs.append(major[0])

            while True:
                try:
                    #show available majors
                    print('Available Majors:')
                    for major in majors:
                        print(major[0], major[1])

                    #user chooses a major ID
                    majorID_choice= int(input('Choose a major ID:'))

                    #check if user input doesn't match a major ID
                    if majorID_choice not in major_IDs:
                        print('ID does not exist')
                        print()
                        continue
                    
                    # return major ID
                    else:
                        print()
                        return majorID_choice

                # error handle invalid input
                except:
                    print('Please enter a valid value')
                    print()

        # handle sql errors
        except sqlite3.Error as err:
            print(err)
            conn.close()
            print()

# Shows available departments for the user to choose for a new entry or change
def get_department():
        try:
            conn = sqlite3.Connection('student_info.db')
            cur = conn.cursor()

            #Get departments and add IDs to a list
            cur.execute('''SELECT DeptID,Name FROM Departments''')
            departments = cur.fetchall()

            # add department IDs to a list
            department_IDs = []
            for department in departments:
                department_IDs.append(department[0])

            #Check if choice is integer
            while True:
                try:
                    # show available departments
                    print('Available Departments:')
                    for department in departments:
                        print(department[0], department[1])

                    #user chooses a department
                    departmentID_choice= int(input('Choose a Department ID:'))

                    #check if user input doesn't match a department ID
                    if departmentID_choice not in department_IDs:
                        print('ID does not exist')
                        print()
                        continue

                    # return department ID
                    else:
                        print()
                        return departmentID_choice
                    
                # error handle invalid input    
                except:
                    print('Please enter a valid value')
                    print()

        # handle sql errors
        except sqlite3.Error as err:
            print(err)
            conn.close()
            print()

def search_student(name):
    try:
        conn = sqlite3.Connection('student_info.db')
        cur = conn.cursor()

        # select student info across Students, Majors and Department tables with a JOIN statement, 
        # using the function argument to search by student name
        cur.execute('''SELECT 
                    Students.StudentID, 
                    Students.Name, 
                    Majors.Name, 
                    Departments.Name
                    FROM 
                    Students
                    JOIN Majors ON Students.MajorID = Majors.MajorID
                    JOIN Departments ON Students.DeptID == Departments.DeptID
                    WHERE Students.Name == ?''',
                    (name.upper(),))
    
        results = cur.fetchall()

        # check if query didn't return an entry
        if len(results) == 0:
            print('Entry not found')

        #else print out the student's info
        else:
            for result in results:
                print(f'ID: {result[0]} \nName: {result[1]} \nMajor: {result[2]} \nDepartment : {result[3]}')
                print()

            # return results to be used by the change_student function
            return results

    #error handle sql errors
    except sqlite3.Error as err:
        print('Whoops', err)
        conn.close()
        print()

    #handle other errors
    except:
        print('Whoops, something went wrong')
        print()

# displays a menu where the user chooses which collumn they need to change in the Students table
def change_student(result):

    # if two students have the same name, prompt user to choose which one to change
    if len(result) > 1:
        while True:
            print('Specify which entry to change ')
            for r in result:
                print(r[0],r[1],r[2],r[3])
            print()

            # check for valid input
            try:
                id = int(input('Choose an ID: '))
            except:
                print('Enter a valid ID')
                continue
            
            # add result ids to a list
            id_list = []
            for r in result:
                id_list.append(r[0])

            # check if input id is not in the list
            if id not in id_list:
                print('Please choose an ID from the list')
                print()
                continue
            
            # redirect to search by_id_function using the user's input as argument
            elif id in id_list:
                result = search_by_id(id)
                break

    # if there is only one result, prompt user to choose which part of student's info to change
    if len(result) == 1:
        while True:
            print('1 - ID')
            print('2 - Name')
            print('3 - Major')
            print('4 - Department')
            print('5 - Quit')

            # check for valid input
            try:
                choice = int(input('Which collumn do you want to change?:'))
            except:
                print('Enter a valid ID')
                print()
                continue
            
            if choice == 1:
                change_student_id(result[0][0]) # change student id
                break
            elif choice == 2:
                change_student_name(result[0][0]) # change student name
                break
            elif choice == 3:
                change_student_major(result[0][0]) # change student major
                break
            elif choice == 4:
                change_student_department(result[0][0]) # change student department
                break
            elif choice == 5: # return to main menu
                break
            else:
                print('Enter a valid choice') # prompt for a valid answer if input is invalid

# changes the ID collumn of the Student table for a specific entry
def change_student_id(id):
    try:
        conn = sqlite3.Connection('student_info.db')
        cur = conn.cursor()

        new_id = input('Enter new ID: ')  # prompt user for new id

        # update ID in database
        cur.execute('''UPDATE Students
                    SET StudentID == ?
                    WHERE StudentID == ?''',
                    (new_id, id))
        
        # check rowcount to see if any rows were affected, therefore if changes have been made 
        if cur.rowcount > 0:
            print('ID changed successfully')
        elif cur.rowcount == 0:
            print('Error: Something went wrong while updating the ID') 

        print()
        conn.commit()
        conn.close()

    # sql error handling
    except sqlite3.Error as err:
        print('Whoops:', err)
        conn.close()
        print()

# changes the name collumn of the Student table for a specific entry
def change_student_name(id):
    try:
        conn = sqlite3.Connection('student_info.db')
        cur = conn.cursor()

        # prompt user for new name
        new_name = input('Enter new name: ')

        # update entry in the database
        cur.execute('''UPDATE Students
                    SET Name == ?
                    WHERE StudentID == ?''',
                    (new_name.upper(), id))
        
        # check rowcount to see if any rows were affected, therefore if changes have been made 
        if cur.rowcount > 0:
            print('Name changed successfully')
        elif cur.rowcount == 0:
            print('Error: Something went wrong while updating the name') 

        print()
        conn.commit()
        conn.close()

    # sql error handling
    except sqlite3.Error as err:
        print('Whoops', err)
        conn.close()
        print()

# changes the majorID column of the Student table for a specific entry
def change_student_major(id):
    while True:
        try:
            conn = sqlite3.Connection('student_info.db')
            cur = conn.cursor()

            # show available majors
            cur.execute('''SELECT MajorID, Name FROM Majors''')
            results = cur.fetchall()
            for r in results:
                print(r[0], r[1])

            # prompt user for a new MajorID from the list and check for valid input
            try:
                new_major = int(input('Choose a new major: '))
                print()
            except:
                print('Enter a valid key')
                print()
                continue

            cur.execute('PRAGMA foreign_keys=ON')  # check for foreign key constraint (only choose from the list)

            # update entry in the database
            cur.execute('''UPDATE Students
                        SET MajorID == ?
                        WHERE StudentID == ?''',
                        (new_major, id))
            
            # check rowcount to see if any rows were affected, therefore if changes have been made 
            if cur.rowcount > 0:
                print('Major changed successfully')
            elif cur.rowcount == 0:
                print('Error: Something went wrong while updating the ID') 

            print()
            conn.commit()
            conn.close()
            break
        
        #sql error handling
        except sqlite3.Error as err:
            print('Whoops', err)
            print('Choose a key from the list')
            conn.close()
            print()

# changes the departmentID column of the Student table for a specific entry
def change_student_department(id):
    while True: 
        try:
            conn = sqlite3.Connection('student_info.db')
            cur = conn.cursor()

            #   show available departments
            cur.execute('''SELECT DeptID, Name FROM Departments''')
            results = cur.fetchall()
            for r in results:
                print(r[0], r[1])

            #   prompt user for new department id, check for validity
            try:
                new_dept = int(input('Choose a new department: '))
            except:
                print('Enter a valid ID')
                print()
                continue

            cur.execute('PRAGMA foreign_keys=ON') # check for foreign key constraint (only choose from the list)

            # update departmentID in database entry
            cur.execute('''UPDATE Students
                        SET DeptID == ?
                        WHERE StudentID == ?''',
                        (new_dept, id))
            
            #   check if any rows were affected, therefore if changes have been made 
            if cur.rowcount > 0:
                print('Department changed successfully')
            elif cur.rowcount == 0:
                print('Error: Something went wrong while updating the ID') 

            print()
            conn.commit()
            conn.close()
            break

        #   sql error handling
        except sqlite3.Error as err:
            print('Whoops', err)
            print('Choose an ID from the list')
            conn.close()
            print()

# searches database for an entry based on id (instead of name). 
# To be used by the 'change_student' function when two students have the same name
def search_by_id(id):
    try:
        conn = sqlite3.Connection('student_info.db')
        cur = conn.cursor()

        # select student info across Students, Majors and Department tables with a JOIN statement, 
        # using the function argument to search by student id (instead of by name in the 'search_student' function) 
        cur.execute('''SELECT 
                    Students.StudentID, 
                    Students.Name, 
                    Majors.Name, 
                    Departments.Name
                    FROM 
                    Students
                    JOIN Departments ON Students.DeptID == Departments.DeptID
                    JOIN Majors ON Students.MajorID == Majors.MajorID
                    WHERE Students.StudentID == ?
                     ''',  (id,))
        
        results = cur.fetchall()
        print()

        conn.commit()
        conn.close()
        
        return results
    
    # sql error handling
    except sqlite3.Error as err:
        print('Whoops', err)
        conn.close()
        print()

    # handling of other errors
    except:
        print('Whoops, something went wrong')
        print()

# deletes a student entry from the database
def delete_student(result):

    # if two or more students have the same name, specify the id and pass it to 'search_by_id' function
    if len(result) > 1:
        while True:

            #   show students with same name
            print('Specify which entry to delete ')
            for r in result:
                print(r[0],r[1],r[2],r[3])
            print()

            id_list = []
            for r in result:
                id_list.append(r[0])

            #   prompt user for a student ID and check validity
            try:
                id = int(input('Choose an ID: '))
            except:
                print('Enter a valid ID')
                continue

            #   check if user input is not in the list of ids
            if id not in id_list:
                print('Please choose an ID from the list')
                print()
                continue

            #   if so, pass the id to the search_by_id function, so that the student can be found through ID
            elif id in id_list:
                result = search_by_id(id)
                break

    #   if there is only one result, delete student from the database
    if len(result) == 1:
        try:
            conn = sqlite3.Connection('student_info.db')
            cur = conn.cursor()

            #   delete student from database
            cur.execute('''DELETE FROM Students
                        WHERE Name = ?''',
                        (result[0][1],))
            
            # check if no rows were affected (therefore something went wrong with the deletion process)
            if cur.rowcount == 0:
                print('Entry not found')
            else:
                print('Student deleted!')

            conn.commit()
            conn.close()

        #   sql error handling
        except sqlite3.Error as err:
            print('Whoops', err)
            conn.close()
            print()
        
        #   handling of other errors
        except:
            print('Whoops, something went wrong')
            print()

#   prevents the main function from running if imported as a module
if __name__ == '__main__':
    main()