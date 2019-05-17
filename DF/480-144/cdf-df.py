
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches
roundtriptimes= [872,771,672,777,779,826,769,778]
roundtriptimes2 = [2481,2512,2034,2189,2627,2128,2303,2271]



sortedtime = np.sort(roundtriptimes)
p = 1. * np.arange(len(roundtriptimes))/(len(roundtriptimes) - 1)

sortedtime2 = np.sort(roundtriptimes2)
p2 = 1. * np.arange(len(roundtriptimes2))/(len(roundtriptimes2) - 1)

plt.plot(sortedtime2, p2,'-r')
plt.plot(sortedtime, p,'-b')
red_patch = mpatches.Patch(color='red', label='480p')
blue_patch = mpatches.Patch(color='blue', label='144p')



plt.tick_params(labelsize=10)
plt.subplots_adjust( bottom=0.135)
plt.legend(handles=[red_patch,blue_patch],fontsize = 8)


plt.xlabel('Total Dropped Frames',fontsize = 8)
plt.ylabel('CDF',fontsize = 8)
plt.title('Frame Drops on Different Bitrates/Resoultion',fontsize = 8)
plt.savefig('df-cdf-bitrates.png')
plt.show()