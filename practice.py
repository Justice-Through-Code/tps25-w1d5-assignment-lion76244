# String data type

# literal assignment of value 
first = 'Joyce'
last = 'Kamdem'

# print(type(first))
# print(type(first) == str) 
# print(isinstance(first, str))

# constructure function
# pizza = str('pepperoni')
# print(type(pizza))
# print(type(pizza) == str) 
# print(isinstance(pizza, str))

# Concatenation 
fullname = first + ' ' + last 
print(fullname)

fullname += '!'
print(fullname)

#casting a number to a string
decade = str(1980)
print(type(decade))
print(decade)

statment = "I like rock music from the " + decade + "s."
print(statment)

# Multiple lines
multiline = ''' 
Hey, how are you?   

I was just checking in.

                            All good?

'''                           
print(multiline)

# Escaping special charecters
sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at\\located?'
print(sentence)

# String Methods
print(first)
print(first.lower())
print(first.upper())
print(first)

print(multiline.title())
print(multiline.replace('good', 'ok'))
print(multiline)

print(len(multiline))
multiline += '                                                 '
multiline = '                                ' + multiline
print(len(multiline))

print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

print("")

# Build a menu
title = 'menu'.upper()
print(title.center(20, '='))
print('Coffee'.ljust(16, ".") + '$1'.rjust(4))
print('Muffin'.ljust(16, ".") + '$2'.rjust(4))
print('Cheesecake'.ljust(16, ".") + '$4'.rjust(4))

print(" ")

#string index value
print(first[1])
print(first[-1])
print(first[1:-1])
print(first[1:])

# Some methods return boolean data
print(first.startswith('J'))
print(first.endswith('y'))

# Booolean data type 
myvalue = True 
x = bool(False)
print(type(x))
print(isinstance(myvalue, bool))

#Numeric data types

#interger type
price = 100 
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))

# float type
gpa = 3.2
y = float(1.12)
print(type(gpa))

# complex type
comp_value = 5+3j
print(type(type(comp_value)))
print(type(comp_value.real))
print(type(comp_value.imag))

# Built -in functions
print(abs(gpa))
print(round(gpa, 1))

# Casting a string to a number
zipcode = "10027"
zip_value = int(zipcode)
print(type(zip_value))

# Error if you attempt to cast incorrect data
# zip_value = int('New York')