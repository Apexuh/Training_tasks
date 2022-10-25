import random


digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
strange_symbol = 'il1Lo0O'


quantity_of_passwords = int(input('How many passwords do you need? >>> '))
len_password = int(input('Length of password? >>> '))
digit = input('Do you need digits in your password?(Y/N) >>> ')
uppercase = input('Do you need UPPERCASE letters in your password?(Y/N) >>> ')
lowercase = input('Do you need lowercase letters in your password?(Y/N) >>> ')
symbols = input('Do you need symbols in your password?(Y/N) >>> ')
strange_symbols = input('Do you need symbols like this--> il1Lo0O  in your password?(Y/N) >>> ')

chars = ''
if digit.lower() == 'y':
    chars += digits
if uppercase.lower() == 'y':
    chars += uppercase_letters
if lowercase.lower() == 'y':
    chars += lowercase_letters
if symbols.lower() == 'y':
    chars += punctuation
if strange_symbols.lower() == 'n':
    for i in strange_symbol:
        chars = chars.replace(i, '')
print(chars)


def generate_password(length, chars):
    password = ''.join([random.choice(chars) for _ in range(length)])
    return password

for i in range(quantity_of_passwords):
    print(generate_password(len_password, chars))