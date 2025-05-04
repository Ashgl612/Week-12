import string
import random
 
random_string = ''
count = 0
while count < 12 :
    random_string += random.choice(string.ascii_lowercase)
    count += 1
print(random_string)
# I tried to figure it out on my own, but I honestly didn't get further than figuring out it's a while loop.. I'm still not very skilled when it comes to For and While loops...so I looked at the solution you put on canvas