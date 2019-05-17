
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches
roundtriptimes= [885,854,1010,854,982,907]
roundtriptimes2 = [426,825,663,643,674,156]



sortedtime = np.sort(roundtriptimes)
p = 1. * np.arange(len(roundtriptimes))/(len(roundtriptimes) - 1)

sortedtime2 = np.sort(roundtriptimes2)
p2 = 1. * np.arange(len(roundtriptimes2))/(len(roundtriptimes2) - 1)

plt.plot(sortedtime2, p2,'-r')
plt.plot(sortedtime, p,'-b')
red_patch = mpatches.Patch(color='red', label='Youtube Go')
blue_patch = mpatches.Patch(color='blue', label='Youtube App')




plt.tick_params(labelsize=20)
plt.subplots_adjust( bottom=0.135)
plt.legend(handles=[red_patch,blue_patch],fontsize = 20)


plt.xlabel('Total Dropped Frames',fontsize = 20)
plt.ylabel('CDF',fontsize = 20)
plt.title('Frame Drops on Youtube App and Youtube Go',fontsize = 20)
plt.show()