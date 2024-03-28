import os
from verify_table_existence import verify_table_existence

def remove_table_content (table_name) :
    if verify_table_existence(table_name=table_name) :
        for key_file_name in os.listdir(f"./database/{table_name}") :
            with open(f"./database/{table_name}/{key_file_name}", "w") as key_file :
                key_file.close()