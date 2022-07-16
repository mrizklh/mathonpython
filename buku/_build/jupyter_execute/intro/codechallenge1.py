#!/usr/bin/env python
# coding: utf-8

# # code challenge 
# #### Larger Power 

# In[1]:


# Write your large_power function here:
def large_power(base, exponent):
  if base ** exponent > 5000: 
    return True 
  else: return False 
#Uncomment these function calls to test your large_power function:
print(large_power(2, 13))
# should print True
print(large_power(2, 12))
# should print False


# #### Over Budget 

# In[2]:


# Write your over_budget function here:
def over_budget(budget, food_bill, electricity_bill, internet_bill, rent):
  if budget - (food_bill+ electricity_bill+ internet_bill + rent ) < 0: 
    return True
  else: return False
# Uncomment these function calls to test your over_budget function:
print(over_budget(100, 20, 30, 10, 40))
# should print False
print(over_budget(80, 20, 30, 10, 30))
# should print True


# #### twice as large

# In[3]:


# Write your twice_as_large function here:
def twice_as_large(num1, num2): 
  if num1 > num2 *2: 
    return True 
  else:
    return False 
# Uncomment these function calls to test your twice_as_large function:
print(twice_as_large(10, 5))
# should print False
print(twice_as_large(11, 5))
# should print True


# #### divisible by ten

# In[4]:


def divisible_by_ten(num): 
  if num % 10 == 0: 
    return True 
  else: 
    return False 


# ### Control Flow: Advanced
# #### in range

# In[5]:


def in_range(num, lower, upper):
  if num >= lower and num <= upper: 
    return True
  else:
    return False  


# #### Same Name 

# In[6]:


def same_name(your_name, my_name):
  if your_name == my_name: 
    return True 
  else: 
    return False 


# #### always false 

# In[7]:


def always_false(num):
  if num > 10 and num < 5: 
    return True 
  else: return False 


# In[8]:


def retry(operation, attempts):
  for n in range(attempts):
    if operation():
      print("Attempt " + str(n) + " succeeded")
    
    
    else:
      print("Attempt " + str(n) + " failed")

retry(create_user, 3)
retry(stop_service, 5)


# In[ ]:


def factorial(n):
    result = 1
    for x in range(1,n):
        result = x * result
    return result

for n in range(0,9):
    print(n, factorial(n+1))


# In[1]:


def sum_divisors(n):
  sum = 0
  divisors = 1 
  while n > divisors: 
    if n % divisors ==0: 
      sum += divisors 
    divisors += 1 


  # Return the sum of all divisors of n, not including n
  return sum

print(sum_divisors(0))
# 0
print(sum_divisors(3)) # Should sum of 1
# 1
print(sum_divisors(36)) # Should sum of 1+2+3+4+6+9+12+18
# 55
print(sum_divisors(102)) # Should be sum of 2+3+6+17+34+51
# 114


# In[ ]:


def is_power_of_two(n):
    # make a function that take a number and return True if it is a power of two, otherwise return False
    if n == 0:
        return False
    while n % 2 == 0:
        n = n / 2
    if n == 1:
        return True
    else:
        return False

  

print(is_power_of_two(0)) # Should be False
print(is_power_of_two(1)) # Should be True
print(is_power_of_two(8)) # Should be True
print(is_power_of_two(9)) # Should be False


# In[ ]:


def print_prime_factors(number):
  # Start with two, which is the first prime
  factor = 2
  list = []
  # Keep going until the factor is larger than the number
  while factor <= number:
    # Check if factor is a divisor of number
    if number % factor == 0:
      # If it is, print it and divide the original number
      list.append(str(factor))
      # print(factor)
      number = number / factor
    else:
      # If it's not, increment the factor by one
      factor += 1
  
  print(', '.join(list))
  

print_prime_factors(25876858)
# Should print 2,2,5,5
# DO NOT DELETE THIS COMMENT

