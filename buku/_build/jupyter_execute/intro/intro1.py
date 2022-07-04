#!/usr/bin/env python
# coding: utf-8

# # this is introduction to python 
# 
# at this point we have no idea what to do. 

# In[1]:


## asign value to python 
a = 10
print(type(a))


# 

# In[2]:


#codeacademy intro to python computer science 101 

quilt_width = 8 
quilt_length = 12 
print(quilt_width * quilt_length)

# for third question cahnge the value of quilt_width to 10 and quilt_length to 8 so the answer is 64 
quilt_length = 8 
print(quilt_width * quilt_length)


# In[3]:


# Calculation of squares for:
# 6x6 quilt
print(6**2)

# 7x7 quilt
print(7**2)
# 8x8 quilt
print(8**2)
# How many squares for 6 people to have 6 quilts each that are 6x6?
print(6**4)


# In[4]:


#food for thought: what number team are the two people next to you (26 and 28) on? What are the numbers for all 4 teams? (Optional Challenge Question)
my_team = 26
your_team = 28
print(my_team + your_team)


# In[5]:


string1 = "The wind, "
string2 = "which had hitherto carried us along with amazing rapidity, "
string3 = "sank at sunset to a light breeze; "
string4 = "the soft air just ruffled the water and "
string5 = "caused a pleasant motion among the trees as we approached the shore, "
string6 = "from which it wafted the most delightful scent of flowers and hay."

# Define message below:
message = string1 + string2 + string3 + string4 + string5 + string6


#print(message)
print(message)


# In[6]:


total_price = 0

new_sneakers = 50.00

total_price += new_sneakers

nice_sweater = 39.00
fun_books = 20.00
# Update total_price here:

print("The total price is", total_price + nice_sweater + fun_books)



# next task: 
# Create variables:
# 
# my_age
# half_my_age
# greeting
# name
# greeting_with_name
# Assign values to each using your knowledge of division and concatenation!

# In[7]:


# find solution fron next task 
name = "John"
my_age = 30
half_my_age = my_age / 2
greeting = "Hello" 
greeting_name = greeting + " " + name 

