#!/usr/bin/env python
# coding: utf-8

# # String in Python 

# In[1]:


a = " ini adalah string pada python"
print(a)


# Pada python string adalah tipe data yang immutable, artinya data itu tidak bisa diubah setelah dideklarasikan. tipe ada ini mirip dengan tuple. namun kita bisa assign nilai string baru ke variable yang sama. 

# In[2]:


a1 = " ini adalah string pada python"
a1[2] = "a"


# inilah yang terjadi kalau kita mencoba mengubah nilai string. akan terjadi TypeError. 

# In[5]:


a = " ini adalah string pada python"
print(a) 
a = " ini adalah string baru yang di-assign pada peubah a"
print(a)


# ## index pada string
# sama seperti list, kita bisa mengakses elemen pada string dengan menggunakan index. index pada python dimulai dari 0.

# In[1]:


name = "Muhammad Rizkillah"
print(name[0:5])


# seperti yang anda duga hal ini mirip dengan apa yang kita lakukan pada list. padaa dasarnya string merupakan list of char yang tidak membutuhkan koma. 

# ## slicing a string 
# 

# In[2]:


first_name = "Rodrigo"
last_name = "Villanueva"

new_account = last_name[:5]
print(new_account)
temp_password = last_name[2:6]
print(temp_password)


# ### concatenation of slicing strinng 

# In[6]:


first_name = "Julie"
last_name = "Blevins"

def account_generator(first_name, last_name):
    first = first_name[:3]
    last = last_name[:3]
    new_account = first + last
    return new_account
new_account = account_generator(first_name, last_name)
print(new_account)


# In[7]:


#Write a function called password_generator() that takes two inputs, first_name and last_name, and then concatenates the last three letters of each and returns them as a string.
def password_generator(first_name, last_name):
    first = first_name[-3:]
    last = last_name[-3:]
    new_account = first + last
    return new_account
new_account = password_generator(first_name, last_name)
print(new_account)


# #### Negative indexing

# In[ ]:




