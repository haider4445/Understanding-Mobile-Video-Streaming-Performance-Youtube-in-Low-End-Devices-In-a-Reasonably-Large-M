
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches
roundtriptimes= [0.06,0.13,0.09,0.07,0.12,5.87,0.11]
roundtriptimes2 = [0.05,0.08,167.72,107.07,193.31,0.08,21.11]



sortedtime = np.sort(roundtriptimes)
p = 1. * np.arange(len(roundtriptimes))/(len(roundtriptimes) - 1)

sortedtime2 = np.sort(roundtriptimes2)
p2 = 1. * np.arange(len(roundtriptimes2))/(len(roundtriptimes2) - 1)

plt.plot(sortedtime2, p2,'-r')
plt.plot(sortedtime, p,'-b')
red_patch = mpatches.Patch(color='red', label='Low Bandwidth')
blue_patch = mpatches.Patch(color='blue', label='High Bandwidth')



plt.tick_params(labelsize=20)
plt.subplots_adjust( bottom=0.135)
plt.legend(handles=[red_patch,blue_patch],fontsize = 20)



plt.xlabel('Rebuffering (seconds)',fontsize = 20)
plt.ylabel('CDF',fontsize = 20)
plt.title('Rebuffering on Different Bandwidths in Chrome',fontsize = 20)
plt.show()