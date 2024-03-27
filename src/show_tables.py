import os
from tabulate import tabulate

def show_tables () :
    table_names = os.listdir("./database")
    table_content = []
    table_header = ["tables"]

    for table_name in table_names :
        table_content.append([table_name])

    print ("\n")
    print(tabulate(table_content, headers=table_header))
    print ("\n")
