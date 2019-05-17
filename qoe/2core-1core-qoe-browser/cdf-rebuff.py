
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches
roundtriptimes= [0.11,0.16,0.09,0.01,12.99]
roundtriptimes2 = [61.46,127.41,0.07,167.39,172.37,50.33,124.01,175.18,0.07]



sortedtime = np.sort(roundtriptimes)
p = 1. * np.arange(len(roundtriptimes))/(len(roundtriptimes) - 1)

sortedtime2 = np.sort(roundtriptimes2)
p2 = 1. * np.arange(len(roundtriptimes2))/(len(roundtriptimes2) - 1)

plt.plot(sortedtime2, p2,'-r')
plt.plot(sortedtime, p,'-b')

red_patch = mpatches.Patch(color='red', label='1 core')
blue_patch = mpatches.Patch(color='blue', label='2 core')


plt.tick_params(labelsize=20)
plt.subplots_adjust( bottom=0.135)
plt.legend(handles=[red_patch,blue_patch],fontsize = 20)



plt.xlabel('Rebuffering (seconds)',fontsize = 20)
plt.ylabel('CDF',fontsize = 20)
plt.title('Rebuffering on Different Cores in Chrome',fontsize = 20)
plt.show()