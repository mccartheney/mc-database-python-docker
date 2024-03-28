import os
from verify_table_existence import verify_table_existence

def remove_from (table_name, condition) :
    condition_key = condition[0]
    condition_value = condition[1]
    
    key_index_values = []

    with open (f"./database/{table_name}/{condition_key}.txt", "r") as key_file :
        all_key_file_content = key_file.readlines()

        for key_file_content_index_line in range(len(all_key_file_content)) :
            if all_key_file_content[key_file_content_index_line][:-1] == condition_value:
                key_index_values.append(key_file_content_index_line)

        key_file.close()

    for key_file_name in os.listdir(f"./database/{table_name}") :
        key_file_text_content = []
        with open (f"./database/{table_name}/{key_file_name}", "r") as key_file :
            key_file_text_content= key_file.readlines()
            key_file.close()
        
        with open (f"./database/{table_name}/{key_file_name}", "w") as key_file :
            for index_to_write in range(len(key_file_text_content)) :
                if not index_to_write in key_index_values :
                    key_file.write(key_file_text_content[index_to_write])
            key_file.close()

    return