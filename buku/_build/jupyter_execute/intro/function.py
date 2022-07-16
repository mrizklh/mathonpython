#!/usr/bin/env python
# coding: utf-8

# # Function 
# ## Pengenalan 
# sama seperti di matematika, fungsi adalah sebuah kumpulan kode yang dapat menghasilkan suatu nilai. fungsi bisa butuh input (parameter) dan output (return value). sama seperti pada contol flow dan loop. blok kode dalam fungsi bersifat local. dan fungsi setelah diinisiasi bisa dipanggil di dalam blok kode lain, atau bahkan di dalam kode itu sendiri. 

# In[1]:


def hello():
    print("Hello World")
hello()


# fungsi diatas merupakan contoh sederhana suatu funsi dalam python, fungsi diatas tidak memiliki argument.  

# ### Mendeklarasikan Fungsi
# 

# In[2]:


def nama_fungsi(argument, umur): 
    print(argument)
    if int(umur) < 20: 
        return "Anda masih muda"
nama_fungsi(input("Masukkan nama: "), input("Masukkan umur: "))


# mari kita breakdown kode diatas: 
# - def merupakan reserved word yang digunakan untuk deklarasi fungsi.
# - "nama_fungsi" adalah nama yang akan diberikan kepada fungsi.
# - "argument, umur" merupakan argument/parameter/input yang akan diproses oleh fungsi
# - blok kode yang di dalam fungsi merupakan aksi yang akan dijalankan ketika fungsi dipanggil. 
# - return merupakan keyword yang digunakan untuk mengembalikan nilai dari fungsi.
# - "nama_fungsi(input("Masukkan nama: "), input("Masukkan umur: "))" adalah pemanggilan fungsi beserta input yang akan dijalankan. input() itu sendiri sebenarnya juga fungsi yang built-in di Python. 
# 

# ### Argument 

# In[ ]:


# Your code below:
def generate_trip_instructions(location):
  print("Looks like you are planning a trip to visit"+ location)
  print("You can use the public subway system to get to" + location )
generate_trip_instructions("Grand Central Station")


# ### multiple argument function. 

# In[ ]:


# Write your code below: 
def calculate_expenses(plane_ticket_price, car_rental_rate, hotel_rate, trip_time):
  car_rental_total = car_rental_rate * trip_time 
  hotel_total = hotel_rate * trip_time -10
  print(car_rental_total + hotel_total + plane_ticket_price)
calculate_expenses(200, 100, 100, 5)


# ### tipe argument
# ada tiga macam argument yang bisa kita pakai pada fungsi yaitu: 
# - posisional argument: argument yang bisa dipanggil dengan posisinya pada saat fungsi didefinisikan. 
# - keyword argument: argument yang bisa dipanggil dengan nama yang sama seperti nama variabel.
# - default argument: argument yang bisa dipanggil dengan nama yang sama seperti nama variabel. dan nilai default yang akan diisi jika tidak ada input.
# 

# #### Positional Argument
# posisitional argument adalah argument yang bisa dipanggil dengan posisinya pada saat fungsi didefinisikan. tipe argument ini biasanya dipakai untuk fungsi sederhana. 
# #### keyword argument
# keyword argument adalah argument yang bisa dipanggil dengan nama yang sama seperti nama variabel. tipe argument ini biasanya dipakai untuk fungsi yang lebih kompleks.

# In[8]:


def calculate_taxi_price(miles_to_travel, rate, discount):
  print(miles_to_travel * rate - discount )
calculate_taxi_price(rate=0.5, discount=10, miles_to_travel=100)


# #### Default Argument
# terakhir, terkadang kita ingin menjadikan suatu nilai dari argument itu sudah ada alias nilai default. untuk itulah tipe argument ini dipakai. cara menggunakannya adalah dengan menggunakan tanda "=" pendefinisian fungsi. 

# In[9]:


def calculate_taxi_price(miles_to_travel, rate, discount = 10):
  print(miles_to_travel * rate - discount )
calculate_taxi_price(miles_to_travel=100, rate=0.5)


# pada contoh diatas kita tidak perlu menuliskan nilai argument discount, hal ini bisa terjadi karena kita menggunakan default argument, sehingga argument ketiga menajadi optional. 

# In[10]:


# Write your code below:
def trip_planner(first_destination, second_destination, final_destination= "Codecademy HQ"):
  print("Here is what your trip will look like!")
  print("First, we will stop in " + first_destination +", then " + second_destination+ ", and lastly " + final_destination)
trip_planner("France", "Germany", "Denmark")
trip_planner("Denmark", "France", "Germany")
trip_planner(first_destination="Iceland", second_destination="India", final_destination="Germany")
trip_planner("Brooklyn", "Queens")


# ### Built-in Functions vs User Defined Functions
# Di Python, kita bisa membuat fungsi sendiri. namun, Bahasa Pemrograman Python memiliki fungsi yang sudah ada. istilahnya built-in function. print() adalah built-in function. len() juga build in function. yang kita pelajari di laman ini adalah user defined function, yaitu fungsi yang bisa kita buat sendiri. bukankah itu hal yang menakjubkan, kita bisa ekstensi bahasa python dengan menggunakan fungsi sendiri. begitu juga dengan library dan module. tapi itu akan kita plajari nanti. 

# In[ ]:


tshirt_price = 9.75
shorts_price = 15.50
mug_price = 5.99
poster_price = 2.00

# Write your code below:

# Checkpoint 1
max_price = max(tshirt_price, shorts_price, mug_price, poster_price)
print(max_price)

# Checkpoint 2
min_price = min(tshirt_price, shorts_price, mug_price, poster_price)
print(min_price)

# Checkpoint 3
rounded_price = round(tshirt_price, 1)
print(rounded_price)


# #### Variable accessible inside a function
# 
# suatu variable yang didifinisikan di dalam fungsi ini bisa dipanggil di luar fungsi tersebut. seperti yang anda lihat pada kode di bawah. variable a yang didifinisikan di dalam fungsi ini tidak bisa dipanggil di luar fungsi tersebut. hal ini karena *scope* atau jangkauan dari useable variable tersebut cuma sebatas di dalam fungsi tersebut. Namun, kita bisa menggunakan variable yang didefinisikan secara global ke dalam fungsi. 
# 

# In[16]:


def test_fungsi(argument):
    a = 0 
    print(argument)
test_fungsi("Hello World")
print(a)


# In[17]:


favorite_locations = "Paris, Norway, Iceland"
def print_count_locations():
  
  print("There are 3 locations")
    
# This function will print the favorite locations
def show_favorite_locations():
  print("Your favorite locations are: " + favorite_locations)

print_count_locations()
show_favorite_locations()


# contoh diatas merupakan salah satu contoh dari variable yang didifinisikan secara global dan diakses di dalam fungsi.yaitu variable "favorite_location". 

# ### Return Value 
# 
# selain dengan menggunakan print() function. kita juga bisa menggunakan reserved word return untuk mengembalikan nilai dari fungsi. return berfunsi sebagai yang mengeluarkan nilai dari fungsi. 

# In[20]:


def hello(name):
  return "Hello " + name

hello("John")


# pada kode diatas kita tidak perlu menggunakan print function karena sudah kata return sudah mencukupi. 

# In[ ]:


current_budget = 3500.75

def print_remaining_budget(budget):
  print("Your remaining budget is: $" + str(budget))

print_remaining_budget(current_budget)

# Write your code below: 
def deduct_expense(budget, expense):
  return budget - expense

shirt_expense = 9

new_budget_after_shirt = deduct_expense( current_budget, shirt_expense )

print_remaining_budget(new_budget_after_shirt)


# #### Multiple return 
# 
# gunakan koma untuk memisahkan nilai yang akan dikembalikan. 
# 

# In[1]:


def span_of_time(start_time, end_time):
  return start_time, (end_time - start_time)
span_of_time(10, 20)


# In[ ]:


def top_tourist_locations_italy():
  first = "Rome"
  second = "Venice"
  third = "Florence"
  return first, second, third
most_popular1, most_popular2, most_popular3 = top_tourist_locations_italy()
print(most_popular1)
print(most_popular2)
print(most_popular3)    


# ## review Function
# di laman ini kita belajar: 
# - kapan menggunakan suatu fungsi.
# - apa itu fungsi dalam python dan bagaimana mendeklarasikan fungsi.
# - bagaimana indentation pada kode python.
# - bagaimana memasukkan input ke dalam fungsi. 
# - perbedaan build-in function dan user defined function.
# - berbagai macan tipe argument
# - return value 
# - scope of variable. 

# In[6]:


# Write your code below:

def trip_planner_welcome(name): 
  print("Welcome to tripplanner v1.0 " + name)

trip_planner_welcome(" <YOUR NAME HERE> ")

def estimated_time_rounded(estimated_time):
  rounded_time = round(estimated_time)
  return rounded_time

estimate = estimated_time_rounded(2.43)

def destination_setup(origin, destination, estimated_time, mode_of_transport="Car"):
  print("Your trip starts off in " + origin)
  print("And you are traveling to " + destination)
  print("You will be traveling by " + mode_of_transport)
  print("It will take approximately " + str(estimated_time) + " hours")


destination_setup(" <PICK AN ORIGIN> ", "<PICK A DESTINATION > ", estimate, "Car")

