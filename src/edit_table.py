# import funtion to verify if table exists
from verify_table_existence import verify_table_existence

# funtion to edit specific info on table
def edit_table (table_name, things_to_change, condition) :
    # verify of table exists
    if verify_table_existence(table_name=table_name) :
        # index of specific key line where have element which will be changed
        keys_index_with_old_value = []

        # key file to search info to change
        key_to_search = things_to_change[0]
        # value to search to get index to change info
        old_value = things_to_change[1]

        # key where info will be changed
        key_to_change = condition[0]
        # info what to add in specific index and key
        new_value = condition[1]

        # open key file to search for info
        with open(f"./database/{table_name}/{key_to_search}.txt", "r") as search_key_file :
            # get all content from key file
            key_content = search_key_file.readlines()

            # loop through taht content
            for key_line_index in range(len(key_content)) :
                # if that line have the same value of the value to change
                if key_content[key_line_index][:-1] == old_value :
                    # add the index of that line to a key_line_index
                    keys_index_with_old_value.append(key_line_index)

        # var to add content of the key file which will recieve info
        key_text_content = []

        # open key file ( key to receive info )
        with open(f"./database/{table_name}/{key_to_change}.txt", "r") as key_file :
            # get the content to key_text_content
            key_text_content = key_file.readlines()

            # close the file
            key_file.close()

        # open key file ( key to receive info ) in w mode to reset file
        with open(f"./database/{table_name}/{key_to_change}.txt", "w") as key_file :
            # loop through key_text_content
            for line_index in range(len(key_text_content)) :
                # if the actual index is in keys_index_with_old_value
                if line_index in keys_index_with_old_value :
                    key_file.write(f"{new_value}\n") # write the new value
                else : # if its not
                    key_file.write(key_text_content[line_index]) # write the old content
    return
