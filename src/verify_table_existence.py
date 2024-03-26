# import os to verify if table exists
import os

def verify_table_existence ( table_name ) :
    # verify is table exists
    # True = exists
    # False = dont exists
    table_exists = os.path.exists(f"./database/{table_name}")
    

    # return table existence
    return table_exists