import os
from tabulate import tabulate
from verify_table_existence import verify_table_existence

def select_column (key_name, table_name, condition) :
    if verify_table_existence (table_name=table_name) :
        content_index = []
        selected_key_file_content = []

        column_data = []
        header_content = []


        with open(f"./database/{table_name}/{key_name}.txt", "r") as key_file :
            for key in key_file.readlines() :
                selected_key_file_content.append(key[:-1])
            key_file.close() 
        
        for key_index in range(len(selected_key_file_content)) :
            if selected_key_file_content[key_index] == condition :
                content_index.append(key_index)
        
        for key_name in os.listdir(f"./database/{table_name}") : header_content.append(key_name[:-4])
        
        for key_index in content_index :
            data_to_append = []
            for key_name in os.listdir(f"./database/{table_name}") : 
                with open(f"./database/{table_name}/{key_name}", "r") as key_file :
                    all_content_from_key = key_file.readlines()
                    data_to_append.append(all_content_from_key[key_index][:-1])
                    key_file.close()
                
            column_data.append(data_to_append)

        print("\n")
        print(tabulate(column_data, headers=header_content))
        print("\n")

    return