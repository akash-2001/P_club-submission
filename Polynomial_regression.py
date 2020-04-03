#!/usr/bin/env python
# coding: utf-8

# In[7]:


get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import * 
import numpy as np
np.random.seed(4)
x=np.random.normal(3.0,1.0,1000)
y=np.random.normal(50.0,20.0,1000)/x

scatter(x,y)


# In[8]:


import matplotlib.pyplot as plt

a=np.array(x)
b=np.array(y)

p9=np.poly1d(np.polyfit(a,b,9))

xp=np.linspace(0,6,300)
plt.scatter(x,y)

plt.plot(xp,p9(xp),c='b')

plt.show()


# In[ ]:




