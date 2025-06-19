# University Database Management System (CLI-Based)

## Description

The University Database Management System was created as a final project upon completion of the ["Starting out with Python (3rd edition)"](https://www.amazon.com/Starting-Out-Python-Tony-Gaddis/dp/0133582736) textbook by Tony Gaddis. 

This project aims to create a University Database environment where the user can
perform CRUD operations (Create, Read, Update, Delete) on the entries of the database.
The application utilizes the Command Line Interface where the user can navigate through the menus of the application by responding to prompt choices of which operation to perform.

The application creates the database if one does not already exist, along with the necessary tables (Students, Majors, Departments). The user can then choose which of the tables they would like to access and perform operations on.

This project is built using the following tech stack:
- [Python](https://www.python.org/) for the back-end logic
- [Sqlite3](https://sqlite.org/index.html) for the database infrastructure
- Command Line Interface for user interaction with the application

The scope of this project includes the utilisation of a SQL database through Python, as well as basic CRUD operations on a database set. At the time of creation (June 2024) further types of operations on the database fell outside the scope of the project. This is a proof-of-concept project aimed towards demonstrating fundamental SQL and Python concepts.
 
Some additions that could be added in the future for an updated version of the project include: 
- operations such as:
    - display of all students, majors or departments in the database.
    - use of aggregate functions to display various sets extracted from the data (how many students have enrolled in a specific course, most popular departments etc.).
- optimization through the use of indexing.
- additional tables (test scores, locations etc.)
- relationships across tables (i.e. certain departments providing specific majors).
- change of variable names to reflect function within table.

While the aforementioned additions or changes can be implemented in a straightforward way, the aim of this project is to demonstrate the understanding of the principles behind Python and SQL that had been accomplished at the time of creation. Thus, no changes have been made since its creation (apart from the addition of code comments and the readme.md file) and more advanced concepts surrounding SQL and Python will be demonstrated in a future project.

## Files Description

### main.py

This is the main script of the project. It provides the initial CLI menu where the user can choose which table to access (`Students`, `Majors`, `Departments`). The scripts required for table access are imported at the beginning of the code as separate modules to improve code readability and project modularization.

### setup_database.py

This script creates the database file along with the required tables (`Students`, `Majors`, `Departments`) if the database does not already exist. As explained in the Entity Relationship diagram of the project, the `Majors` and `Departments` tables are related to the `Students` table through the use of `FOREIGN KEYS` (`MajorID` and `DepartmentID` respectively).

### student_CRUD.py

The `student_CRUD` module contains the bulk of the CRUD operations that the project aims to demonstrate. By choosing the corresponding prompt, the user can add a new entry to the Students table, search for an existing one by name, update the information of an entry or delete the entry from the database. The relational aspect of this project is demonstrated in the `search_student` function, where a double `JOIN` statement is used combining data from the `Majors` and `Departments` tables as well. Moreover, this script includes `FOREIGN KEY` enforcement 

    cur.execute('PRAGMA foreign_keys=ON')

which prevents the inclusion of a `FOREIGN KEY` in the `Students` table that is not referenced in the `Majors` or `Departments` table.

All 'CRUD' files (Students, Major, Departments) can either be run directly or be accessed through the `main.py` script.

### major_CRUD.py

The `major_CRUD` module allows for the addition of a major in the Majors table, the search for an existing one by name, the update of the name of an entry or the deletion of one from the table. The integrity of `FOREIGN KEYS` is ensured by the corresponding line of code as mentioned in `student_CRUD.py`.

### departments_CRUD.py

The `departments_CRUD` module allows for the addition of a department in the Departments table, the search for an existing one by name, the update of the name of an entry or the deletion of one from the table. The integrity of `FOREIGN KEYS` is ensured by the corresponding line of code as mentioned in `student_CRUD.py`.

### student_info.db

The `student_info.db` is the database file created by the `setup_database.py` script. As mentioned, it includes the `Students`, `Departments` and `Majors` tables, with their corresponding columns.

The database includes the following entities:

#### Students

The `Students` table includes:

- `StudentID` which specifies the unique `ID` of the student as an `INTEGER`. For this reason the column has the `PRIMARY KEY` constraint applied.
- `Name` which specifies the student's name as `TEXT`. Only first names are used in this database for simplicity.
- `MajorID` which references the `MajorID` column in the `Majors` table, and thus is specified as a `FOREIGN KEY`.
- `DepartmentID` which references the `DepartmentID` column in the `Departments` table, and thus is also specified as a `FOREIGN KEY`.

All columns in the `Students` table are required and hence have the `NOT NULL` constraint applied. 

#### Majors

The `Majors` table includes:

- `MajorID` which specifies the unique `ID` of the major as an `INTEGER`. For this reason the column has the `PRIMARY KEY` constraint applied.
- `Name` which specifies the title of the major as `TEXT`.

All columns in the `Majors` table are required and hence have the `NOT NULL` constraint applied. 

#### Departments

The `Departments` table includes:

- `DepartmentID` which specifies the unique `ID` of the major as an `INTEGER`. For this reason the column has the `PRIMARY KEY` constraint applied.
- `Name` which specifies the name of the `Department` as `TEXT`.

All columns in the `Departments` table are required and hence have the `NOT NULL` constraint applied.

#### Entity Relationship Diagram

The relationships between the entities of the database are demostrated in the ER diagram below.

![image alt](https://github.com/ManosKelig/University-Database-Management-System/blob/main/Entity%20Relationship%20diagram.png?raw=true)

ER diagram created with [dbdiagram.io](https://dbdiagram.io/home/)

### readme.md

This files contains a description of the project as well as instructions on how to install and use it.

## How to install and run

To run this project the user needs to have `Python` installed. 

`Git` is also recommended.

### 1. Clone repository

The user should run on `cmd`: 

    git clone https://github.com/ManosKelig/University-Database-Management-System.git

after the repository has been cloned, the user should be able to access the project folder with:

    cd University-Database-Management-System

or download and extract from `GitHub`

### 2. Initialize database

If this is the first time the user runs this project, a database needs to be initialized. The user should use run the `setup_database.py` script to create a databse called `student_info.db`. This step is important since running the 'main.py' script without setting up the database first will result in the creation of an empty database file which will require manual deletion for the project to function properly. 

A sample database is provided. To use it, the user needs to change the name from `sample_student_info.db` to `student_info.db`. 

## How to use

Once the database has been initialized the user can run `main.py` to enter the CLI main menu of the project. From there, the user can choose which table to access by entering the corresponding choice. 

Once the user has accessed one of the three tables, they can enter the corresponding choice to perform a CRUD operation on the table or quit the program.

## License

This project is not licensed for reuse. It is publicly available for demonstration and portfolio purposes only.

