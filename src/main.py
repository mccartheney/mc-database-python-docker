# import click to get arguments
import click

from inicialize_database import inicialize

from create_table import create_table

import ast

def parse_arguments(ctx, param, value):
    if not value:  # If no arguments provided
        return ("", [])
    elif len(value) == 1:  # If only one argument provided
        return value[0], []  # Return the argument as table_name and an empty list as keys
    else:  # If multiple arguments provided
        return value[0], ast.literal_eval(value[1])  # Return the first argument as table_name and the second argument parsed as a list


# initiliaze click
@click.command()
# get first argument
# this argument is to get the action to do for exemple : CREATE, DELETE, SHOW, etc ...
@click.argument("funtion_entry", default='')
# get other arguments
# the arguments bellow will be used to complement the query
@click.argument("funtion_argument_one", default='')
@click.argument("funtion_argument_two", nargs=-1, callback=parse_arguments)
@click.argument("funtion_argument_three", default='')
@click.argument("funtion_argument_four", default='')
@click.argument("funtion_argument_five", default='')
# pass all arguments to funtion 
def doFunction (funtion_entry, funtion_argument_one, funtion_argument_two, funtion_argument_three, funtion_argument_four, funtion_argument_five) :
    if funtion_entry == "SHOW" :
        pass

    elif funtion_entry == 'DELETE' :
        pass

    # elif funtion_entry == 'CREATE' :
    #     pass

    elif funtion_entry == 'INSERT' :
        pass

    elif funtion_entry == 'SELECT' :
        pass

    elif funtion_entry == 'REMOVE' :
        pass

    elif funtion_entry == 'EDIT' :
        pass



if __name__ == "__main__" :
    # create database dir in case is the first time using 
    inicialize()

    # run query in database
    doFunction()