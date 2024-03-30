# import os to list dirs
import os

# import tabulate to show info in table
from tabulate import tabulate

# import funtion to verify table existence
from verify_table_existence import verify_table_existence

# create funtion to select column and show them 
def select_column (key_name, table_name, condition):
    # if table exists
    if verify_table_existence (table_name=table_name) :
        # index inside of each file where the content to show is
        content_index = []

        # all content from key from where data will be searched
        selected_key_file_content = []

        # content data to show in table
        column_data = []
        # header content to show in table
        header_content = []

        # open key to seaerch data and if that data exists, get index of theme
        with open(f"./database/{table_name}/{key_name}.txt", "r") as key_file :
            # loop through key file and apped each line to selected selected_key_file_content \n
            for key in key_file.readlines() :
                selected_key_file_content.append(key[:-1])
            # close file
            key_file.close() 
        
        # loop through selected_key_file_content
        for key_index in range(len(selected_key_file_content)) :
            # if selected_key_file_content[key_index] is equal to data gived by user
            if selected_key_file_content[key_index] == condition : 
                # append that index to content_index
                content_index.append(key_index)
        
        # loop through keys on table, exclude .txt from theme and append it to header content
        for key_name in os.listdir(f"./database/{table_name}") : header_content.append(key_name[:-4])
        
        # loop through content_index 
        for key_index in content_index :
            # create data to append to append on column_data
            data_to_append = []
            # loop through keys inside table
            for key_name in os.listdir(f"./database/{table_name}") :
                # open key file 
                with open(f"./database/{table_name}/{key_name}", "r") as key_file :
                    # get all content from key file
                    all_content_from_key = key_file.readlines()

                    # append specific line by key_index, and without \n
                    data_to_append.append(all_content_from_key[key_index][:-1])

                    # close file
                    key_file.close()
                
            # append data to column to show in table
            column_data.append(data_to_append)

        # print table with specific content selected by user
        print("\n")
        print(tabulate(column_data, headers=header_content))
        print("\n")

    return