#!/usr/bin/env python
# coding: utf-8

# ## this is introdcution from code academy
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

