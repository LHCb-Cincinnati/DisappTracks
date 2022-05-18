
# This script is plotting number of Events Produced that pass cuts vs Mass
import matplotlib.pyplot as plt
import numpy as np

## for 1000 cm 
x1 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
y1 = [238,230,216,171,184,123,134,132,126,109]
y1 = [element / 10000 for element in y1]
xsec_prod = [2.428e-08,1.902e-09,3.969e-10,1.229e-10,4.592e-11,1.984e-11 ,9.366e-12,4.775e-12,2.175e-12,1.328e-12]
xsec_prod = [element * 1e-3 for element in xsec_prod]

 # https://lhcb.web.cern.ch/speakersbureau/html/PerformanceNumbers.html
L = 5.7e15 # LHCb run 2 integrated lumniosity
N1 = L * np.multiply(y1,xsec_prod) 
plt.plot(x1, N1,marker='x', linestyle='solid', color='r', label='1000 cm')


## for 10000 cm 
x2 = [100,200, 300, 400, 500, 600, 700, 800, 900, 1000]
y2 = [40,43,46,36,58,40,46,48,42,30]
y2 = [element / 10000 for element in y2]
N2 = L * np.multiply(y2,xsec_prod) 
plt.plot(x2, N2,marker='x', linestyle='solid', color='b', label='10000 cm')

## for 100000 cm 
x3 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
y3 = [4,4,6,8,8,6,6,2,2,2]
y3 = [element / 10000 for element in y3]

N3 = L * np.multiply(y3,xsec_prod) 
plt.plot(x3, N3,marker='x', linestyle='solid', color='g', label='100000 cm')

## for 1000000 cm 

x4 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
y4 = [0,0,0,0,0,0,0,0,0,2]
y4 = [element / 10000 for element in y4]

N4 = L * np.multiply(y4,xsec_prod) 
plt.plot(x4, N4,marker='x', linestyle='solid', color='y', label='1000000 cm')

plt.yscale('log')
plt.title('Number of Events in M1-M2 region vs Mass')
plt.xlabel('Mass (GeV)')
plt.ylabel('Number of Events')
plt.legend()
plt.savefig('nEvent_M1-M2.pdf')  
plt.show()
