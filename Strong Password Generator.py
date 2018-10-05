
# coding: utf-8

# In[11]:


from secrets import choice
import string

pNumber = input('Number Of Passwords Required: ')
pNumber = int(pNumber)

# N is length of pass
N = 16
for outputnum in range(pNumber):
    # Output: pNumber of passwords as a 16 character string
    print (''.join([choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(N)]))

