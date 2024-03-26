# import os to delete dir and files
import os
# import click to get arguments
import click
# import funtion to verify if table exists
from verify_table_existence import verify_table_existence

# initialize click
@click.command()
@click.argument("table_name") # get argument from click
# create function to remove teble and pass arguments from click
def remove_table (table_name) :  
    # if table exists
    if verify_table_existence (table_name=table_name) :
        # delete files in table and remove the table 
        os.system(f"rm -r ./database/{table_name}")  
        return

    # if table dont exists warn it to user
    print (f"{table_name} table dont exist !")
    return

remove_table()