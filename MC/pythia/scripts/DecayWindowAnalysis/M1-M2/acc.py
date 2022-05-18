
# This script is plotting number of Events Produced that pass cuts vs Mass for low taus (10-100-1000 cm)
import matplotlib.pyplot as plt
import numpy as np


## for 1000 cm 
x1 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
y1 = [238,230,216,171,184,123,134,132,126,109]
y1 = [element / 10000 for element in y1]
plt.plot(x1, y1,marker='.', linestyle='solid', color='r', label='10000  cm')


## for 10000 cm 
x2 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
y2 = [40,43,46,36,58,40,46,48,42,30]
y2 = [element / 10000 for element in y2]
plt.plot(x2, y2,marker='.', linestyle='solid', color='g', label='10000 cm')

## for 100000 cm 
x3 = [100,200, 300, 400, 500, 600, 700, 800, 900, 1000]
y3 = [4,4,6,8,8,6,6,2,2,2]
y3 = [element / 10000 for element in y3]
plt.plot(x3, y3,marker='.', linestyle='solid', color='m', label='100000 cm')

## for 1000000 cm 
x4 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
y4 = [0,0,0,0,0,0,0,0,0,2]
y4 = [element / 10000 for element in y4]
plt.plot(x4, y4,marker='.', linestyle='solid', color='c', label='1000000 cm')



plt.yscale('log')
plt.title('LHCb Acceptance (M1-M2) vs Mass')
plt.xlabel('Mass (GeV)')
plt.ylabel('Acceptance')
plt.legend()
plt.savefig('acc_LHCb.pdf')  
plt.show()
