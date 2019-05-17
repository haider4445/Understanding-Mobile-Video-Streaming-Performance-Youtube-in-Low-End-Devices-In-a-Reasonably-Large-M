

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches
roundtriptimes= [107.41,138.55,97.8,78.32,138.55,104.51]
roundtriptimes2 = [115.34,109.28,118.32,104.25,93.82,136.73]

xerror = [129.17,152.42,76.98,99.24,63.35,121.23]
xerror2 = [118.54,106.53,117.08,115.71,99.79,103.8]

sortedtime = np.sort(roundtriptimes)
p = 1. * np.arange(len(roundtriptimes))/(len(roundtriptimes) - 1)

sortedtime2 = np.sort(roundtriptimes2)
p2 = 1. * np.arange(len(roundtriptimes2))/(len(roundtriptimes2) - 1)

plt.errorbar(sortedtime2, p2,xerr = xerror2,label = "Some Line",color = "red", ecolor = "red",capsize = 5, capthick = 2,linewidth = 2,elinewidth = 1)

plt.errorbar(sortedtime, p,xerr = xerror,label = "Some Line",color = "blue", ecolor = "blue",capsize = 5, capthick = 2,linewidth = 2,elinewidth = 1)

red_patch = mpatches.Patch(color='red', label='WiFi')
blue_patch = mpatches.Patch(color='blue', label='Ufone 3G')



plt.tick_params(labelsize=20)
plt.subplots_adjust( bottom=0.135)
plt.legend(handles=[red_patch,blue_patch],fontsize = 20)


plt.xlabel('Bandwidth Measured(Mbps)',fontsize = 20)
plt.ylabel('CDF',fontsize = 20)
plt.title('Bandwidth on Cellular Network and WiFi',fontsize = 20)
plt.show()