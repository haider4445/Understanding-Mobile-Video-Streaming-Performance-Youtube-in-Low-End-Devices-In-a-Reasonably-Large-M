
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches
roundtriptimes= [10.77,5.13,20.76,11.74,8.35,9.21,6.87]
roundtriptimes2 = [18.21,17.45,26.78,21.23,22.87,18.88,21.11]



sortedtime = np.sort(roundtriptimes)
p = 1. * np.arange(len(roundtriptimes))/(len(roundtriptimes) - 1)

sortedtime2 = np.sort(roundtriptimes2)
p2 = 1. * np.arange(len(roundtriptimes2))/(len(roundtriptimes2) - 1)

plt.plot(sortedtime2, p2,'-r')
plt.plot(sortedtime, p,'-b')
red_patch = mpatches.Patch(color='red', label='Low Bandwidth')
blue_patch = mpatches.Patch(color='blue', label='High Bandwidth')



plt.tick_params(labelsize=20)
plt.subplots_adjust( bottom=0.135)
plt.legend(handles=[red_patch,blue_patch],fontsize = 20)



plt.xlabel('Startup Latency (seconds)',fontsize = 20)
plt.ylabel('CDF',fontsize = 20)
plt.title('Startup Latency on Different Bandwidths in Chrome',fontsize = 20)
plt.show()