import numpy as np
import matplotlib.pyplot as plt

# data to plot
n_groups = 6
means_frank = (3740,3705,1928,1299,2046,2537)


means_guido = (940,1146,864,1089,993,1130)


# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.8

rects1 = plt.bar(index, means_frank, bar_width,
alpha=opacity,
color='b',
label='362 MB RAM')

rects2 = plt.bar(index + bar_width, means_guido, bar_width,
alpha=opacity,
color='g',
label='512 MB RAM')
plt.tick_params(labelsize=20)
plt.subplots_adjust( bottom=0.135)
plt.xlabel('Datasets',fontsize = 20)
plt.ylabel('Total Dropped Frames',fontsize = 20)
plt.title('Dropped Frames when Memory is reduced with different videos',fontsize = 20)
plt.xticks(index + bar_width, ('1', '2', '3', '4','5','6'))
plt.legend()

plt.tight_layout()
plt.show()