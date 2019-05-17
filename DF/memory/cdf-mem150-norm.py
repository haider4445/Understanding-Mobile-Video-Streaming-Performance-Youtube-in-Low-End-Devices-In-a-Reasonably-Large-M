
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches
roundtriptimes= [65.87,75.22,72.47,65.69,72.51,67.27,72.11]
roundtriptimes2 = [77.4,76.35,76.77,82.93,87.08,77.43]

xerror = [2.1,2.11,1.68,2.51,3.55,2.49,2.04]
xerror2 = [1.83,1.8,2.09,2.53,4.73,2.48]

sortedtime = np.sort(roundtriptimes)
p = 1. * np.arange(len(roundtriptimes))/(len(roundtriptimes) - 1)

sortedtime2 = np.sort(roundtriptimes2)
p2 = 1. * np.arange(len(roundtriptimes2))/(len(roundtriptimes2) - 1)

plt.errorbar(sortedtime2, p2,xerr = xerror2,label = "Some Line",color = "red", ecolor = "green",capsize = 5, capthick = 2,linewidth = 2,elinewidth = 1)

plt.errorbar(sortedtime, p,xerr = xerror,label = "Some Line",color = "blue", ecolor = "purple",capsize = 5, capthick = 2,linewidth = 2,elinewidth = 1)

red_patch = mpatches.Patch(color='red', label='512 MB RAM')
blue_patch = mpatches.Patch(color='blue', label='362 MB RAM')




plt.tick_params(labelsize=20)
plt.subplots_adjust( bottom=0.135)
plt.legend(handles=[red_patch,blue_patch],fontsize = 20)



plt.xlabel('Memory (MB)',fontsize = 20)
plt.ylabel('CDF',fontsize = 20)
plt.title('Memory on different videos when RAM is reduced',fontsize = 20)
plt.show()