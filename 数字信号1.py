import matplotlib.pyplot as plt
import numpy as np 

x = np.linspace(0, 3 * np.pi, 100)
y = np.sin(x)

plt.rcParams['font.sans-serif']=['SimHei'] 
plt.rcParams['axes.unicode_minus']=False 
plt.subplot(1,2,1)
plt.title(r'$f(x)=sin(x)$') 
plt.plot(x, y)

x1 = [t*0.375*np.pi for t in x]
y1 = np.sin(x1)
plt.subplot(1,2,2)
plt.title(r'$f(x)=sin(\omega x), \omega = \frac{3}{8} \pi$') 
plt.plot(x1, y1)
plt.show()