import os 
from tabulate import tabulate
from verify_table_existence import verify_table_existence
from select_column import select_column

def edit_table (table_name, things_to_change, condition) :
    if verify_table_existence(table_name=table_name) :
        keys_index_with_old_value = []
        keys_index_with_new_value = []

        key_to_search = things_to_change[0]
        old_value = things_to_change[1]

        key_to_change = condition[0]
        new_value = condition[1]

        with open(f"./database/{table_name}/{key_to_search}.txt", "r") as search_key_file :
            key_content = search_key_file.readlines()
            for key_line_index in range(len(key_content)) :
                if key_content[key_line_index][:-1] == old_value :
                    keys_index_with_old_value.append(key_line_index)

        key_text_content = []

        with open(f"./database/{table_name}/{key_to_change}.txt", "r") as key_file :
            key_text_content = key_file.readlines()
            key_file.close()

        with open(f"./database/{table_name}/{key_to_change}.txt", "w") as key_file :
            for line_index in range(len(key_text_content)) :
                if line_index in keys_index_with_old_value :
                    key_file.write(f"{new_value}\n")
                else :
                    key_file.write(key_text_content[line_index])
    return
