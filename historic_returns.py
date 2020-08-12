#!/usr/bin/env python
# coding: utf-8

# ## Calculating the Return of stocks

# In[12]:


import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt


# In[76]:


tickers = ['HINDUNILVR.NS', 'RELIANCE.NS', 'BHARTIARTL.NS' ]
mydata = pd.DataFrame()
for t in tickers:
    mydata[t] = wb.DataReader(t, data_source='yahoo', start='2004-1-1')['Adj Close']


# In[40]:


mydata.dropna(axis=0, inplace= True)


# In[77]:


mydata.info()


# In[78]:


mydata['RELIANCE.NS'].plot(color= "red", figsize= (15,6), legend=True)
mydata['HINDUNILVR.NS'].plot(color= "BLUE", figsize= (15,6), legend=True)
mydata['BHARTIARTL.NS'].plot(color= "GREEN", figsize= (15,6), legend=True)
plt.xlabel("Year")
plt.ylabel("Price")
plt.title(" Stock price")
plt.show


# In[80]:


returns= (mydata / mydata.iloc[0] * 100)
returns['RELIANCE.NS'].plot(color= 'red', legend = True, figsize = (15, 6),);
returns['HINDUNILVR.NS'].plot(color= 'blue', legend = True, figsize = (15, 6),);
returns['BHARTIARTL.NS'].plot(color= 'green', legend = True, figsize = (15, 6),);
plt.xlabel("Year")
plt.ylabel("Return Percentage %")
plt.title("Stock Returns")
plt.show()


# *****

# In[85]:


returns = (mydata / mydata.shift(1)) - 1
returns.head()


# In[86]:


annual_returns = returns.mean() * 250
annual_returns


# In[88]:


pfolio_1 =('Annual return for the stocks of ' + str(round(annual_returns, 5) * 100) + ' %' )
print (pfolio_1)

