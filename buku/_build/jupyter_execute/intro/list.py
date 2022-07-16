#!/usr/bin/env python
# coding: utf-8

# # List 
# List adalah suatu cara menyimpan koleksi dari suatu data yang dapat diubah (mutable). tipe data list tidak terbatas pada tipe data yang sama. satu list bisa memiliki banyak tipe data.

# ## list tutorial

# In[1]:


contoh_list = [1, 2, 3, 4, 5]
print(contoh_list)


# ### Kriteria mendeklarasikan list 
# - List didefinisikan dengan tanda kurung kotak "[]"
# - tiap elemen dalam list harus dipisahkan dengan tanda koma ","
# - list dapat mengandung elemen yang sama, jadi tidak ada koma di tengah elemen
# - list dapat mengandung list lain, namanya list 2 dimensi. 
# 
# 

# In[2]:


contoh_list_2 = [1, 2, " python", 1.2, ["list di dalam list"], True]
print(contoh_list_2[-1])


# ### mengakses list
# 
# pada contoh diatas mungkin anda kebungungan kenapa cuma niai True yang keluar. hal ini karena kita mengakses list dengan index yang dimulai dari 0. namun di sini uniknya kita juga bisa mengakses elemen dalam list dengan index negatiif yaitu yna g munlai dari belakang. 

# In[3]:


# anda juga bisa mendeklarasikan list ke variable tanpa elemen yang biasanya nantinya akan diisi
contoh_list_3 = []
print(contoh_list_3)


# ### List Methods
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


# ### Menambahkan list dengan + (Plus)
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


# ### Mengakses list dengan index. 
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

# ### Negatif index: mengakses list dari belakang. 
# 
# Dengan negatif index kita bisa mengakses item pada list dari belakang. 

# In[ ]:


shopping_list = ["eggs", "butter", "milk", "cucumbers", "juice", "cereal"]
last_element = shopping_list[-1]
index5_element = shopping_list[5]
print(last_element)
print(index5_element)


# ### Modifikasi element list.
# 
# kita bisa mengganti elemen list dengan menggunakan operator assignment.

# In[ ]:


arden_waitlist = ["Jiho", "Adam","Sonny", "Alisha"]
garden_waitlist[1] = "Calla"
print(garden_waitlist)

garden_waitlist[-1] = "Alex"
print(garden_waitlist)


# ### Removing element list.
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

# ## Two Dimension List
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


# ## Review about list. 
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


# ## Working with list. 
# 
# ### Adding by index: insert 
# insert method membutuhkan 2 argument yaitu index dan item.
# 

# In[ ]:


front_display_list = ["Mango", "Filet Mignon", "Chocolate Milk"]
print(front_display_list)

# Your code below: 
front_display_list.insert(0, "Pineapple")
print(front_display_list)


# pada contoh diatas, 0 adalah index item yang ditambahkan berapada, sedangakan "Pineapple" adalah item yang ditambahkan.

# ### removing by index: pop
# pop method membutuhkan 1 argument yaitu index item yang akan dihapus. 

# In[2]:


cs_topics = ["Python", "Data Structures", "Balloon Making", "Algorithms", "Clowns 101"]
removed_topic = cs_topics.pop()
print(cs_topics)


# argumen default adalah -1. yang artinya akan menghapus item terakhir. 

# In[ ]:


data_science_topics = ["Machine Learning", "SQL", "Pandas", "Algorithms", "Statistics", "Python 3"]
print(data_science_topics)

# Your code below: 
data_science_topics.pop()
print(data_science_topics)

data_science_topics.pop(3)
print(data_science_topics)


# In[ ]:


number_list = range(9)
print(list(number_list))

zero_to_seven = range(8)
print(list(zero_to_seven))


# ### The Power of Range in Python
# secara default range mengambil index 0 sampai index terakhir. jadi dengan satu argument range akan mengambil index 0 sampai index yang diinputkan, namun tidak inclusive artinnya untuk range(10) akan menghasilkan index 0 sampai index 9. 
# 
# namun, range tidak harus mulai dari 0, kita bisa mengambil 2 argument sebagai awalan dan akhiran. seperti contoh dibawah. 
# 

# In[3]:


a1 = range(3, 10)
print(list(a1))


# kita juga bisa memasukkan argument ketiga untuk inkremental atau penambahan index. seperti contoh dibawah.

# In[4]:


a2 = range(3, 20, 2)
print(list(a2))
range_five_three = range(5, 15, 3)
range_diff_five = range(0, 40, 5)


# ### Length of List
# kita bisa mengetahui panjang dari list dengan menggunakan funsi len.

# In[ ]:


long_list = [1, 5, 6, 7, -23, 69.5, True, "very", "long", "list", "that", "keeps", "going.", "Let's", "practice", "getting", "the", "length"]

big_range = range(2, 3000, 10)


# In[ ]:


long_list = [1, 5, 6, 7, -23, 69.5, True, "very", "long", "list", "that", "keeps", "going.", "Let's", "practice", "getting", "the", "length"]

big_range = range(2, 3000, 100)

# Your code below: 
long_list_len = len(long_list)
print(long_list_len)

big_range_length = len(big_range)
print(big_range_length)


# ### Slicing Lists I
# 
# Dalam Python, seringkali kita ingin mengekstrak hanya sebagian dari daftar. Membagi daftar sedemikian rupa disebut sebagai mengiris.

# In[6]:


letters = ["a", "b", "c", "d", "e", "f", "g"]
beginnimg_of_letters = letters[0:3]
print(beginnimg_of_letters)


# In[ ]:


suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]

# Your code below: 
last_two_elements = suitcase[-2:]
print(last_two_elements)

slice_off_last_three = suitcase[:-3]
print(slice_off_last_three)


# ### counting an element in a list. 
# using count method.

# In[ ]:


votes = ["Jake", "Jake", "Laurie", "Laurie", "Laurie", "Jake", "Jake", "Jake", "Laurie", "Cassie", "Cassie", "Jake", "Jake", "Cassie", "Laurie", "Cassie", "Jake", "Jake", "Cassie", "Laurie"]

# Your code below: 
jake_votes = votes.count("Jake")
print(jake_votes)


# ### sort a list in ascending order.

# In[ ]:


# Checkpoint 1 & 2
addresses = ["221 B Baker St.", "42 Wallaby Way", "12 Grimmauld Place", "742 Evergreen Terrace", "1600 Pennsylvania Ave", "10 Downing St."]

addresses.sort()
print(addresses)


# Checkpoint 3
names = ["Ron", "Hermione", "Harry", "Albus", "Sirius"]
names.sort()


# Checkpoint 4 & 5
cities = ["London", "Paris", "Rome", "Los Angeles", "New York"]
sorted_cities = cities.sort(reverse=True)
print(sorted_cities)


# ## Review working list in Python 
# - .insert() menambahkan item ke list.
# - .pop() menghapus item dari list.
# - .range() menghasilkan list dari index yang ditentukan.
# - len() adalah fungsi untuk mengetahui panjang dari list.
# - .count() adalah fungsi untuk menghitung jumlah item yang sama dalam list.
# - .sort() adalah fungsi untuk mengurutkan list.
# 

# In[ ]:


inventory = ["twin bed", "twin bed", "headboard", "queen bed", "king bed", "dresser", "dresser", "table", "table", "nightstand", "nightstand", "king bed", "king bed", "twin bed", "twin bed", "sheets", "sheets", "pillow", "pillow"]

inventory_len = len(inventory)
first = inventory[1]
last = inventory[-1]
inventory_2_6 = inventory[2:6]
first_3 = inventory[:3]
twin_beds = inventory.count("twin bed")
removed_item = inventory.pop(4)
inventory.insert(10,"19th Century Bed Frame")
inventory.sort()


# # Tuples in Python
# 
# Tuples hampir sama dengan tuples tapi tidak mutable. cara mendeklarasikan tuple yaitu dengan kurang biasa "()". 

# In[3]:


my_info= ("Muhammad Rizkillah", 29, "depok" )
print(my_info[1])
nama, angka, kota = my_info
print(nama)


# kasus kusus ketika mendeklarasikan tuples dengan satu elemen, kita harus menambahkan tanda koma "," di akhiran.

# In[8]:


one_element = (4)
print(one_element)
one_element1 = (4,)
print(one_element1)


# ## zip function in Python

# In[10]:


names = ["Jenny", "Alexus", "Sam", "Grace"]
heights = [61, 70, 67, 64]

name_and_height = zip(names, heights)
print(list(name_and_height))


# ## latihan list google it automation 

# In[2]:


#Given a list of filenames, we want to rename all the files with extension hpp to the extension h. To do this, we would like to generate a new list called newfilenames, consisting of the new filenames. Fill in the blanks in the code using any of the methods you’ve learned thus far, like a for loop or a list comprehension.
filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
newfilenames = []
for filename in filenames:
    if filename.endswith("hpp"):
        newfilenames.append(filename[:-3] + "h")
    else:
        newfilenames.append(filename)
print(newfilenames)


# #### Pertanyaan #2
# Let's create a function that turns text into pig latin: a simple text transformation that modifies each word moving the first character to the end and appending "ay" to the end. For example, python ends up as ythonpay.

# In[ ]:


def pig_latin(text):
  say = ""
  # Separate the text into words
  words = text.split()
  for word in words:
    # Create the pig latin word and add it to the list
    a = word[1:]+word[0] + "ay "
    say = say + a
    # Turn the list back into a phrase
  return say
		
print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"


# #### pertanyaan  #3
# The permissions of a file in a Linux system are split into three sets of three permissions: read, write, and execute for the owner, group, and others. Each of the three values can be expressed as an octal number summing each permission, with 4 corresponding to read, 2 to write, and 1 to execute. Or it can be written with a string using the letters r, w, and x or - when the permission is not granted.
#  For example: 
# 
#  
#  640 is read/write for the owner, read for the group, and no permissions for the others; converted to a string, it would be: "rw-r-----"
#  755 is read/write/execute for the owner, and read/execute for group and others; converted to a string, it would be: "rwxr-xr-x"
#  Fill in the blanks to make the code convert a permission in octal format into a string format.

# In[4]:


def octal_to_string(octal):
    result = ""
    value_letters = [(4,"r"),(2,"w"),(1,"x")]
    # Iterate over each of the digits in octal
    for i in [int(n) for n in str(octal)]:
        # Check for each of the permissions values
        for value, letter in value_letters:
            if i >= value:
                result += letter
                i -= value
            else:
                result += "-"
    return result
    
print(octal_to_string(755)) # Should be rwxr-xr-x
print(octal_to_string(644)) # Should be rw-r--r--
print(octal_to_string(750)) # Should be rwxr-x---
print(octal_to_string(600)) # Should be rw-------


# The group_list function accepts a group name and a list of members, and returns a string with the format: group_name: member1, member2, … For example, group_list("g", ["a","b","c"]) returns "g: a, b, c". Fill in the gaps in this function to do that.

# In[ ]:


def group_list(group, users):
  members = group+ ":"
  for user in users: 
    members = members + " " + user
    
  return members

print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", "")) # Should be "Users:"

