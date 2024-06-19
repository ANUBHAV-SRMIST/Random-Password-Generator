import random
import string 
pass_len = 8
charValue = string.ascii_letters + string.digits + string.punctuation

#list comprehension [ function for i in range (n)]

password = "" .join ([random.choice(charValue) for i in range (pass_len)])

#Another way
#password = ""
#for i in range(pass_len):
#    password += random.choice(charValue)

print("Your random password is : " , password)