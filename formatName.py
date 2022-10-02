#Formats the users first and last name to be capitalized
def formatName(f_name, l_name):
    if f_name == '' or l_name == '':
        return 'First and last name must have a value.'
    else:
        return (f'The formated name is now {f_name.title()} {l_name.title()}.')