# import click to get arguments
import click

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
        pass

    elif funtion_entry == 'INSERT' :
        pass

    elif funtion_entry == 'SELECT' :
        pass

    elif funtion_entry == 'REMOVE' :
        pass

    elif funtion_entry == 'EDIT' :
        pass



if __name__ == "__main__" :
    doFunction()