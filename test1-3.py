import os
import matplotlib.pyplot as plt
from thinkdsp import read_wave
from thinkdsp import decorate
from IPython.display import display
from ipywidgets import interact, fixed
from thinkdsp import SinSignal

wave2 = read_wave('C:/Users/38407/Desktop/2/数字信号处理/python/3python练习第一章/18871__zippi1__sound-bell-440hz.wav')
signal = (SinSignal(freq=400, amp=1.0) +
          SinSignal(freq=600, amp=0.5) +
          SinSignal(freq=800, amp=0.25))
wave2 = signal.make_wave(duration=1)
wave2.apodize()
wave2.make_audio()
signal += SinSignal(freq=450)
signal.make_wave().make_audio()
signal.plot()
wave2.write(filename='output1-3.wav')
plt.show()




