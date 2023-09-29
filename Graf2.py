import numpy as np
import matplotlib.pyplot as plt
plt.title('Задание 2')
plt.xlabel('x1')
plt.ylabel('x2')
plt.xlim(-5,20)
plt.ylim(-5,20)

plt.plot([-10,0, 6, 11], [27, 10, 0, -9], label='5x+3y>=30', color='Crimson', linestyle='dashed')
plt.plot([0, 3, 17], [-3, 0, 14], label='x-y<=3', color='Coral', linestyle='dashed')
plt.plot([0, -5, 17], [3, 0, 13], label='-3x+5y<=15', color='DarkGreen', linestyle='dashed')
plt.axvline(x=0, color='gray', linestyle='dashed')
plt.axhline(y=0, color='gray', linestyle='dashed')

plt.fill_between([3.075, 4.87, 15, 3.075], [4.84, 1.874, 12, 4.84], color='DarkCyan')

plt.arrow(0, 0, -1, 2, head_width=0.4, head_length=0.7, color='Black', label='вектор z')
plt.plot([-3, 3], [-2, 2], linestyle='dashdot', color='DarkBlue', label='перпендикуляр')

plt.plot(4.87,1.874,'o')
plt.text(4.87,1.874, 'max')
plt.plot(15,12,'o')
plt.text(15,12, 'min')
plt.grid()
plt.legend()
plt.show()