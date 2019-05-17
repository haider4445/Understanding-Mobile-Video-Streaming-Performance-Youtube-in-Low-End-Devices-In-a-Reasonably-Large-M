
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches
roundtriptimes= [7.41,10.57,12.72,10.57,12.72,9.83,11.33,7.29,8.63,4.95,11.12]
roundtriptimes2 = [4.11,3.99,4.6,3.19,3.22,2.76,2.7,5.13,4.84]


sortedtime = np.sort(roundtriptimes)
p = 1. * np.arange(len(roundtriptimes))/(len(roundtriptimes) - 1)

sortedtime2 = np.sort(roundtriptimes2)
p2 = 1. * np.arange(len(roundtriptimes2))/(len(roundtriptimes2) - 1)

plt.plot(sortedtime2, p2,'-r')
plt.plot(sortedtime, p,'-b')
red_patch = mpatches.Patch(color='red', label='2 core')
blue_patch = mpatches.Patch(color='blue', label='1 core')



plt.tick_params(labelsize=20)
plt.subplots_adjust( bottom=0.135)
plt.legend(handles=[red_patch,blue_patch],fontsize = 20)



plt.xlabel('Startup Latency (seconds)',fontsize = 20)
plt.ylabel('CDF',fontsize = 20)
plt.title('Startup Latency on Different Cores on Youtube App',fontsize = 20)
plt.show()