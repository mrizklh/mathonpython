#!/usr/bin/env python
# coding: utf-8

# # List 
# List adalah suatu cara menyimpan koleksi dari suatu data yang dapat diubah (mutable). tipe data list tidak terbatas pada tipe data yang sama. satu list bisa memiliki banyak tipe data.

# In[1]:


contoh_list = [1, 2, 3, 4, 5]
print(contoh_list)


# ## Kriteria mendeklarasikan list 
# - List didefinisikan dengan tanda kurung kotak "[]"
# - tiap elemen dalam list harus dipisahkan dengan tanda koma ","
# - list dapat mengandung elemen yang sama, jadi tidak ada koma di tengah elemen
# - list dapat mengandung list lain, namanya list 2 dimensi. 
# 
# 

# In[2]:


contoh_list_2 = [1, 2, " python", 1.2, ["list di dalam list"], True]
print(contoh_list_2[-1])


# ## mengakses list
# 
# pada contoh diatas mungkin anda kebungungan kenapa cuma niai True yang keluar. hal ini karena kita mengakses list dengan index yang dimulai dari 0. namun di sini uniknya kita juga bisa mengakses elemen dalam list dengan index negatiif yaitu yna g munlai dari belakang. 

# In[3]:


# anda juga bisa mendeklarasikan list ke variable tanpa elemen yang biasanya nantinya akan diisi
contoh_list_3 = []
print(contoh_list_3)


# ## List Methods
# List methods adalan sekumkulan dari method yang dapat digunakan pada list. untuk penjelasan lebih lanjut tentang method akan disampaikan pada bagian selanjutnya. untuk sekarang kita akan mencukupkan diiri dengan contoh berikut:

# In[4]:


a = [1, 2, 3, 4, 5]
a.append(6)
print(a)


# Pada kasus ini .append method berfungsi untuk menambahkan elemen baru ke list.
# 
