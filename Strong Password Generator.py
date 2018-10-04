
# coding: utf-8

# In[11]:


from secrets import choice
import string

generate = input('Number Of Passwords Required: ')
generate = int(generate)

N = 16
for outputnum in range(generate):
    print (''.join([choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(N)]))

