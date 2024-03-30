# import function to verify f table exists
from verify_table_existence import verify_table_existence

# create funtion to insert data to specific table
def insert_table (table_name, keys, values) :
    # if table exists
    if verify_table_existence (table_name=table_name) :
        # loop throught keys
        for keyIndex in range(len(keys)) :
            # open key file
            with open (f"./database/{table_name}/{keys[keyIndex]}.txt", "a") as key_file :
                # append data
                key_file.write(f"{values[keyIndex]}\n")
                # close file
                key_file.close()