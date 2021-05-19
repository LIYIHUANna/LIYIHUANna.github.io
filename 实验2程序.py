import matplotlib.pyplot as plt#把matplotlib.pyplot库定义为plt
import numpy as np #把numpy库定义为np

x = np.linspace(0, 3*np.pi, 100)#在x轴上0到3*pi上分布100个点
y = np.sin(x)#y轴为sin（x）

plt.rcParams['font.sans-serif']=['SimHei'] #加上这一句就能在图表中显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
plt.subplot(1,2,1)#自上往下第一个，自左往右的2个里的第一个

plt.title(r'$f(x)=sin(x)$') #定义第一个图的标题
plt.plot(x, y)#输出

x1 = [t*0.375*np.pi for t in x]#定义x轴长度，把t的值赋给x
y1 = np.sin(x1)#y轴为sin（x1）
plt.subplot(1,2,2)#自上往下第一个，自左往右的2个里的第二个
plt.title(r'$f(x)=sin(\omega x), \omega = \frac{3}{8} \pi$') #定义第二个图的标题
plt.plot(x1, y1)#输出
plt.show()#结束