# import matplotlib
# import numpy as np 
# import tkinter as tk
# import matplotlib.animation as animation
# matplotlib.use("TkAgg")
# from matplotlib.figure import Figure
# from matplotlib import style
# from tkinter import ttk
# import pandas as pd
# import matplotlib.pyplot as plt
# import random
# from itertools import count

# plt.style.use('fivethirtyeight')

# # psi vs time
# psi = [1,2,3,4,5,6,7]
# time = [1,2,3,4,5,6,7]

# plt.plot(psi, time) 
# plt.show()



# import matplotlib.pyplot as plt


# plt.style.use('fivethirtyeight')

# time = [0, 1, 2, 3, 4, 5]
# pressure = [0, 1, 3, 2, 3, 5]

# plt.plot(time, pressure)
# plt.show()
# plt.tight_layout()
# plt.show()





# import random
# from itertools import count
# import pandas as pd
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation

# plt.style.use('fivethirtyeight')

# x_vals = []
# y_vals = []

# index = count()


# def animate(i):
#     data = pd.read_csv('data.csv')
#     x = data['x_value']
#     y1 = data['total_1']
#     y2 = data['total_2']

#     plt.cla()

#     plt.plot(x, y1, label='Channel 1')
#     plt.plot(x, y2, label='Channel 2')

#     plt.legend(loc='upper left')
#     plt.tight_layout()


# ani = FuncAnimation(plt.gcf(), animate, interval=1000)

# plt.tight_layout()
# plt.show()



import matplotlib as plt
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style

import tkinter as tk
from tkinter import ttk

big_font = ('Verdana', 12)
style.use("fivethirtyeight")

f = Figure(figsize=(5,5), dpi=100)
a = f.add_subplot(111)

def animate(i):
    pullData = open("sampleData.txt","r").read()
    dataList = pullData.split('\n')
    xList = []
    yList = []
    for eachLine in dataList:
        if len(eachLine) > 1:
            x, y = eachLine.split(',')
            xList.append(int(x))
            yList.append(int(y))
    a.clear()
    a.plot(xList, yList)




app = SeaofBTCapp()
ani = animation.FuncAnimation(f, animate, interval = 1000)
app.mainloop()


class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.frame.__init__(self, parent)
        label = tk.Label(self, text = "Page Two!!!", font = big_font)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text = "Back to Home", command = lambda: controller.show_frame(StartPage))
        button1.pack()

class PageThree(tk.Frame):
    def __init__(self, parent, controller):
        tk.frame.__init__(self, parent)
        label = tk.Label(self, text = "Graph Page!!!", font = big_font)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text = "Back to Home", command = lambda: controller.show_frame(StartPage))
        button1.pack()