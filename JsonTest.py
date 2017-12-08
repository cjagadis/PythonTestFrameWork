
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib as mp
import matplotlib.pyplot as plt


# In[44]:






def checkJson(prod, test):
    jsprod = prod
    jstest = test
    i = 0
    j = 0
    for key in jsprod:
        i = i + 1
    for key in jstest:
        j = j + 1
    if i > j:
        return("Prod Schema is Greater than Test Schema")
    elif i < j:
        return("Prod Schema is smaller than Prod Schema")

    for key in jsprod:
        if jsprod[key] == jstest[key]:
            print("Prod " + str(jsprod[key]))
            print("Test " + str(jstest[key]))
        else:
            print("Prod " + str(jsprod[key]))
            print("Test " + str(jstest[key]))
            return("Data Mismatch")
    return("Data Match")

print("Test 1")
jsonprod = {'employeeid': 1, 'name': "jagadish", 'school': "University of Idaho", 'datejoined': "12-04-2017"}
jsontest = {'employeeid': 1, 'name': "jagadish", 'school': "University of Idaho", 'datejoined': "12-04-2017"}
t = checkJson(jsonprod,jsontest)
print(t)



#Test 2
jsonprod = {'employeeid': 1, 'name': "jagadish", 'school': "University of Idaho", 'datejoined': "12-04-2017"}
jsontest = {'employeeid': 1, 'name': "jagadish", 'school': "University of Idaho"}
t = checkJson(jsonprod,jsontest)
print(t)

#Test 3
jsonprod = {'employeeid': 1, 'name': "jagadish", 'school': "University of Idaho", 'datejoined': "12-04-2017"}
jsontest = {'employeeid': 1, 'name': "jagadish", 'school': "University of Idaho", 'datejoined': "12-04-2017", "coutnry": "USA"}
t = checkJson(jsonprod,jsontest)
print(t)

# In[49]:

# Test 4
jsonprod = {'employeeid': 1, 'name': "jagadish", 'school': "University of Idaho", 'datejoined': "12-04-2017"}
jsontest = {'employeeid': 1, 'name': "jagadish", 'school': "University of Idaho", 'datejoined': "12-05-2017"}
t = checkJson(jsonprod,jsontest)
print(t)

