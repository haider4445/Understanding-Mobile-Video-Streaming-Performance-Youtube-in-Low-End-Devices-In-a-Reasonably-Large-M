
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches
roundtriptimes= [4.14,8.51,6.02,3.79,9.02,3.47]
roundtriptimes2 = [3.99,5.72,5.07,2.04,3.59,3.51,4.73]



sortedtime = np.sort(roundtriptimes)
p = 1. * np.arange(len(roundtriptimes))/(len(roundtriptimes) - 1)

sortedtime2 = np.sort(roundtriptimes2)
p2 = 1. * np.arange(len(roundtriptimes2))/(len(roundtriptimes2) - 1)

plt.plot(sortedtime2, p2,'-r')
plt.plot(sortedtime, p,'-b')
red_patch = mpatches.Patch(color='red', label='WiFi')
blue_patch = mpatches.Patch(color='blue', label='3G Ufone')



plt.tick_params(labelsize=20)
plt.subplots_adjust( bottom=0.135)
plt.legend(handles=[red_patch,blue_patch],fontsize = 20)



plt.xlabel('Startup Latency (seconds)',fontsize =  20)
plt.ylabel('CDF',fontsize = 20)
plt.title('Startup Latency on Cellular/WiFi Network in Youtube App',fontsize = 20)
plt.show()