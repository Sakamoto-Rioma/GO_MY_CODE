#!/usr/bin/env python
# coding: utf-8

# In[26]:


#Question1 : Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
#between 2000 and 3200 (both included). The numbers obtained should be printed in a sequence on a single line.


for i in range(2000,3201):
    if (i%7)==0 and (i%5)!=0:
        print(i, end=' ')
        
        


# In[27]:


#Question 2 Question: Write a program which can compute the factorial of a given numbers. The results should be printed in a sequence on a single line. Suppose the following input is supplied to the program: 8 Then, the output should be: 40320 

#Hints: In case of input data being supplied to the question, it should be assumed to be a console input. 

n= int(input('enter a given number: '))
f=1

if n!=0:
    for i in range(1,n+1):
        f=f*i
    print(f)
        
else:
    print(f)

   


# In[28]:


#Question 3 

#Question: With a given integral number n, write a program to generate a dictionary that contains (i, i*i) 
#such that is an integral number between 1 and n (both included). and then the program should print the dictionary. 
#Suppose the following input is supplied to the program: 8 Then, the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64} 

n = int(input('enter a given number: '))
dict = {1:1}
for i in range (1,n+1):
    dict[i]= i*i
print(dict)
      
    


# In[1]:


#Question 4 

#Given a non-empty string and an int n, return a new string where the char at index n has been removed. 
#The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive). 

#missing_char('kitten', 1) → 'ktten' 
#missing_char('kitten', 0) → 'itten' 
#missing_char('kitten', 4) → 'kittn' 

s = input('Enter a given word: ')
n = int(input('Enter a given number: '))
s = s[:n] + s[(n+1):]
print(s)


# In[37]:


#Question 5 

#Write a NumPy program to convert a NumPy array into a Python list structure.

#Expected Output: 

#Original array elements: [[0 1] [2 3] [4 5]] 

#Array to list: [[0, 1], [2, 3], [4, 5]] 

import numpy as np

arr = np.array([[0,1], [2,3], [4,5]])

print(arr)
list = arr.tolist()
print(list)


# In[44]:


#Question 6

#Write a NumPy program to compute the covariance matrix of two given arrays. 

#Original array1: [0 1 2] 

#Original array2: [2 1 0] 

#Covariance matrix of the said arrays: [[ 1. -1.] [-1. 1.]]
import numpy as np
array1 = np.array([0,1,2])
array2 = np.array([2,1,0])
print(np.cov(array1,array2))


# In[25]:


#Question 7

#Question: Write a program that calculates and prints the value according to the given formula: 
#Q = Square root of [(2 * C * D)/H] Following are the fixed values of C and H: C is 50. H is 30. 
#D is the variable whose values should be input to your program in a comma-separated sequence. 
#Example Let us assume the following comma separated input sequence is given to the program:
#100,150,180 The output of the program should be: 18,22,24 

import numpy as np
import math as m
c = 50
h = 30
d = [100,150,180]
output=[]

for i in d:
    value=round(m.sqrt(2*c*i/h))
    output.append(value)            
print(output)


# In[ ]:




