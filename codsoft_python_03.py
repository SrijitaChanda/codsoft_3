#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as np
import pandas as pd
import random
import string


# In[8]:


print(string.ascii_letters)
print(string.digits)
print(string.punctuation)


# In[10]:


length=int(input("Enter Length:"))
chars=string.ascii_letters
chars+= string.digits
chars+= string.punctuation

password=""

for i in range(length):
    n_char=random.choice(chars)
    password+=n_char
print("your password:",password)


# In[ ]:




