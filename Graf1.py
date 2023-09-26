import numpy as np
import matplotlib.pyplot as plt
plt.title('Задание 1')
plt.xlabel('x1')
plt.ylabel('x2')
plt.xlim(-5,15)
plt.ylim(-5,15)

plt.plot([21/2, 0], [0, 21/3], label='2X1+3X2<=21', color='Crimson', linestyle='dashed')
plt.plot([0, 10], [10, 0], label='X1+X2<=10', color='Coral', linestyle='dashed')
plt.plot([0, 8], [8, 0], label='2X1+2X2<=16', color='DarkGreen', linestyle='dashed')
plt.axvline(x=0, color='gray', linestyle='solid')
plt.axhline(y=0, color='gray', linestyle='solid')

plt.fill_between([0, 0, 3,8], [0, 7, 5, 0], color='DarkCyan')

plt.arrow(0, 0, 2.7,  2, head_width=0.4, head_length=0.7, color='Black', label='вектор z')
plt.plot([-2, 2], [1.8, -1.8], linestyle='dashdot', color='DarkBlue', label='перпендикуляр')

plt.plot(8,0,'o')
plt.text(8,-1, 'max (8,0)')

plt.grid()
plt.legend()
plt.show()