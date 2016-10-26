
# coding: utf-8

# In[2]:

import numpy as np
k=9100
Premium_Call=179
Premium_Put=185
Interval=500
ST=np.arange(k-Interval,k+Interval)

ST


# In[4]:

Payoff_LongCall=np.maximum(ST-k,0)-Premium_Call
Payoff_ShortCall=-Payoff_LongCall


# In[7]:

import matplotlib.pyplot as plt
plt.plot(ST,Payoff_LongCall)
plt.plot(ST,Payoff_ShortCall)
plt.show()


# In[12]:

import numpy as np
k=9100
Premium_Call=179
Premium_Put=185
Interval=500
St=np.arange(k-Interval,k+Interval)

Payoff_LongPut=np.maximum(k-St,0)-Premium_Put
Payoff_ShortPut=-Payoff_LongPut


# In[13]:

import matplotlib.pyplot as plt
plt.plot(ST,Payoff_LongPut)
plt.plot(ST,Payoff_ShortPut)
plt.show()


# In[17]:

import numpy as np
K1=9100
K2=8700
Premium_Call=205
Premium_Put=175
Interval=500
ST=np.arange(K1-Interval,K2+Interval)
#ST


# In[21]:

Payoff_LongCall=np.maximum(ST-K1+ST-K2,0)-Premium_Call
Payoff_LongPut=np.maximum(K1-ST+K2-ST,0)-Premium_Put


# In[23]:

import matplotlib.pyplot as plt
plt.plot(ST,Payoff_LongCall)
plt.plot(ST,Payoff_LongPut)
plt.show()


# In[ ]:



