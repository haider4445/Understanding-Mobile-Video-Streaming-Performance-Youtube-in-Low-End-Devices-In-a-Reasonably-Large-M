
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches
roundtriptimes= [938,993,902,850,853,999,918,1148,1054]
roundtriptimes2 = [2314,1337,1678,1445,2272,1124,1340,1394,1807]

sortedtime = np.sort(roundtriptimes)
p = 1. * np.arange(len(roundtriptimes))/(len(roundtriptimes) - 1)
sortedtime2 = np.sort(roundtriptimes2)
p2 = 1. * np.arange(len(roundtriptimes2))/(len(roundtriptimes2) - 1)
plt.plot(sortedtime2, p2,'-r')
plt.plot(sortedtime, p)
red_patch = mpatches.Patch(color='red', label='1 core')
blue_patch = mpatches.Patch(color='blue', label='2 core')
plt.tick_params(labelsize=20)
plt.subplots_adjust( bottom=0.135)
plt.legend(handles=[red_patch,blue_patch],fontsize = 20)
plt.xlabel('Total Dropped Frames',fontsize = 20)
plt.ylabel('CDF',fontsize = 20)
plt.title('Dropped Frames on different cores in Youtube App',fontsize = 20)
plt.show()