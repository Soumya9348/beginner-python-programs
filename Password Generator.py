import random
import string

#input the length of password
length = int(input('Enter the length of password: '))

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation
#string.ascii_letters

#combine the data
all = lower + upper + num + symbols

#create the password
password = "".join(random.sample(all,length))

#print the password
print(password)
