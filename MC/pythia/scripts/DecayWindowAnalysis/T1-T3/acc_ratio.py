# This script is two plot the difference between LHCb and CMS acceptance

import matplotlib.pyplot as plt
import numpy as np


mass = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
## for 10 cm 
y1 = [16,0,0,0,0,0,0,0,0,0]
y1 = [element / 10000 for element in y1]

## for 100 cm
y2 = [486,283,102,150,88,86,59,46,32,20]
y2 = [element / 10000 for element in y2]
## for 1000 cm
y3 = [305,287,267,291,302,222,238,193,172,157]
y3 = [element / 10000 for element in y3]

## for 10000 cm
x4 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
y4 = [52,39,32,57,46,47,60,45,51,39]
y4 = [element / 10000 for element in y4]


# CMS accpetance
# https://www.hepdata.net/record/ins1790827
y5 = [0.00085014,0.00048598,0.00062577,0.00082845,0.00062054,0.00064325,0.0007397,0.00056225,0.0004338,0.00037027]

y6 = [0.00061004,0.0024316,0.0038854,0.0051921,0.0050584,0.00598,0.0071477,0.0074629,0.007491,0.0079149]

y7 = [0.00015382,0.00028979,0.00091359,0.0011283,0.001012,0.001058,0.002202,0.0021455,0.002421,0.002421]

y8 = [1.6176e-05,2.5473e-05,5.5924e-05,0.00012573,0.00017215,0.00024393,0.00018914,0.00021643,0.00038493,0.00038831]


ratio10 = [(a-b)/b for a,b in zip(y1,y5)]
ratio100 = [(a-b)/b for a,b in zip(y2,y6)]
ratio1000 = [(a-b)/b for a,b in zip(y3,y7)]
ratio10000 = [(a-b)/b for a,b in zip(y4,y8)]

plt.plot(mass, ratio10,marker='o', linestyle='solid', color='r', label='10 cm ')
plt.plot(mass, ratio100,marker='o', linestyle='solid', color='b', label='100 cm ')
plt.plot(mass, ratio1000,marker='o', linestyle='solid', color='g', label='1000 cm ')
plt.plot(mass, ratio10000,marker='o', linestyle='solid', color='purple', label='10000 cm ')

plt.title(' Accpetance difference between LHCb and CMS (T1-T3)')
plt.xlabel('Mass (GeV)')
plt.ylabel('Accpetance Ratio (LHCb/CMS)')
plt.legend()
plt.savefig('acc_ratio.pdf')  
plt.show()
