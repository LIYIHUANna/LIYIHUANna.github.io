import os
import matplotlib.pyplot as plt
from thinkdsp import read_wave
from thinkdsp import decorate
from IPython.display import display
from ipywidgets import interact, fixed
from thinkdsp import SinSignal

wave3 = read_wave('C:/Users/38407/Desktop/2/数字信号处理/python/3python练习第一章/18871__zippi1__sound-bell-440hz.wav')
wave3.normalize()
wave3.make_audio()

def stretch(wave, factor):
    wave.ts *= factor
    wave.framerate /= factor

stretch(wave3, 0.3)
wave3.make_audio()
wave3.plot()

wave3.write(filename='output1-4.wav')
plt.show()