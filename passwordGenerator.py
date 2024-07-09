import random 
import array

lowerCase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

upperCase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['@', '#', '$', '%', '^', '&', '*', '(',')', '=', ':', '?', '.', '/', '|', '~', '>', '<']

combinedCharacters = lowerCase + upperCase + digits + symbols
 
rand_lower = random.choice(lowerCase) 
rand_upper = random.choice(upperCase) 
rand_digit = random.choice(digits)
rand_symbol = random.choice(symbols)

temp_pass = rand_lower + rand_upper + rand_digit + rand_symbol

maxLength = 16

for x in range (maxLength - 6):
    temp_pass = temp_pass + random.choice(combinedCharacters)

    temp_pass_list = array.array('u', temp_pass) 
    random.shuffle(temp_pass_list)

    password = "" 

for x in temp_pass_list: 
        password = password + x 
          
print("Your Generated Password: ", password) 