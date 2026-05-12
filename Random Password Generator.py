print("RANDOM PASSWORD GENERATOR")
print()


import random
import string

pass_len = 10
charValues = string.ascii_letters + string.digits + string.punctuation

#list comprehension [function for i in range(n)]

# password = "".join([random.choice(charValues) for i in range(pass_len)])

password = ""
for i in range(pass_len):
    password += random.choice(charValues)
    

print("Your Random Password is : ", password)