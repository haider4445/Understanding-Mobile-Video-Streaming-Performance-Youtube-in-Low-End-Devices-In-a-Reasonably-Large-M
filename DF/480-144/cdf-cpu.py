

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches
roundtriptimes= [20.81,20.17,19.74,20.16,20.67,19.54,20.52,19.97]
roundtriptimes2 = [24.43,24.66,22.61,23.58,25.71,24.3,23.66,24.81]

xerror = [3.81,3.84,2.88,3.52,3.19,4.12,4,3.2]
xerror2 =  [5.74,4.66,4.54,4.5,4.86,4.4,5.06,4.2]

sortedtime = np.sort(roundtriptimes)
p = 1. * np.arange(len(roundtriptimes))/(len(roundtriptimes) - 1)

sortedtime2 = np.sort(roundtriptimes2)
p2 = 1. * np.arange(len(roundtriptimes2))/(len(roundtriptimes2) - 1)

plt.errorbar(sortedtime2, p2,xerr = xerror2,label = "Some Line",color = "red", ecolor = "red",capsize = 5, capthick = 2,linewidth = 2,elinewidth = 1)

plt.errorbar(sortedtime, p,xerr = xerror,label = "Some Line",color = "blue", ecolor = "blue",capsize = 5, capthick = 2,linewidth = 2,elinewidth = 1)

red_patch = mpatches.Patch(color='red', label='144p')
blue_patch = mpatches.Patch(color='blue', label='480p')



plt.tick_params(labelsize=20)
plt.subplots_adjust( bottom=0.135)
plt.legend(handles=[red_patch,blue_patch],fontsize = 20)



plt.xlabel('CPU Utilization (% - Out of 100)',fontsize = 20)
plt.ylabel('CDF',fontsize = 20)
plt.title('CPU on different resolutions/bitrates',fontsize = 20)
plt.show()