#!/usr/bin/env python
# coding: utf-8

# # this is introdcution from code academy
# 1.
# Determine if the following statements are boolean expressions or not. If they are, set the matching variable to the right to "Yes" and if not set the variable to "No". Here’s an example of what to do:
# 
# Example statement:
# 
# My dog is the cutest dog in the world.
# This is an opinion and not a boolean expression, so you would set example_statement to "No" in the editor to the right. Okay, now it’s your turn:
# 
# Statement one:
# 
# Dogs are mammals.
# Statement two:
# 
# My dog is named Pavel.
# Statement three:
# 
# Dogs make the best pets.
# Statement four:
# 
# Cats are female dogs.

# In[1]:


example_statement = "No"

statement_one ="Yes"

statement_two ="No"

statement_three ="Yes"

statement_four ="No"


# In[2]:


#bool((5 * 2) - 1 == 8 + 1)
#bool(13 - 6 != (3 * 2) + 1)
bool(3 * (2 - 1) == 4 - 1)


# In[3]:


# Enter a user name here, make sure to make it a string
user_name = "angela_catlady_87"

if user_name == "Dave":
  print("Get off my computer Dave!")
if user_name == "angela_catlady_87":
    print("I know it is you, Dave! Go away!")



# In[4]:


statement_one = (2 + 2 + 2 >= 6) and (-1 * -1 < 0)

statement_two = (4 * 2 <= 8) and (7 - 1 == 6)

credits = 120
gpa = 3.4

if credits >= 120 and gpa >= 2.0:
  print("You meet the requirements to graduate!")


# ### Review 
# 
# Kali ini aku akan mereview kembali hasil pembelajaran kita pada kendali alir ini *control flow* ini. sebelum kendali alir kita tahu komputer bisa melakukan beberapa primitif operasi yaitu tambah, kurang, kali, bagi, dan modulus. 
# 
# Ekspresi boolean adalah sebuah kondisi yang menghasilkan nilai true (dengan True t huruf kapital) atau begitu juga dengan false false. suatu variable boolean adalah variable yang menyimpan nilai true or false. kita bisa membuat ekspresi boolean dengan operator: 
# - " and " untuk dan 
# - " or " untuk atau
# - " not " untuk negasi
# - " == " untuk sama dengan
# - " != " untuk tidak sama dengan
# - " > " untuk lebih besar dari
# - " < " untuk lebih kecil dari
# - " >= " untuk lebih besar sama dengan
# - " <= " untuk lebih kecil sama dengan
# - " in " untuk mengecek apakah ada di dalam sebuah list
# - " not in " untuk mengecek apakah tidak ada di dalam sebuah list
# - " is " untuk mengecek apakah ada di dalam sebuah objek
# - " is not " untuk mengecek apakah tidak ada di dalam sebuah objek
# 
# https://www.w3schools.com/python/python_operators.asp
# 
# ### Pernyataan If, Else, dan Else If
# if digunakan ketika kita ingin mengecek apakah suatu kondisi terpenuhi atau tidak. jika kondisi terpunuhi maka blok kode akan dieksekusi. sedangakan untuk elif dieksekusi hanya jika kondisi if sebelumnya terpenuhi. jika tidak terpenuhi maka akan dieksekusi blok kode else. 
#  

# In[5]:


print( (4 <= 2 * 3) and (7 + 1 == 8))


# ### Error di Python Review 
# 
# jadi ada tiga macam error yang bisa terjadi di Python:
# - nameerror: adalah error yang menandakan bahwa sebuah nama yang kita gunakan tidak ada di dalam sebuah objek.
# - typeerror: adalah error yang menandakan bahwa sebuah operasi yang kita lakukan dengan objek yang salah.
# - syntaxerror: adalah error yang menandakan bahwa kode yang kita buat tidak benar.
# 
# 

# In[6]:


#declare a int variable without assigning a value

