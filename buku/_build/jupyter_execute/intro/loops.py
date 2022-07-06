#!/usr/bin/env python
# coding: utf-8

# # Loops 
# seringkali kita melakukan pengulangan suatu kode, padahal pada Python ada fitur yang bisa kita gunakan untuk melakukan pengulangan. yaitu for loop, while loop, dan for each loop. sebagai contoh dibawah ini:  

# In[1]:


print("This can be so much easier with loops!")
print("This can be so much easier with loops!")
print("This can be so much easier with loops!")
print("This can be so much easier with loops!")
print("This can be so much easier with loops!")
print("This can be so much easier with loops!")
print("This can be so much easier with loops!")
print("This can be so much easier with loops!")
print("This can be so much easier with loops!")
print("This can be so much easier with loops!")


# kita bisa menggunakan cara yang lebih efisien untuk melakukan pengulangan. yaitu dengan menggunakan looping.

# In[2]:


for i in range(10):
    print("This can be so much easier with loops!")


# seperti yang anda lihat di atas alih alih kita menulis 10 baris kode kini kita hanya butuh dua barus kode, dengan output yang sama. 

# ## for loop: sebuah pengenalan. 

# In[3]:


board_games = ["Settlers of Catan", "Carcassone", "Power Grid", "Agricola", "Scrabble"]

sport_games = ["football", "hockey", "baseball", "cricket"]

for game in board_games:
  print(game) 

for i in sport_games: 
  print(i)


# pada contoh diatas menunjukkan bagaimana penggunaan for loop bisa emudahkan kita untuk melakukan pengulangan. adapun cara mendeklarasikan for loop adalah dengan menuliskan kode seperti ini:
# 1. "for" digunakan sebagai reversed word yang menandakan awal dari suatu for loop. 
# 2. "i" dan "game" adalah variabel yang akan digunakan untuk mengisi nilai dari for loop. variable sementara ini bisa apa saja asalkan tidak reserved word. variable ini bisa digunakan di dalam block kode yang ada di dalam for loop.
# 3. "in" digunakan untuk memisahkan elemen dari list menjadi item tiap iterasinya. 
# 4. "sport_games" dan "board_games" adalah list yang akan digunakan untuk mengisi nilai dari for loop.
# 5. ":" digunakan untuk menandakan bahwa for loop akan dijalankan.
# 6. aksi. aksi yang dimaksud di sini adalah blok kode yang ada didalam for loop. 
# 

# ### for loop using range 
# kadang kala kita tidak ingin menulis kode yang sama untuk setiap iterasi, kita bisa menggunakan range. bedanya dengan for loop pada list adalah range akan mengisi nilai dari 0 sampai dengan batas yang ditentukan. tidak perlu menginisiasi list karena range akan mengisi nilai dari 0 sampai dengan batas yang ditentukan. 
# 

# In[4]:


promise = "I will finish the python loops module!"
for i in range(5):
  print(promise)


# ## While loop: sebuah pengenalan.

# In[5]:


count = 0
while count <= 3:
  # Loop Body
  print(count)
  count += 1


# mari kita breakdown kode diatas: 
# 1. count adalah variable yang akan digunakan untuk mengisi nilai dari while loop.
# 2. while merupakan reserved word yang menandakan awal dari suatu while loop.
# 3. "count <= 3" merupakan suatu kondisi yang akan dijalankan selama kondisi ini terpenuhi. 
# 4. "print(count)" merupakan kode yang akan dieksekusi selama kondisi pada poin 3 terpenuhi. 
# 5. "count+=1" sama dengan menambahkan nilai 1 pada variable count. hal ini digunakan agar while loop tidak terjebak dalam infinite iterasi. 
# 

# In[6]:


python_topics = ["variables", "control flow", "loops", "modules", "classes"]

#Your code below: 
length = len(python_topics)
index = 0 
while index < length: 
  print(python_topics[index])
  index += 1 


# In[7]:


python_topics = ["variables", "control flow", "loops", "modules", "classes"]

#Your code below: 
length = len(python_topics)
index = 0 
while index < length: 
  print("I am learning about "+python_topics[index])
  index += 1 


# ### Infinite Loop: warning, keadaan ini akan mengakibatkan program terjebak dan komputer anda crash. 
# infinite loop terjadi ketika loop tidak memiliki kondisi yang menghentikanya. hal ini mengakibatkan penuhnya memory dan cpu akan bekerja keras. sering kali infinite loop akan membuat program kita crash. pastikan kode anda tidak mengandung infinite loop. 
# 

# In[8]:


students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]

# for student in students_period_A:
#   students_period_A.append(student)
#   print(student)


# kode diatas merupakan kode yang mengandung infinite loop hari ini karena tiap kali kode pada blok for dijalankan akan menambahkan jumlah iterasi pada keseluruhan cell. hal ini menyebabkan infinite loop. saya beri tanda komen agar tidak terkompilasi saat "jupyter-book build" dijalankan.  

# ### cara menggabungkan 2 list dengan menggunakan for loop. 

# In[9]:


students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]

for student in students_period_A:
  students_period_B.append(student)
print(students_period_B)


# ### Loop Control: Break 
# sering kali kita tidak perlu mengiterasi seluruh koleksi (list, tuple) untuk mencari suatu nilai tertentu. kita bisa menggunakan break untuk menghentikan iterasi. break berguna untuk menghentikan iterasi. ketika kondisi pada break terpenuhi. maka akan berhenti dari iterasi. 

# In[10]:


dog_breeds_available_for_adoption = ["french_bulldog", "dalmatian", "shihtzu", "poodle", "collie"]
dog_breed_I_want = "dalmatian"

for dog_breed in dog_breeds_available_for_adoption:
  print(dog_breed)
  if dog_breed == dog_breed_I_want:
    print("They have the dog I want!")
    break


# ### Loop Control: Continue 
# continue berguna untuk melanjutkan iterasi. ketika kondisi pada continue terpenuhi, maka akan melanjutkan iterasi. dalam artian, kondisi yang terpenuhi oleh continue akan diabaikan. 

# In[11]:


big_number_list = [1, 2, -1, 4, -5, 5, 2, -9]
for i in big_number_list:
  if i <= 0:
    continue
  print(i)


# seperti yang anda duga bilangan negatif akan diabaikan, karena kita set kondisi untuk continue itu " 1 <= 0". 

# ##### perhatikan hal berikut: 
# sama dengan break, continue biasanya berpasangan dengan control flow seperti if, elif dan else. 
#  

# In[12]:


ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]

for i in ages: 
  if i < 21: 
    continue 
  print(i)


# ### nested Loop 
# 
# 

# In[13]:


sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]
scoops_sold = 0

for location in sales_data: 
  print(location)
  for i in location: 
    scoops_sold += i
print(scoops_sold)


# ### list comprehension 
# 
# Alih-alih menulis kode seperti dibawah ini:     

# In[14]:


numbers = [2, -1, 79, 33, -45]
doubled = []
 
for number in numbers:
  doubled.append(number * 2)
 
print(doubled)


# kita bisa menulis variable double dengan list comprehension yaitu seerti ini: 

# In[15]:


numbers = [2, -1, 79, 33, -45]
doubled = [num * 2 for num in numbers]
print(doubled)


# In[16]:


new_list = [<expression> for <element> in <collection>]


# mari kita breakdown bagaimana menggunakan list comprehension: 
# 1. inisiasi temporary variable yang meruapakan item dari list.
# 3. for adalah loop untuk element dari koleksi. 
# 3. element adalah item dari koleksi.
# 4. in menunjukkan bahwa item berada dalam koleksi.
# 5. kelekukan adalah adalah kumpulan data struktur yang akan di iterasi. 

# In[ ]:


grades = [90, 88, 62, 76, 74, 89, 48, 57]
scaled_grades = [num + 10 for num in grades]
print(scaled_grades)


# #### list comprehension using condition. 
# 

# In[10]:


import random 

a = [x for x in range(100) if random.randint(0, 1) == 0]
print(a)


# sekarang kita telah mendapatkan list dari angka ganjil dan genap dari 1 sampai 100. abaikan dulu apa itu random dalam python. intinya random itu memunculkan angka acak dari 0 sampai 100 secara acak. jika angka random = 1 maka hasil dari range akan diabaikan. sekarang bagaimana caranya kita bisa menjadikan list a menjadi list dari bilangan genap.  

# In[14]:


# b adalan list dari bilangan genap dengan mengalikan 2 bilangan ganjil pada list a. 
b = [z*2  for z in a if z % 2 == 1] 
print(b)


# mari kita breakdown lagi kode diatas:
# 1. [] adalah inisiasi dari list comprehension 
# 2. z*2 merupakan expresi yang akan dijalankan 
# 3. for adalah looping untuk element dari koleksi.
# 4. in menunjukkan bahwa item berada dalam koleksi.
# 5. if adalah kondisi yang membatasi for loop.
# 6. " z % 2 == 0" merupakan kondisi yang akan dijalankan. 

# kode diatas adalah list comprehension yang mengambil list a dan menjadikan bilangan ganjil pada list a menjadi list dari bilangan genap. selanjutnya kita akan mengantikan bilangan ganjil di list a dengan bilangan genap.

# In[12]:


for i in a: 
  if i % 2 == 0: 
    b.append(i * 2)
print(b)


# untuk mengecek apakah masih ada bilangan genap pada list a kita bisa menggunakan loop. 

# In[16]:


for i in a: 
    if i % 2 == 1: 
        break 
        print("bilangan ganjil ditemmukan")
    else: 
        print("bilangan ganjil tidak ditemukan")


# In[ ]:


heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]
can_ride_coaster = [x for x in heights if x > 161]
print(can_ride_coaster)
# dari codeacademy


# ## Review Loop 
# dari laman ini kita belajar: 
# - cara menulis for loop
# - menggunakan range pada for loop 
# - cara menulis while loop
# - apa itu infinite loop dan bagaimana cara untuk menghentikan infinite loop.
# - menggunakan break dan continue.
# - bagaimana list comprehension bekerja.

# In[18]:


# Your code below:
single_digits = [a for a in range(10)]
squares = []
for a in single_digits: 
  squares.append(a**2)
print(squares)
cubes = [i**3 for i in single_digits ]
print(cubes)

## solution for codeacademy loop review. 
  

