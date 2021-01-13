# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Vu'
age = 18

#concatenate
# print('Hello, my name is ' + name + ' and my age is '+ str(age))

# String Formatting

# Arguments by position
# print('My name is {ten} and my age is {tuoi}'.format(ten = name, tuoi = age))

#F-Strings (3.6+) (SHOULD USE THIS)
print(f'Hello, my name is {name} and my age is {age}')
# String Methods

s = "hello world"

#Capitalized Strings

print(s.capitalize()) #Chỉ viết hoa chữ cái đầu

#Make all uppercases

print(s.upper())

# Make all lower
print(s.lower())

# Swap case
print(s.swapcase())


# Get length
print(len(s))

# Replace
print(s.replace('world', 'everyone'))

# Count
sub = 'l'
print(s.count(sub))

# Starts with
print(s.startswith('hello'))

# Ends with
print(s.endswith('d'))

# Split into a list
print(s.split())

# Find position
print(s.find('r'))

# Is all alphanumeric
print(s.isalnum())

# Is all alphabetic
print(s.isalpha())

# Is all numeric
print(s.isnumeric())

