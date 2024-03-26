# import os to create dirs
import os

# import click to get params from user
import click

# funtion for verify is table exists
from verify_table_existence import verify_table_existence

# initialize click
@click.command()

# get arguments by click
@click.argument("table_name")
@click.argument("keys", nargs=-1)
# create funtion to create table
def create_table (table_name, keys) : # pass click arguments to 
    # if table dont exists
    if not verify_table_existence ( table_name = table_name ) :
        # create table dit
        os.mkdir(f"./database/{table_name}")

        # do a loop through keys
        for keyIndex in range(len(keys)) :
            # the keys comes with a "bug", for exemple [this, is, a, array]
            # it will return as :
            # [this,
            # is,
            # a,
            # array]

            # file name is equal the key
            filename = keys[keyIndex]
            # from the actual key get all except the last caracter
            filename = filename[:-1]
            
            # if it is the first key
            if keyIndex == 0 :
                # get all minus the the first caracter
                filename = filename[1:]

            # create key file
            with open(f"./database/{table_name}/{filename}.txt", "w") as key_file:
                # close the key file
                key_file.close()
        
        return
    
    # if table already exists warn user
    print (f"{table_name} already exists !")

    return

create_table()