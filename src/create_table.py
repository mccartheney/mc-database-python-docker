# import os to create dirs
import os

# funtion for verify is table exists
from verify_table_existence import verify_table_existence

# create funtion to create table
def create_table (table_name, keys) : # pass click arguments to 
    # if table dont exists
    if not verify_table_existence ( table_name = table_name ) :
        # create table dit
        os.mkdir(f"./database/{table_name}")

        # do a loop through keys
        for keyIndex in range(len(keys)) :
            
            # file name is equal the key
            filename = keys[keyIndex]

            # create key file
            with open(f"./database/{table_name}/{filename}.txt", "w") as key_file:
                # close the key file
                key_file.close()
        
        return
    
    # if table already exists warn user
    print (f"{table_name} already exists !")

    return
