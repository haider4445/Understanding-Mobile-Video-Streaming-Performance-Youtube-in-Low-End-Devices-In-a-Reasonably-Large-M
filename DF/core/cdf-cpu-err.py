
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches
roundtriptimes= [28.36,34.94,33.2,32.59,33.2,33.06,33.12,33.57,34.07]
roundtriptimes2 = [46.7,45.2,48.21,47.93,44.52,47.6,48.21,47.52,44.46]

xerror = [8.22,6.69,5.84,6.59,6.28,7.39,6.984,8.56,7.35]
xerror2 = [8.4,7.1,9.06,8.07,6.62,8.9,7.53,8.96,7.50]

sortedtime = np.sort(roundtriptimes)
p = 1. * np.arange(len(roundtriptimes))/(len(roundtriptimes) - 1)

sortedtime2 = np.sort(roundtriptimes2)
p2 = 1. * np.arange(len(roundtriptimes2))/(len(roundtriptimes2) - 1)

plt.errorbar(sortedtime2, p2,xerr = xerror,label = "Some Line",color = "red", ecolor = "green",capsize = 5, capthick = 2,linewidth = 2,elinewidth = 1)

plt.errorbar(sortedtime, p,xerr = xerror2,label = "Some Line",color = "blue", ecolor = "purple",capsize = 5, capthick = 2,linewidth = 2,elinewidth = 1)

red_patch = mpatches.Patch(color='red', label='1 core')
blue_patch = mpatches.Patch(color='blue', label='2 core')



plt.tick_params(labelsize=20)
plt.subplots_adjust( bottom=0.135)
plt.legend(handles=[red_patch,blue_patch],fontsize = 20)



plt.xlabel('CPU Utilization (%-Out of 100)',fontsize = 20)
plt.ylabel('CDF',fontsize = 20)
plt.title('CPU Utilization on different cores in Youtube App',fontsize = 20)
plt.show()