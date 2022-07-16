#!/usr/bin/env python
# coding: utf-8

# # dictionary 

# dictionary adalah suatu bentuk data struktur dimana setiap elemennya memiliki nilai yang unik. elemen yang unik ini disebut *key pair*. ini mirip dengan database dimana setiap elemennya memiliki nilai unik. seperti dalam aplikasi instagram *key pair* pada hal ini adalah *username dan password*. dari username dan password ini segala data yang terkait akun instagram dapat ditemukan. Where a list index is always a number, a dictionary key can be a different data type, like a string, integer, float, or even tuples.

# ## cara mendeklarasikan dictionary

# In[1]:


file_count = {"jpg": 10, "png": 20, "gif": 30, "txt": 40}
print(file_count)


# mari kita breakdown kode diatas:
# - file_count merupakan variabel yang menyimpan data dari dictionary
# - {} atau disebut juga "tanda kurung kurawal" adalah tanda bahwa dictionary ini akan diisi dengan key pair dan value pair.
# - key pair adalah kumpulan data yang memiliki nilai unik. dalam hal ini key pair adalah tipe data string.
# - value pair adalah kumpulan data yang memiliki nilai unik. dalam hal ini value pair adalah tipe data integer.
# - tiap elemen pada dictionary dipisahkan oleh tanda koma sama seperti pada list dan tuple.

# In[2]:


file_count["jpg"]


# kode diatas merupakan salah satu ddari aplikasi dictionary. kita bisa memanggil value pair dengan menggunakan key pair. 

# In[3]:


print("jpg" in file_count)
print("xml" in file_count)


# ### menambahkan elemen pada dictionary 

# In[4]:


file_count["xml"] = 50
print(file_count)


# dapat kita lihat di sini bahwa dictionary file count bersifat mutable. artinya bisa diubah. mirip seperti list bukan tuple. 

# In[5]:


file_count["xml"] += 10
print(file_count)

