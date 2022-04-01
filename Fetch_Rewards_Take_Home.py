#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


users = pd.read_json('JSONS/users.json', lines=True)
receipts = pd.read_json('JSONS/receipts.json', lines=True)
brands = pd.read_json('JSONS/brands.json', lines=True)


# In[7]:


#When considering total number of items purchased from receipts with 'rewardsReceiptStatus’ of ‘Accepted’ or ‘Rejected’, which is greater?
#There is not an "Accepted" status for rewardsReceiptStatus in this dataset, so I will assume "FLAGGED" is the "Accepted" category.
#in this case the 'Rejected' status for rewardsReceiptStatus has a greater total number of items purchased.
receipts.groupby('rewardsReceiptStatus').count()


# In[8]:


#When considering average spend from receipts with 'rewardsReceiptStatus’ of ‘Accepted’ or ‘Rejected’, which is greater?
#With respect to the question above, following my same reasoning from the first question, the average spend of "FLAGGED"
# which will be considered the "ACCEPTED" status, is greater than the rejected status by an average of $153.12 rounded to the nearest tenth.
# This likely suggests that in order to receive an "ACCEPTED" status on the rewardsReceiptStatus, a user must spend a certain amount of money.
# This finding is inline with many other popular rewards programs consumers use today.
receipts.groupby('rewardsReceiptStatus').mean()


# In[ ]:


# The first data quality issue I see in the dataset is the representation of dates as NumPy objects, rather
# than datetime strings. This creates the issue of having unparseable dates if the data has the need to be reviewed
# in another computing language, like Python. Worst case scenario, some comparisons in this format can likely
# only be made in the environment where the datetimes retain their original structure, or the compression of the data
# into a JSON needs to be attempted again to maintain the datetime structure, or a non-compressed and non-serialized 
# file format should attempt to be used, like CSV.

