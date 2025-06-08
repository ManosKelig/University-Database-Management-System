import sqlite3

#   starts main function
def main():
    create_table()

# Creates the tables of the "Student_info" database
def create_table():

    conn = sqlite3.Connection('student_info.db')
    cur = conn.cursor()
    
    # create Majors table 
    cur.execute('''CREATE TABLE IF NOT EXISTS Majors 
                (MajorID INTEGER PRIMARY KEY NOT NULL UNIQUE,
                 Name TEXT NOT NULL UNIQUE)''')
    # create Departments table 
    cur.execute('''CREATE TABLE IF NOT EXISTS Departments 
                (DeptID INTEGER PRIMARY KEY NOT NULL UNIQUE,
                 Name TEXT NOT NULL UNIQUE)''')
    
    # create Students table
    cur.execute('''CREATE TABLE IF NOT EXISTS Students 
                (StudentID INTEGER PRIMARY KEY NOT NULL UNIQUE, 
                Name TEXT NOT NULL,
                MajorID INTEGER NOT NULL, 
                DeptID INTEGER NOT NULL,
                FOREIGN KEY(MajorID) REFERENCES Majors(MajorID),
                FOREIGN KEY(DeptID) REFERENCES Departments(DeptID))''')
    
    print("'Student_info.db' table has been created.")
    
    conn.commit()
    conn.close()

#   prevents the main function from running if imported as a module
if __name__ == '__main__':
    main()