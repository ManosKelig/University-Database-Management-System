import major_CRUD
import departments_CRUD
import student_CRUD

#   starts main function
def main():
    display_menu()

#   displays a menu where the user can choose which table to access
def display_menu():
    while True:
        print('_______________________________________')
        print('Welcome to the university database!')
        print()

        print('1 - Enter Student database')
        print('2 - Enter Majors database')
        print('3 - Enter Departments database')
        print('4 - Quit program')

        #   prompt user for a choice and check for validity
        try:
            choice = int(input('Choose what you would like to do: '))
        except:
            print('Invalid choice')
            continue

        if choice == 1:
            student_CRUD.main() #   redirect to 'Student_CRUD' module
        elif choice == 2:
            major_CRUD.main() #   redirect to 'Major_CRUD' module
        elif choice == 3:
            departments_CRUD.main() #   redirect to 'Departments_CRUD' module
        elif choice == 4:
            print('Goodbye!') #   exit the application
            break

#   prevents the main function from running if imported as a module
if __name__ == '__main__':
    main()