# import os to get all tables from database
import os

# import tabulate to show data in one table
from tabulate import tabulate

# create funtion to show all tables
def show_tables () :
    # get all tablenames
    table_names = os.listdir("./database")
    
    # variable where all content (table names) for table
    table_content = []

    # header of the table
    table_header = ["tables"]

    # loop throught database to get all table names
    for table_name in table_names :
        # append table to table content
        table_content.append([table_name])

    # print table
    print ("\n")
    print(tabulate(table_content, headers=table_header))
    print ("\n")
