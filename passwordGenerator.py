import string
import random
 
random_string = ''
count = 0
while count < 12 :
    random_string += random.choice(string.ascii_lowercase)
    count += 1
print(random_string)
