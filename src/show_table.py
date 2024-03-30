# import os to get all keys from a table
import os

# import funtion to verify if table exists
from verify_table_existence import verify_table_existence

# import tabulate to show data in a table
from tabulate import tabulate


# finction to show table info
def show_table (table_name) :
    # if table exists
    if verify_table_existence(table_name=table_name) :
        # get all keys from selected table by user
        keys = os.listdir(f"./database/{table_name}")
        # header content for table
        header_content = []

        # contents from table
        keys_content = []
        table_content = []

        # loop through all keys (files) inside table dir
        for key_index in range(len(keys)) :
            # get key name file by loop index
            key = keys[key_index]

            # open a file with key variable ( file name )
            with open(f"./database/{table_name}/{key}", "r") as key_file:
                # append key (file) content to keys_content
                keys_content.append(key_file.readlines())

            # remove .txt from file name
            key = key[:-4]

            # append file name to header
            header_content.append(key)
        
        # loop through keys content item
        for key_index in range (len(keys_content[0])) :
            # content to append on table content
            content_to_append = []

            # loop through key content
            for key_sub_index in range(len(keys_content)):
                # append lines with the same index from all keys (files) in one array
                content_to_append.append(keys_content[key_sub_index][key_index])

                # example of content to append after loops
                # [
                #   [
                #       line 1 # key 1  
                #       line 1 # key 2
                #       line 1 # key 3
                #   ]
                #   [
                #       line 2 # key 1  
                #       line 2 # key 2
                #       line 2 # key 3
                #   ]
                #   [
                #       line 3 # key 1  
                #       line 3 # key 2
                #       line 3 # key 3
                #   ]
                # ]
            
            # append array to table content
            table_content.append(content_to_append)
            
        # print table with table content
        print("\n")
        print(tabulate(table_content,headers=header_content))
        print("\n")