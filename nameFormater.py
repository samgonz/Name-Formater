import formatName

#Gathers the first and last name of the user.
f_name = input('What is your first name?')
l_name = input('What is your last name?')

#Formats the user name so the first letter of each name is capitalized
formated_name = formatName.formatName(f_name, l_name)

#Prints the formated first and last name
print(f'{formated_name}')