#!/usr/bin/env python
# coding: utf-8

# # First Python Program

# In[19]:


###Note semicolons used at the end of each statement want affected the code if used too
#Just print my fullname
print('My name is Rooney Mwathani')


# # Python uses indentation to indicate a block of code.
# 
# 

# In[18]:


#A program to compare to numbers
#If the comparison is false nothing will be displayed
if (2 > 5):
    print('5 is greater than 2')
else:
    print('5 is less than 2')
    


# # Python comments

# In[20]:


#used to do single comments
"""
Used to do multiple comments
"""
print(2+4)


# # Variables
# 

# In[22]:


#Variables are containers for storing data e.g x = 2, x is a container
#A program to multiply two numbers

x = 4
y = 4

#z = x * y
#print(z)

print(x * y)


# # Casting

# In[27]:


#It is the specification of variable type

x = int(3)
y = float(8.98)
print(x * y)


# # Get the Type
# 

# In[32]:


#used to check the type of a variable using type() function

x = 4
y = 5.90
z = "Rooney Mwathani"
j = True
type(j)


# # Single/Double quotes

# In[39]:


#strings cna be declared in single or double quotes

x = 'Joyce'
y = "Rooney"

print(x +'\n' + y)


# # Case sensetive

# In[42]:


#Variables are case sensetive e.g x is different from X
x = 34
X = 45

print(x)
print(X)


# # Variable Names

# In[47]:


#A variable name must start with a letter or the underscore character
#A variable name cannot start with a number
#A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
#Variable names are case-sensitive (age, Age and AGE are three different variables)

My_name2 = "My name"
print(My_name2)


# # Multi Words Variable Names
# 

# In[53]:


#Camel case - Each word begins with a uppercase except the first word

myName = "Rooney Mwathani"
print(myName)

#Pascal case - Each word starts with a capital

MyName = "Joyce Mwongeli"
print(MyName)

#Snake case - Each word is separated by an underscore character

Our_Names = myName + MyName
print(Our_Names)


# # Python Variables - Assign Multiple Values
# 

# In[57]:


x = 'Avocado', 'Tomatoes', 'Spinach','Lemon'
print(x)


# In[59]:


x, y, z = 'Potatoes','Sukuma Wiki','Pineapples'
print(x)
print(y)
print(z)


# # One Value to Multiple Variables
# 

# In[60]:


x=y=z = 'Chrome'
print(x)
print(y)
print(z)


# # Global Variables
# 

# In[67]:


#They are variables created outside the function and can be accessed outside and inside the function by everyone
# If you uncomment the the variable inside the function it will be displayed once the other one is commented out
MyName = 'Rooney Mwathani'

def myName():
    #MyName = 'Mwongeli Mwathani'
    print("My name is" + MyName)
    
myName()


# # The global Keyword
# 

# In[75]:


#The global keyword used to create variable inside the function
def myName():
    global MyName
    MyName = 'Joyce Rooney'
    #print("My name is" + MyName)
    
myName()

print("My name is" + MyName)


# In[ ]:




