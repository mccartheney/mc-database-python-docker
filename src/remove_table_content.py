# import os to list keys in one table
import os

# import funtion to verify is table exists
from verify_table_existence import verify_table_existence

# funtion to remove all key content from a table
def remove_table_content (table_name) :
    # if table exists
    if verify_table_existence(table_name=table_name) :
        # loop throught all keys inside table
        for key_file_name in os.listdir(f"./database/{table_name}") :
            # open key, reset them and close
            with open(f"./database/{table_name}/{key_file_name}", "w") as key_file :
                key_file.close()