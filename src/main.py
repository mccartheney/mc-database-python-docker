# import click to get arguments
import click

from inicialize_database import inicialize

from create_table import create_table
from delete_table import remove_table

# initiliaze click
@click.command()
# get first argument
# this argument is to get the action to do for exemple : CREATE, DELETE, SHOW, etc ...
@click.argument("funtion_entry", default='')
# get other arguments
# the arguments bellow will be used to complement the query
@click.argument("funtion_argument_one", default='')
@click.argument("funtion_argument_two", default='')
@click.argument("funtion_argument_three", default='')
@click.argument("funtion_argument_four", default='')
@click.argument("funtion_argument_five", default='')
# pass all arguments to funtion 
def doFunction (funtion_entry, funtion_argument_one, funtion_argument_two, funtion_argument_three, funtion_argument_four, funtion_argument_five) :
    if funtion_entry == "SHOW" :
        pass

    elif funtion_entry == 'DELETE' :
        
        pass

    elif funtion_entry == 'CREATE' :
        table_name = funtion_argument_one
        keys = funtion_argument_two.split (",")
        create_table(table_name=table_name, keys=keys)
        pass

    elif funtion_entry == 'INSERT' :
        pass

    elif funtion_entry == 'SELECT' :
        pass

    elif funtion_entry == 'REMOVE' :
        table_name = funtion_argument_one
        remove_table(table_name=table_name)
        pass

    elif funtion_entry == 'EDIT' :
        pass



if __name__ == "__main__" :
    # create database dir in case is the first time using 
    inicialize()

    # run query in database
    doFunction()