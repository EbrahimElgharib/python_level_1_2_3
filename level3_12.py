# 12. Build an email slicer : create a function that takes an email as input and retrieve the username and domain of the email

email = 'email_-.3zid@exam.ple.com'


# use slice simply
'''
slicer = email.split('@')
print(f'UserName: slicer[0]\nDomain: slicer[1]')
'''


# Using regex
import re

pattern = r'^([\w\-\.]+)@(([\w\-]+\.)+[\w-]{2,4})$'
match = re.match(pattern, email)

if match:
    print(f'UserName : {match.group(1)}\nDomain : {match.group(2)}')
else:   
    print("not valid email")
