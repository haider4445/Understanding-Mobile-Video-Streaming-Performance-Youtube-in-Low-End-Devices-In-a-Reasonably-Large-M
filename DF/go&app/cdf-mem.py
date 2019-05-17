
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches
roundtriptimes= [77.4,76.35,76.77,82.93,87.08,77.43]
roundtriptimes2 = [55.96,59.11,53.5,62.8,58.13]

xerror = [1.83,1.8,2.09,2.53,4.73,2.48]
xerror2 = [2.91,1.79,1.81,3.06,2.09]

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


plt.xlabel('Memory (MB)',fontsize = 20)
plt.ylabel('CDF',fontsize = 20)
plt.title('Memory of Youtube App and Youtube Go',fontsize = 20)
plt.show()