# uppercase
def to_uppercase(string):
    uppercase_string=""
    for char in string:
        ascii_value=ord(char)
        if 97<=ascii_value<=122:
            uppercase_char=chr(ascii_value-32)
        else:
            uppercase_char=char
        uppercase_string+=uppercase_char
        
    return uppercase_string

#  lowerccase
def to_lowercase(string):
    lowercase_string=""
    for char in string:
        ascii_value=ord(char)
        if 65<=ascii_value<=90:
            lowercase_char=chr(ascii_value+32)
        else:
            lowercase_char=char
        lowercase_string+=lowercase_char
        
    return lowercase_string

# capitalize
def capitalize(string):
    capitalized_string = ""
    first_char = True
    for char in string:
        if first_char and 97 <= ord(char) <= 122:
            capitalized_char = chr(ord(char) - 32)
            first_char = False
        else:
            capitalized_char = char
        capitalized_string += capitalized_char
    return capitalized_string

# title
def title(string):
    title_string = ""
    capitalize_next = True
    for char in string:
        if capitalize_next and 97 <= ord(char) <= 122:
            capitalized_char = chr(ord(char) - 32)
            capitalize_next = False
        else:
            capitalized_char = char
        if capitalized_char == " ":
            capitalize_next = True
        title_string += capitalized_char
    return title_string

# isalpha
def is_alpha(string):
    for char in string:
        if not (65 <= ord(char) <= 90 or 97 <= ord(char) <= 122):
            return False
    return True

# isdigit

def is_digit(string):
    for char in string:
        if not 48 <= ord(char) <= 57:
            return False
    return True

# isupper

def is_upper(string):
    for char in string:
        if (65 <= ord(char) <= 90) or( 48 <= ord(char) <= 57):
            return True
    return False

# islower

def is_lower(string):
    for char in string:
        if (97 <= ord(char) <= 122) or (48 <= ord(char) <= 57):
            return True
    return False

# isalnum

def is_alnum(string):
    for char in string:
        if not ((ord(char) >= 48 and ord(char) <= 57) or (ord(char) >= 65 and ord(char) <= 90) or (ord(char) >= 97 and ord(char) <= 122)):
            return False
    return True

# swapcase

def swap_case(string):
    swapped = ''
    for char in string:
        ascii_value = ord(char)
        if ascii_value >= 97 and ascii_value <= 122:
            swapped += chr(ascii_value - 32)
        elif ascii_value >= 65 and ascii_value <= 90:
            swapped += chr(ascii_value + 32)
        else:
            swapped += char
    return swapped
