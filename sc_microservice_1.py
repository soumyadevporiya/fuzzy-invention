#!/usr/bin/env python
# coding: utf-8

# In[6]:


from flask import Flask


# In[7]:


app = Flask(__name__)


# In[8]:


@app.route('/')
def hello_world():
    return 'Hello World'


# In[12]:


@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello %s!' %name


# In[ ]:



# In[ ]:




