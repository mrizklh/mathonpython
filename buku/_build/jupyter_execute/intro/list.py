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


# Pada kasus ini .append method berfungsi untuk menambahkan elemen baru ke list, yaitu element int 6. dengan ini kita dapat simpulkan bahwa list dalam python adaah mutable. yang artinya bisa diubah ketika sudah dideklarasikan. 
# 

# In[5]:


order = ["bola", "kotak", "buku"] 
order.append("komputer")
print(order)


# # Menambahkan list dengan + (Plus)
# list pada python bisa ditambahkan dengan list lain dengan menggunakan operator +. namun tipe datanya juga harus list. seperti kode di bawah. 

# In[6]:


items_to_add = ["buku", "komputer", "bola", "kotak"]
items_to_add_new = items_to_add + ["laptop"]
print(items_to_add_new)


# In[7]:


items_to_add_new2 = items_to_add + "laptop"
print(items_to_add_new2)


# type error terjadi karena kita concatenate list dengan tipe data string. 

# In[ ]:


orders = ["daisy", "buttercup", "snapdragon", "gardenia", "lily"]

# Create new orders here:
new_orders =  ["lilac", "iris"]

orders_combined = orders + new_orders 

broken_prices = [5, 3, 4, 5, 4] + [4]


# # Mengakses list dengan index. 
# Index pada list dimulai dari 0. jadi index dari element pertama pada list berindex 0. 
# sekarang kita coba lihat bagaimana mengakses item dalam list menggunakan index. 

# In[5]:


employees = ["Michael", "Dwight", "Jim", "Pam", "Ryan", "Andy", "Robert"]
forth_employee = employees[3]
print(forth_employee)


# dari contoh di atas kita bisa lihat employee ke 4 berindex 3 dan begitu seterusnya. 

# jika index melebih batas list maka akan terjadi error. yaitu index error. sseperti contoh di bawah. 

# In[6]:


list = [1, 2, 3, 4, 5]
print(list[6])


# hal ini dikarenakan list[6] tidak ada. yang ada cuma sampe index 4. sehingga terjadi index error. 

# # Negatif index: mengakses list dari belakang. 
# 
# Dengan negatif index kita bisa mengakses item pada list dari belakang. 

# In[ ]:


shopping_list = ["eggs", "butter", "milk", "cucumbers", "juice", "cereal"]
last_element = shopping_list[-1]
index5_element = shopping_list[5]
print(last_element)
print(index5_element)


# # Modifikasi element list.
# 
# kita bisa mengganti elemen list dengan menggunakan operator assignment.

# In[ ]:


arden_waitlist = ["Jiho", "Adam","Sonny", "Alisha"]
garden_waitlist[1] = "Calla"
print(garden_waitlist)

garden_waitlist[-1] = "Alex"
print(garden_waitlist)


# # Removing element list.
# 
# Kita bisa menghilangkan item dari suat List. dengan method .remove. seperti contoh dibawah. 

# In[ ]:


order_list = ["Celery", "Orange Juice", "Orange", "Flatbread"]
print(order_list)
order_list.remove("Flatbread")
print(order_list)
new_store_order_list = ["Orange", "Apple", "Mango", "Broccoli", "Mango"]
print(new_store_order_list)
new_store_order_list.remove("Mango")
print(new_store_order_list)
new_store_order_list.remove("Onions")


# kita tidak bisa remove item yang tidak ada di list. jika kita melakukan itu akan terjadi value error.

# # Two Dimension List
# 
# List bisa mengandung list lain. seperti contoh dibawah.

# In[ ]:


heights = [["Jenny", 61], ["Alexus", 70], ["Sam", 67], ["Grace", 64]]
heights.append(["Vik", 68])
print(heights)

ages = [["Aaron", 15],["Dhruti", 16]]


# In[ ]:


class_name_test = [["Jenny",	90],["Alexus",	85.5],["Sam",	83],["Ellie",	101.5]]
print(class_name_test)
sams_score = class_name_test[2][1]
print(sams_score)
ellies_score = class_name_test[-1][-1]
print(ellies_score)


# In[ ]:


incoming_class = [["Kenny", "American", 9],["Tanya", "Russian", 9], ["Madison", "Indian", 7]]
incoming_class[2][2] = 8 
print(incoming_class)
incoming_class[-3][-3] = "Ken"
print(incoming_class)


# # Review about list. 
# 
# 

# In[ ]:


first_names = ["Ainsley", "Ben", "Chani","Depak"] 
preferred_size = ["Small", "Large", "Medium"]
preferred_size.append("Medium")
print(preferred_size)
customer_data = [["Ainsley",	"Small",	True],["Ben",	"Large",	False],["Chani","Medium",	True],["Depak","Medium", False]]
print(customer_data)
customer_data[2][2] = False
customer_data[1].remove(customer_data[1][2])


# 
