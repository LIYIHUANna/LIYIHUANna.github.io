import os
import matplotlib.pyplot as plt
import thinkdsp as dsp
from thinkdsp import read_wave
from thinkdsp import decorate
from IPython.display import display
from ipywidgets import interact, fixed

wave = read_wave('C:/Users/38407/Desktop/2/数字信号处理/python/3python练习第一章/18871__zippi1__sound-bell-440hz.wav')
wave.normalize()
wave.make_audio()
segment = wave.segment(start=1.1, duration=0.3)
segment.make_audio()
spectrum = segment.make_spectrum()
spectrum.low_pass(5000,0.1)
spectrum.make_wave().make_audio()
spectrum.plot()
wave.write(filename='output1-2.wav')
plt.show()


