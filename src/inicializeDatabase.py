# import os for path verification and creation
import os

# create funtions which :
# verify if database dir exists
# create database dir if necessary
def inicialize () :
    # get existence of database dir
    databaseExist = os.path.exists("./database")
    
    # if it not exist
    if databaseExist == False :
        # create database dir
        os.mkdir("database")

    return