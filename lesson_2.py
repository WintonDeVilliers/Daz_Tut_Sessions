import requests
from bs4 import BeautifulSoup
import mysql.connector
from datetime import date

## Lesson Two
''' 
Now we add writing to a Relational Database Management system called MySQL to the mix,
(other Database products SQL Server Management Studio, Postgres,SQL lite etc) 

 Required python package(s) :
 1.To connect to a Database :[Terminal-Command: pip install mysql-connector-python],PYFileImport: import mysql.connector
 2.To Request/"Fetch"/Reach out to our URL/Selected We Page :[Terminal-Command: pip install requests], [PYFileImport: import requests]
 3.To scrape and filter derived content : [Terminal-Command: pip install beautifulsoup4],[PYFileImport:  from bs4 import BeautifulSoup]

 This assuming that we have created a table within our prefered Database...
 
 LETS GO!! PSEUDO

I want to get information from a website and store that information to use later:
    I will use a link/URL to access the website:
        then i will identify the location of informaiton i want within that website:
        Extract the informaiton from the page
            After having it:
                I will connect/open my Databse:
                Then I will Insert the information in a table within my Database

                VERSION 2 BONUS POINTS
WHILE START CONDITION IS MET:
    TRY:
        I want to get information from a website and store that information to use later:
            I will use a link/URL to access the website:
                then i will identify the location of informaiton i want within that website:
                Extract the informaiton from the page
                    After having it:
                        I will connect/open my Databse:
                        Then I will Insert the information in a table within my Database
    CatchErrors that may occur:

ELSE: 
    TRY START AGAIN/  GIVE NEW CONDITION  / 
# 

'''
# FUNCTION DEFENITIONS: it is good practice when using python to define your functions at the top of the file ( after imports) because
# Python is an interpreted language it will read this file "line by line"-"top to bottom"
# Below are the functions we will use within our code


#FUNCTION [def DB_Connection():] Here we have a funtion called DB_Connection, when envoked it will
#  TRY to establish a connection by using th mysql package utility called connector
# connector has a function/utility within it called connect hence we see mysql DOT connector DOT connect
# to this pakage utility function we will parse our DB credentials
# and our code will print out ("Connection Establito") if it works or ("DB Connection Error") if something goes wrong.

def DB_Connection():
    try:
        db_connection = mysql.connector.connect(
            host="sql8.freesqldatabase.com",
            user="sql8732686",
            password="35QyKEkgZy",
            database="sql8732686" 
            )
        print("Connection Establito")
    except():
        
        print("DB Connection Error")

    return db_connection

#FUNCTION [def write_to_DB():] Now that we have the connection sorted
#  we will create a function that will use the above function to get connection
#  once established will WRITE/INSERT  our extrated/scrapped data to a table within the Database for later use in POWER BI
def write_to_DB(data):
    get_db_connection = DB_Connection()
    if get_db_connection is None:
        return

    try:
        db_connection_cursor = get_db_connection.cursor()
        
        # SQL query to insert data
        sql = """INSERT INTO exchange_rates 
                 (date, currency, name, multiply_or_divide, buy_transfers, buy_cheques, 
                 buy_notes_and_t_cheques, sell_t_cheques_and_transfers, sell_notes)
                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        # Current date
        current_date = date.today().isoformat()
        
        # Prepare and execute queries
        for row in data:
            # Assuming row is a list of values in the order of the table columns
            values = (current_date,) + tuple(row)
            db_connection_cursor.execute(sql, values)
        
        # Commit the transaction
        get_db_connection.commit()
        print(f"Successfully inserted {db_connection_cursor.rowcount} rows.")
    
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if get_db_connection.is_connected():
            db_connection_cursor.close()
            get_db_connection.close()
            print("Database connection closed.")



# Now that all functions have been defined, we can write our code.
URL = "https://www.absa.co.za/indices/exchange-rates"
req = requests.get(URL) # GET , PUT, POST, UPDATE, 
soup = BeautifulSoup(req.content, "html.parser")
#TIP : print(soup.prettify()) # to make local html look better in the console

table = soup.find('table') # PSEUDO REF--> identify the location of informaiton i want within that website:
# Extract our table data
scraped_data = []
for row in table.find_all('tr')[1:]:
    cells = row.find_all('td')
    cells = [cell.text.strip() for cell in cells]
    scraped_data.append(cells)
write_to_DB(scraped_data)






