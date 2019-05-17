
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches
roundtriptimes= [36.39,28.408,36.44,30.32,36.44,25.69,28.28,4.39,26.8,21.83,26.22]
roundtriptimes2 = [0.59,3.77,6.55,5.4,2.02,6.67,3.87,5.12,6.98]



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



plt.xlabel('Rebuffering (seconds)',fontsize = 20)
plt.ylabel('CDF',fontsize = 20)
plt.title('Rebuffering on Different cores in Youtube App',fontsize = 20)
plt.show()