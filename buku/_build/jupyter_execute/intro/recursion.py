#!/usr/bin/env python
# coding: utf-8

# # Recursion 
# Rekursi adalah 

# In[1]:


rekusi adalah adalah memanggil suatu fungsi di dalam fungsi itu sendiri. 


# ## contoh kasus 
# let says... kita ingin membuat fungsi yang mengambil suatu input bilangan bulat dan mengembalikan total penjumlahan dari 1 sampai input tersebut.

# ### jawab
# kasus ini dapat diselesaikan dengan metode rekusif. karena f(n) = f(n-1) + n, maka kita bisa mengimplementasikan fungsi ini dengan rekusif. bentuk kodenya dalah sebagai berikut.  
# 

# In[8]:


def jumlah_sampai_n(n): 
    if n == 0: 
        return 0
    elif n < 0: 
        return n + jumlah_sampai_n(n+1)
    else:
        return n + jumlah_sampai_n(n-1)
jumlah_sampai_n(5)


# ### is power of 
# mari kita buat funsi yang mengamambil dua input, pada argument pertama meruapakan bilangan bulat dan pada argument kedua meruapakan bilangan bulat. fungsi ini akan mengembalikan true jika bilangan tersebut merupakan pangkat dari bilangan lain.
# 
# misalnya f(8,2) maka outputnya harusnya True. karena 2^3 = 8. 

# In[9]:


a = 2^89245823459
def is_powerof(a, b): 
    
    if a == b: 
        return True
    elif a < b: 
        return False
    else:
        return is_powerof(a/b, b)
is_powerof(a, 2)


# pada contoh kode diatas merupakan contoh funsi yang bisa didefinisikan dengan fungsi itu sendiri. f(5,2) = f(2.5/2,2) = f(4/2,2)

# In[11]:


# make a function that take 2 input a number and base number and return the exponent of the number
def exponent(a, b):
    if b == 1:
        return a
    else:
        return 

exponent(8, 2)


# f(n,m)= f()

# In[17]:


## maek a function that take a 2 number that is number and base number and return the exponent of the number
def how_many_exponent(a, b):
    if a == b:
        return 1
    elif a % b != 0:
        return "a tidak genap pangkat b"
    else:
        return 1 + how_many_exponent(a/b, b)
how_many_exponent(3, 2)
  


# In[ ]:




