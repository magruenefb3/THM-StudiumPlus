import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
x= pd.period_range(pd.datetime.now(), periods = 200, freq ='d')
x= x.to_timestamp().to_pydatetime()
y = np.random.randn(200,3).cumsum(0)
plt.title('Random trends')
plt.xlabel('Date')
plt.ylabel('Cum. sum')
plt.figtext(0.995, 0.01, u'Acme designs 2015', ha='right', va = 'bottom')
plt.plot(x,y)
plt.show()
