from thinkdsp import Sinusoid
from thinkdsp import normalize, unbias
from thinkdsp import TriangleSignal
from thinkdsp import decorate
from thinkdsp import SquareSignal
import os
import numpy as np
import matplotlib.pyplot as plt
triangle = TriangleSignal(440).make_wave(duration=0.01)
triangle.plot()
spectrum = triangle.make_spectrum()
print(spectrum.hs[0])
spectrum.hs[0] = 100 
triangle.plot(color='gray')
spectrum.make_wave().plot()    
plt.show()