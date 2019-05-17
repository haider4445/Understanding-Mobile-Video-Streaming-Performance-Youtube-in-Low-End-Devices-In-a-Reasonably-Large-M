
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches
roundtriptimes= [54.69,32.55,28.15,67.68,25.24,106.02]
roundtriptimes2 = [117.54,241.35,97.94,138.92,227.14]



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
plt.title('Rebuffering on Ufone 3G Network in Youtube App',fontsize = 20)
plt.show()