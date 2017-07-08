
# coding: utf-8

# In[1]:

import pandas as pd
import requests
import httplib, urllib
#'http://localhost:8086/write?db=LIVINGHOPE' --data-binary 'cpu_load_short,host=server02 value=0.67
conn = httplib.HTTPConnection("localhost",8086)
conn.request("POST", "", 'cpu_load_short,host=server02 value=0.67')
response = conn.getresponse()
response


# In[9]:

data = pd.read_csv('/Users/yusuf/Downloads/chart_new.csv')


# In[27]:

data_list = []
for i in data.columns[2:]:
    datatmp = data[['DateTime', i]].dropna()
    datatmp['Zone'] = i
    datatmp.columns = ['DateTime','Temperature','Zone']
    data_list.append(datatmp)


# In[93]:

for i in data_list[0]:
    print(i)


# In[98]:

data_list[0].iloc[5]


# In[25]:

data_all = pd.concat(data_list)


# In[ ]:




# In[155]:


data_list[0].iloc[1000]


# In[173]:

data_list[3]


# In[162]:

def parsedata(data):
    if "Steam" not in data['Zone']:
        zone = data['Zone'][14:].replace(' ','_')
    else:
        zone = data['Zone'].replace(' ','_')
    value ='temp,location='+ zone +',region=us_west value=' + str(data['Temperature'])+ ' ' + str(int(data['DateTime']))
    return value


# In[ ]:




# In[ ]:




# In[ ]:




# In[169]:

for z in data_list:
    for i in z.index:
        data = parsedata(z.loc[i])
        print(data)


# In[170]:

for z in data_list:
    for i in z.index:
        data = parsedata(z.loc[i])
        r = requests.post(url='http://localhost:8086/write?db=LIVINGHOPE', data=data, headers={'Content-Type': 'application/octet-stream'})
        print(r.status_code, r.reason)


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



