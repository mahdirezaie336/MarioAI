import matplotlib.pyplot as plt


line_up, = plt.plot([1, 2, 3])
line_down, = plt.plot([3, 2, 1])
plt.legend([line_up, line_down], ['Line Up', 'Line Down'])
plt.show()
