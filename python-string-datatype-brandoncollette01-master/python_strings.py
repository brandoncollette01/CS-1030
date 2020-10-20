# TODO Create Variables
#   - Create the following variables
#   - my_first_name
#       -set this equal to your first name
#   - my_last_name
#       -set this equal to your last name
#   - my_year_of_birth
#       -set this equal to your birth year (doesn't have to be real should be less then 100 yrs ago)
#   - current_year
#       -set this equal to 2020
my_first_name = 'Brandon'
my_last_name = 'Collette'
my_year_of_birth = 2001
current_year = 2020
email_address = '@gmail.com'

#print(my_first_name)
#print(my_first_name + my_last_name)
#print(my_first_name + ' ' + my_last_name)
#print(my_first_name + '.' + my_last_name + email_address)



# TODO String Indexing
#   - Print the following items (one per line) (print using variables)
#       - first name  
#       - last name
#       - first letter of your first name (use the +index)
#       - second letter of your last name (use the -index)
#       - first two letter of your first name (use the +index)
#       - second two letter of your last name (use the -index)

first_letter = my_first_name[0]
first_initial = my_first_name[0]
last_initial = my_last_name[0]
initials = first_initial + '.' + last_initial + '.'

#print('first letter of your first name: ' + my_first_name[0])
#print('first letter of your first name: ' + first_letter)
#print('last letter of your last name: ' + my_last_name[-1])
#print('My initials are: ' + initials)

first_two_name = my_first_name[0:2]
last_two_name = my_last_name[-2:]

print('First two letters: ' + first_two_name)
print('Last two letters: ' + last_two_name)

#TODO Combining Strings
#   - Print the following items (one per line) (print using variables)
#       -first name and last name combined
#       -first name six times

#print(first_letter * 6)
#print(my_first_name, my_last_name)



# TODO Formatting Strings
#   - Print the following items (one per line) (print using variables)
#       - first name last name -was born in- year of birth
#       - first name last name -was born in- year of birth. first name -enjoyed celebrating- current year

birth_year = my_first_name + ' ' + my_last_name + ' born in {}.'
print(birth_year.format(my_year_of_birth))

birth_year_message = my_first_name + my_last_name + ' was born in {}. {} enjoyed celebrating {}'
print(birth_year_message.format(my_year_of_birth, my_first_name, current_year))

my_birth_year_string = str(my_year_of_birth)
print('birth year string ' + my_birth_year_string)

# TODO Escape characters
#   - Print the following items (one per line) (print using variables)
#       - possesive first name -birth year is- year of birth 
#       - tab last name current year

print("Brandon's birth year is " + my_birth_year_string)
print('\t' + my_last_name, str(current_year))


# TODO String methods
#   - Print the following items (one per line) (print using variables)
#       - first name and last name in lower case
#       - length of last name
#       - first name and last name all in upper case

lower_name = my_first_name.casefold()
print(my_first_name.casefold(), my_last_name.casefold())
print(my_first_name.upper(), my_last_name.upper())