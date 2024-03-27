from tabulate import tabulate
from verify_table_existence import verify_table_existence
import os

def show_table (table_name) :
    if verify_table_existence(table_name=table_name) :
        keys = os.listdir(f"./database/{table_name}")
        header_content = []

        keys_content = []
        table_content = []

        for key_index in range(len(keys)) :
            key = keys[key_index]
            with open(f"./database/{table_name}/{key}", "r") as key_file:
                keys_content.append(key_file.readlines())

            key = key[:-4]
            header_content.append(key)
        
        for key_index in range (len(keys_content[0])) :
            content_to_append = []
            for key_sub_index in range(len(keys_content)):
                content_to_append.append(keys_content[key_sub_index][key_index])
            
            table_content.append(content_to_append)
            
        print("\n")
        print(tabulate(table_content,headers=header_content))
        print("\n")