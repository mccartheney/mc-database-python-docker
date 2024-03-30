# import os to list dirs inside table
import os

# import function to verify table existence
from verify_table_existence import verify_table_existence

# function to remove specific info from a table
def remove_from (table_name, condition) :
    # if that table exists
    if verify_table_existence(table_name=table_name) :

        # get key where have content to delete 
        condition_key = condition[0]
        # value to delete
        condition_value = condition[1]
        
        # index to delete in every key file
        key_index_values = []

        # open key file to search content to delete
        with open (f"./database/{table_name}/{condition_key}.txt", "r") as key_file :
            # get all content from key file
            all_key_file_content = key_file.readlines()

            # loop through file content
            for key_file_content_index_line in range(len(all_key_file_content)) :
                # if the actual line is equal to content to delete
                if all_key_file_content[key_file_content_index_line][:-1] == condition_value:
                    # append the index of that line to keys_index_values 
                    key_index_values.append(key_file_content_index_line)

            
            # close file
            key_file.close()

        # loop throught keys inside table
        for key_file_name in os.listdir(f"./database/{table_name}") :
            # text content of this key
            key_file_text_content = []

            # open this key
            with open (f"./database/{table_name}/{key_file_name}", "r") as key_file :
                # get content from key
                key_file_text_content= key_file.readlines()
                # close it
                key_file.close()
            
            # open this key in w mode to reset it
            with open (f"./database/{table_name}/{key_file_name}", "w") as key_file :
                # loop trought old content
                for index_to_write in range(len(key_file_text_content)) :
                    # if the index of that line is not on index to delete (key_index_values)
                    if not index_to_write in key_index_values :
                        # write that line on file
                        key_file.write(key_file_text_content[index_to_write])
                # close the file
                key_file.close()

    return