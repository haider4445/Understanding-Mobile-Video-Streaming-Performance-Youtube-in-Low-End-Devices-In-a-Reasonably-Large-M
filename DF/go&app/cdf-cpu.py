
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches
roundtriptimes= [32.7,30.43,34.77,32.27,32.32,33.25]
roundtriptimes2 = [9.13,13.23,13.19,13.38,14.32,14.27]

xerror = [8.9,6.91,7.5,7.38,8.79,8.55]
xerror2 = [5.25,4.27,4.0,4.48,4.34,4.41]

sortedtime = np.sort(roundtriptimes)
p = 1. * np.arange(len(roundtriptimes))/(len(roundtriptimes) - 1)

sortedtime2 = np.sort(roundtriptimes2)
p2 = 1. * np.arange(len(roundtriptimes2))/(len(roundtriptimes2) - 1)

plt.errorbar(sortedtime2, p2,xerr = xerror2,label = "Some Line",color = "red", ecolor = "green",capsize = 5, capthick = 2,linewidth = 2,elinewidth = 1)

plt.errorbar(sortedtime, p,xerr = xerror,label = "Some Line",color = "blue", ecolor = "purple",capsize = 5, capthick = 2,linewidth = 2,elinewidth = 1)

red_patch = mpatches.Patch(color='red', label='Youtube Go')
blue_patch = mpatches.Patch(color='blue', label='Youtube App')





plt.tick_params(labelsize=20)
plt.subplots_adjust( bottom=0.135)
plt.legend(handles=[red_patch,blue_patch],fontsize = 20)



plt.xlabel('CPU Utilization (%-Out of 100)',fontsize = 20)
plt.ylabel('CDF',fontsize = 20)
plt.title('CPU of Youtube App and Youtube Go',fontsize = 20)
plt.show()