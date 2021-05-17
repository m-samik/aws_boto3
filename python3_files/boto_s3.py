#!/usr/bin/env python
# coding: utf-8

# In[3]:


import boto3


# In[9]:


s3= boto3.resource('s3')


# In[10]:


s3


# In[11]:


s3.buckets.all()


# In[15]:


for i in s3.buckets.all():
    print(i)


# In[14]:


s3.create_bucket(Bucket='boto3.python',
                 CreateBucketConfiguration={'LocationConstraint': 'ap-south-1'})


# In[45]:


bucket=s3.Bucket('boto3.python')


# In[18]:


image = open('img.png','rb')


# In[20]:


bucket.put_object(Key = 'test_image.png' , Body = image)


# In[22]:


bucket


# In[40]:


bucket.objects.all()


# In[33]:


for i in bucket.objects.all():
    print("Bucket Name : "+i.bucket_name + "\tData :  "+ i.key)


# In[48]:


myobject=bucket.Object('test_image.png')


# In[49]:


myobject.download_file('test_image.png')


# In[ ]:




